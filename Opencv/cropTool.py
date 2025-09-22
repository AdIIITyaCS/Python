from PIL import Image
import cv2
import numpy as np
import os

# Define the image path
image_path = 'Multi.jpg'

try:
    # Load the image
    print("Loading image...")
    image = Image.open(image_path)

    # Convert to OpenCV format
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Resize for easier processing if necessary
    height, width = image_cv.shape[:2]
    aspect_ratio = width / height
    new_height = 800
    new_width = int(aspect_ratio * new_height)
    image_resized = cv2.resize(image_cv, (new_width, new_height))

    # Convert the image to grayscale
    gray = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)

    # Use adaptive thresholding to separate the signatures from the background
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 7)

    # Dilate the image to ensure individual letters within each signature are connected
    kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(thresh, kernel, iterations=1)

    # Find contours of the signatures
    print("Finding contours...")
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours by area, assuming larger contours are signatures
    min_area = 500  # Adjust this value based on the image for accurate contour filtering
    signature_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

    # Sort contours left to right, then top to bottom for proper ordering
    signature_contours = sorted(signature_contours, key=lambda cnt: (cv2.boundingRect(cnt)[1], cv2.boundingRect(cnt)[0]))

    # Initialize list to store each cropped signature image
    signature_images = []

    # Create output directory for cropped signatures if it doesn't exist
    output_dir = 'cropped'
    os.makedirs(output_dir, exist_ok=True)

    # Loop over contours and extract each signature
    print(f"Found {len(signature_contours)} potential signatures.")
    for i, contour in enumerate(signature_contours, start=1):
        x, y, w, h = cv2.boundingRect(contour)

        # Add padding to each bounding box for a cleaner crop (optional)
        padding = 10
        x_start = max(0, x - padding)
        y_start = max(0, y - padding)
        x_end = min(new_width, x + w + padding)
        y_end = min(new_height, y + h + padding)

        # Crop the signature
        signature_img = image_resized[y_start:y_end, x_start:x_end]
        signature_images.append(signature_img)

        # Save each signature image to output directory
        output_path = os.path.join(output_dir, f'signature_{i}.png')
        cv2.imwrite(output_path, signature_img)
        print(f"Saved signature {i} to {output_path}")

    print("All signatures extracted and saved successfully.")

except FileNotFoundError:
    print(f"File not found: {image_path}. Please check the file path and try again.")
except Exception as e:
    print("An error occurred:", e)