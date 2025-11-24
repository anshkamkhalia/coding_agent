
from PIL import Image
import numpy as np
import os
from cv_toolkit.image import ImageProcessing
from cv_toolkit.drawing import ImageDrawing

# Create a dummy image for testing
def create_dummy_image(filepath="dummy_drawing_image.png"):
    img = Image.new('RGB', (200, 200), color = 'white')
    img.save(filepath)
    print(f"Created dummy image: {filepath}")
    return filepath

# Test the ImageDrawing class
def test_image_drawing():
    dummy_image_path = create_dummy_image()
    output_image_path = "dummy_image_drawn.png"

    img_proc = ImageProcessing(dummy_image_path)
    if img_proc.image:
        img_drawing = ImageDrawing(img_proc)

        # Draw a line
        img_drawing.draw_line((10, 10), (100, 100), (255, 0, 0), thickness=3) # Red line

        # Draw an outlined rectangle
        img_drawing.draw_rectangle((20, 120), (80, 180), (0, 255, 0), thickness=5) # Green rectangle

        # Draw a filled rectangle
        img_drawing.draw_rectangle((120, 20), (180, 80), (0, 0, 255), fill=True) # Blue filled rectangle

        # Draw an outlined circle
        img_drawing.draw_circle((150, 150), 30, (255, 255, 0), thickness=2) # Yellow circle

        # Draw a filled circle
        img_drawing.draw_circle((50, 150), 20, (255, 0, 255), fill=True) # Magenta filled circle

        img_proc.save_image(output_image_path)
        print("Image drawing tests completed. Check generated image.")
    else:
        print("Failed to load image for drawing tests.")

    # Clean up dummy images
    if os.path.exists(dummy_image_path):
        os.remove(dummy_image_path)
        print(f"Removed dummy image: {dummy_image_path}")
    if os.path.exists(output_image_path):
        os.remove(output_image_path)
        print(f"Removed output image: {output_image_path}")

if __name__ == "__main__":
    test_image_drawing()
