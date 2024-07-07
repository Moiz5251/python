import pandas as pd
import os
import requests

def download_images_from_excel(excel_file, download_path):
    # Read the Excel file
    df = pd.read_excel(excel_file)
    
    # Create directory if it doesn't exist
    os.makedirs(download_path, exist_ok=True)
    
    # Download images from the URLs in the Excel file
    for index, row in df.iterrows():
        # Get the image URLs from the current row
        image_urls = str(row['Image URL']).split(',')
        
        # Download each image separately
        for image_url in image_urls:
            image_url = image_url.strip()  # Remove leading/trailing whitespace
            if image_url:
                image_name = os.path.basename(image_url)
                image_path = os.path.join(download_path, image_name)
                print(f"Downloading image: {image_url}")
                try:
                    response = requests.get(image_url)
                    if response.status_code == 200:
                        with open(image_path, 'wb') as file:
                            file.write(response.content)
                        print(f"Image downloaded: {image_path}")
                    else:
                        print(f"Failed to download image: {image_url}, Status code: {response.status_code}")
                except Exception as e:
                    print(f"Error downloading image: {image_url}, Error: {str(e)}")

# Example usage
excel_file = 'images.xlsx'  # Replace with the path to your Excel file
download_path = 'E:\python\product-data\images'     # Specify the directory where you want to save the images

# Call function to download images from the Excel file
download_images_from_excel(excel_file, download_path)
