'''ensure you have the Pillow library installed. If not, install it using below command'''
pip install pillow
from PIL import Image

def convert_image(input_path, output_path, output_format):
    try:
        # Open the image file
        img = Image.open(input_path)
        # save image
        img.save(output_path, format=output_format)
        print(f"Image converted successfully and saved as {output_path}")
    except Exception as e:
        print(f"Error: {e}")
convert_image("pic.jpg", "pht.png", "PNG")
