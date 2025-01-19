import cv2
import numpy as np

def load_image(image_path):
    """Loads the image from the given path."""
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image at {image_path} not found.")
    return image

def display_image(window_name, image):
    """Displays an image in a window."""
    cv2.imshow(window_name, image)

def convert_to_grayscale(image):
    """Converts an image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def detect_edges(gray_image):
    """Detects edges using Canny Edge Detection."""
    return cv2.Canny(gray_image, 50, 150)

def find_and_draw_contours(image, edges):
    """Finds contours in the edges and draws them on the image."""
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour_image = image.copy()
    cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)
    return contours, contour_image

def calculate_areas(contours):
    """Calculates and returns the area of each contour."""
    areas = [cv2.contourArea(contour) for contour in contours]
    for i, area in enumerate(areas):
        print(f"Contour {i}: Area = {area:.2f} square pixels")
    return areas

def save_image(output_path, image):
    """Saves the processed image to a file."""
    cv2.imwrite(output_path, image)

def main():
    """Main function to execute the blueprint analyzer."""
    image_path = input("Enter the path to the blueprint image: ")
    output_path = "outlined_blueprint.png"

    try:
        # Step 1: Load the image
        image = load_image(image_path)
        display_image("Original Blueprint", image)

        # Step 2: Convert to grayscale
        gray_image = convert_to_grayscale(image)
        display_image("Grayscale Blueprint", gray_image)

        # Step 3: Detect edges
        edges = detect_edges(gray_image)
        display_image("Edges", edges)

        # Step 4: Find and draw contours
        contours, contour_image = find_and_draw_contours(image, edges)
        display_image("Outlined Blueprint", contour_image)

        # Step 5: Calculate areas
        calculate_areas(contours)

        # Step 6: Save the outlined blueprint
        save_image(output_path, contour_image)
        print(f"Processed image saved as {output_path}")

        # Wait for user to close the windows
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
