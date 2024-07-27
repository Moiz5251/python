from flask import Flask, render_template, jsonify, request
import requests
import urllib.parse
import datetime
from creds import credentials

app = Flask(__name__)

@app.route('/get-orders', methods=['GET'])
def get_orders():
    try:
        # Getting the LWA access token using the Seller Central App credentials. The token will be valid for 1 hour until it expires.
        token_response = requests.post(
            "https://api.amazon.com/auth/o2/token",
            data={
                "grant_type": "refresh_token",
                "refresh_token": credentials["refresh_token"],
                "client_id": credentials["lwa_app_id"],
                "client_secret": credentials["lwa_client_secret"],
            },
        )
        token_response.raise_for_status()  # Check for HTTP errors
        access_token = token_response.json().get("access_token")
        if not access_token:
            return "Failed to retrieve access token", 500

        # North America SP API endpoint (from https://developer-docs.amazon.com/sp-api/docs/sp-api-endpoints)
        endpoint = "https://sellingpartnerapi-eu.amazon.com"

        # US Amazon Marketplace ID (from https://developer-docs.amazon.com/sp-api/docs/marketplace-ids)
        marketplace_id = "A21TJRUUN4KGV"

        # Downloading orders (from https://developer-docs.amazon.com/sp-api/docs/orders-api-v0-reference#getorders)
        # the getOrders operation is a HTTP GET request with query parameters
        request_params = {
            "MarketplaceIds": marketplace_id,  # required parameter
            "CreatedAfter": (
                datetime.datetime.now() - datetime.timedelta(days=365)
            ).isoformat(),  # orders created since 365 days ago, the date needs to be in the ISO format
        }

        orders_response = requests.get(
            endpoint
            + "/orders/v0/orders"  # getOrders operation path (from https://developer-docs.amazon.com/sp-api/docs/orders-api-v0-reference#getorders)
            + "?"
            + urllib.parse.urlencode(request_params),  # encode query parameters to the URL
            headers={
                "x-amz-access-token": access_token,  # access token from LWA, every SP API request needs to have this header
            },
        )
        orders_response.raise_for_status()  # Check for HTTP errors

        orders_data = orders_response.json()
        
        # Log the entire response for debugging
        print("Orders data:", orders_data)

        if 'Orders' not in orders_data['payload'] or not orders_data['payload']['Orders']:
            return render_template('orders.html', orders={'payload': {'Orders': []}})  # No orders found, pass an empty dictionary

        # Pass the orders data to the template
        return render_template('orders.html', orders=orders_data)

    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}", 500
    except Exception as e:
        return f"An error occurred: {e}", 500

@app.route('/get-order/<orderId>', methods=['GET'])
def get_order(orderId):
    try:
        # Getting the LWA access token using the Seller Central App credentials.
        token_response = requests.post(
            "https://api.amazon.com/auth/o2/token",
            data={
                "grant_type": "refresh_token",
                "refresh_token": credentials["refresh_token"],
                "client_id": credentials["lwa_app_id"],
                "client_secret": credentials["lwa_client_secret"],
            },
        )
        token_response.raise_for_status()  # Check for HTTP errors
        access_token = token_response.json().get("access_token")
        if not access_token:
            return "Failed to retrieve access token", 500

        # North America SP API endpoint
        endpoint = "https://sellingpartnerapi-eu.amazon.com"

        # Get order details by orderId
        order_response = requests.get(
            f"{endpoint}/orders/v0/orders/{orderId}",  # getOrder operation path
            headers={
                "x-amz-access-token": access_token,  # access token from LWA
            },
        )
        order_response.raise_for_status()  # Check for HTTP errors
        order_data = order_response.json()

        # Get order items by orderId
        order_items_response = requests.get(
            f"{endpoint}/orders/v0/orders/{orderId}/orderItems",  # getOrderItems operation path
            headers={
                "x-amz-access-token": access_token,  # access token from LWA
            },
        )
        order_items_response.raise_for_status()  # Check for HTTP errors
        order_items_data = order_items_response.json()

        # Log the entire response for debugging
        print("Order data:", order_data)
        print("Order items data:", order_items_data)

        # Pass the order data and order items data to the template
        return render_template('order_detail.html', order=order_data, order_items=order_items_data)

    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}", 500
    except Exception as e:
        return f"An error occurred: {e}", 500

@app.route('/update-price', methods=['GET'])
def update_price_form():
    return render_template('update_price.html')

@app.route('/update-product-price', methods=['POST'])
def update_product_price():
    try:
        # Retrieve access token
        token_response = requests.post(
            "https://api.amazon.com/auth/o2/token",
            data={
                "grant_type": "refresh_token",
                "refresh_token": credentials["refresh_token"],
                "client_id": credentials["lwa_app_id"],
                "client_secret": credentials["lwa_client_secret"],
            },
        )
        token_response.raise_for_status()  # Check for HTTP errors
        access_token = token_response.json().get("access_token")
        if not access_token:
            return "Failed to retrieve access token", 500

        # Product price update endpoint
        endpoint = "https://sellingpartnerapi-eu.amazon.com/listings/2021-08-01/items"
        
        # Retrieve product details from request data
        seller_id = "AKKANLKIMV9TP"  # Replace with your actual seller ID
        sku = urllib.parse.quote(request.form.get("sku"), safe='')  # URL encode SKU
        new_price = request.form.get("price")
        marketplace_ids = "A21TJRUUN4KGV"  # Replace with the actual marketplace ID

        if not sku or not new_price:
            return "SKU and new price are required", 400

        # Request body for updating the price
        update_data = {
            "productType": "PRODUCT",
            "patches": [
                {
                    "op": "replace",
                    "path": "/attributes/price",
                    "value": [
                        {
                            "value": new_price,
                            "currency": "INR"
                        }
                    ]
                }
            ]
        }

        # Updating product price
        update_response = requests.put(
            f"{endpoint}/{seller_id}/{sku}",
            params={
                "marketplaceIds": marketplace_ids,
                "mode": "STANDARD"  # Use appropriate mode if needed
            },
            json=update_data,
            headers={
                "x-amz-access-token": access_token,
                "Content-Type": "application/json"
            },
        )
        update_response.raise_for_status()

        # Pass the response to the template
        response_data = update_response.json()
        return render_template('update_price.html', response=response_data)

    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}", 500
    except Exception as e:
        return f"An error occurred: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)
