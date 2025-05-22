# grayscale_image.py

import cv2

# Load the image
image = cv2.imread("sample.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display both images
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)

# Wait for a key press and close
cv2.waitKey(0)
cv2.destroyAllWindows()
