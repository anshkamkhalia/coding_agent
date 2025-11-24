
from PIL import Image
import numpy as np
import os
from cv_toolkit.image import ImageProcessing
from cv_toolkit.filters import ImageFilters

# Create a dummy image for testing
def create_dummy_image(filepath="dummy_filter_image.png"):
    img = Image.new('RGB', (100, 100), color = 'blue')
    img.save(filepath)
    print(f"Created dummy image: {filepath}")
    return filepath

# Test the ImageFilters class
def test_image_filters():
    dummy_image_path = create_dummy_image()
    output_paths = []

    # Test Gaussian Blur
    img_proc_blur = ImageProcessing(dummy_image_path)
    if img_proc_blur.image:
        img_filters_blur = ImageFilters(img_proc_blur)
        img_filters_blur.apply_gaussian_blur(kernel_size=5, sigma=1.5)
        output_path_blur = "dummy_image_blurred.png"
        img_proc_blur.save_image(output_path_blur)
        output_paths.append(output_path_blur)
    else:
        print("Failed to load image for blur test.")

    # Test Edge Detection
    img_proc_edge = ImageProcessing(dummy_image_path)
    if img_proc_edge.image:
        img_filters_edge = ImageFilters(img_proc_edge)
        img_filters_edge.apply_edge_detection(threshold=70)
        output_path_edge = "dummy_image_edges.png"
        img_proc_edge.save_image(output_path_edge)
        output_paths.append(output_path_edge)
    else:
        print("Failed to load image for edge detection test.")

    # Test Sharpen
    img_proc_sharpen = ImageProcessing(dummy_image_path)
    if img_proc_sharpen.image:
        img_filters_sharpen = ImageFilters(img_proc_sharpen)
        img_filters_sharpen.apply_sharpen()
        output_path_sharpen = "dummy_image_sharpened.png"
        img_proc_sharpen.save_image(output_path_sharpen)
        output_paths.append(output_path_sharpen)
    else:
        print("Failed to load image for sharpen test.")

    # Test Sepia
    img_proc_sepia = ImageProcessing(dummy_image_path)
    if img_proc_sepia.image:
        img_filters_sepia = ImageFilters(img_proc_sepia)
        img_filters_sepia.apply_sepia()
        output_path_sepia = "dummy_image_sepia.png"
        img_proc_sepia.save_image(output_path_sepia)
        output_paths.append(output_path_sepia)
    else:
        print("Failed to load image for sepia test.")

    print("Image filter tests completed. Check generated images.")

    # Clean up dummy images
    if os.path.exists(dummy_image_path):
        os.remove(dummy_image_path)
        print(f"Removed dummy image: {dummy_image_path}")
    for path in output_paths:
        if os.path.exists(path):
            os.remove(path)
            print(f"Removed output image: {path}")

if __name__ == "__main__":
    test_image_filters()
