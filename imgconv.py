import os
from PIL import Image

# Define a global folder for storing old image files
old_images_folder = "old_pic"

def convert_images_to_webp(input_folder, output_folder=None):
    # If output folder is not specified, set it to the same as the input folder
    if output_folder is None:
        output_folder = input_folder

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Create the "old_pic" folder if it doesn't exist
    if not os.path.exists(old_images_folder):
        os.makedirs(old_images_folder)

    for filename in os.listdir(input_folder):
        # Check if the file is an image (PNG/JPG/JPEG)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.webp')

            # Open the image file
            image = Image.open(input_path)
            # Convert the image to WebP format
            image.save(output_path, 'webp')

            # Calculate size differences
            input_size = os.path.getsize(input_path)
            output_size = os.path.getsize(output_path)
            size_difference = output_size - input_size
            percentage_difference = (size_difference / input_size) * 100

            print(f"Converted {filename} to WebP. Size difference: {size_difference} bytes ({percentage_difference:.2f}%).")

            # Move the original image file to the "old_pic" folder
            old_image_path = os.path.join(old_images_folder, filename)
            os.rename(input_path, old_image_path)
            print(f"Moved {filename} to 'old_pic' folder.")

# Prompt the user for input folder
input_folder = input("Enter the path to the input folder: ")
# Prompt the user for output folder (or leave it blank to use the same as input folder)
output_folder = input("Enter the path to the output folder (or leave it blank to use the same as input folder): ")

if not output_folder.strip():
    output_folder = None

convert_images_to_webp(input_folder, output_folder)
