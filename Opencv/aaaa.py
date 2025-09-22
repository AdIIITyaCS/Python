# import cv2
# import numpy as np

# # Load an image from file
# image_path = "Resources\Photos\Myphoto.jpg"  # Replace with your image path
# image = cv2.imread(image_path)  # Loads the image in BGR format

# # Convert the image to RGB (Optional, OpenCV loads as BGR by default)
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# # Convert the image to a NumPy array
# image_array = np.array(image_rgb)

# print("Image shape:", image_array.shape)  # Example output: (height, width, channels)
# print("Image array:", image_array)
# import numpy as np

# # Create a white image (RGB format, 8-bit, 3 color channels)
# height, width = 100, 100  # Example dimensions
# white_image_rgb = np.ones((height, width, 3), dtype=np.uint8) * 255
# print("RGB White Image Array:")
# print(white_image_rgb)

# # Create a white image (Grayscale format, 8-bit, 1 channel)
# white_image_gray = np.ones((height, width), dtype=np.uint8) * 255
# print("\nGrayscale White Image Array:")
# print(white_image_gray)

# # Normalized white image
# white_image_normalized = np.ones((height, width, 3), dtype=np.float32)
# print("\nNormalized White Image Array:")
# print(white_image_normalized)

import numpy as np

# Define two 2D arrays
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

# Stack along axis=0
result = np.concatenate((array1, array2), axis=0)

print("Array 1:")
print(array1)

print("\nArray 2:")
print(array2)

print("\nResult of Concatenation along axis=0:")
print(result)
