
from PIL import Image
import numpy as np
import os
from cv_toolkit.image import ImageProcessing

# Create a dummy image for testing
def create_dummy_image(filepath="dummy_image.png"):
    img = Image.new('RGB', (100, 100), color = 'red')
    img.save(filepath)
    print(f"Created dummy image: {filepath}")
    return filepath

# Test the ImageProcessing class
def test_image_processing():
    dummy_image_path = create_dummy_image()
    output_image_path_grayscale = "dummy_image_grayscale.png"
    output_image_path_resized = "dummy_image_resized.png"

    # Test loading and basic operations
    img_proc = ImageProcessing(dummy_image_path)
    if img_proc.image:
        # Convert to grayscale
        img_proc.convert_to_grayscale()
        img_proc.save_image(output_image_path_grayscale)

        # Resize
        img_proc.resize(50, 50)
        img_proc.save_image(output_image_path_resized)

        print("Image processing tests completed. Check generated images.")
    else:
        print("Failed to load image for processing tests.")

    # Clean up dummy images
    if os.path.exists(dummy_image_path):
        os.remove(dummy_image_path)
        print(f"Removed dummy image: {dummy_image_path}")
    if os.path.exists(output_image_path_grayscale):
        os.remove(output_image_path_grayscale)
        print(f"Removed output image: {output_image_path_grayscale}")
    if os.path.exists(output_image_path_resized):
        os.remove(output_image_path_resized)
        print(f"Removed output image: {output_image_path_resized}")

if __name__ == "__main__":
    test_image_processing()
