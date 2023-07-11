import os
from PIL import Image

def convert_images_to_webp(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        # Check if the file is an image (PNG/JPG)
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

# Prompt the user for input and output folder paths
input_folder = input("Enter the path to the input folder: ")
output_folder = input("Enter the path to the output folder: ")

convert_images_to_webp(input_folder, output_folder)






