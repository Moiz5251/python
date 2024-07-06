import requests
import os

# Create a directory to save images
os.makedirs('images', exist_ok=True)

# Read image URLs from a text file
with open('image_urls.txt', 'r') as file:
    urls = file.readlines()

# Function to download an image
def download_image(url, folder='images'):
    try:
        response = requests.get(url.strip())
        response.raise_for_status()
        # Extract image name from URL
        image_name = os.path.basename(url.strip())
        # Save image to the specified folder
        with open(os.path.join(folder, image_name), 'wb') as img_file:
            img_file.write(response.content)
        print(f'Successfully downloaded: {image_name}')
    except requests.exceptions.RequestException as e:
        print(f'Failed to download {url.strip()}: {e}')

# Download 80 images
for i, url in enumerate(urls):
    if i >= 80:
        break
    download_image(url)

print('Download complete.')
