import cv2

# Load image
image = cv2.imread('sample.jpg')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display grayscale image
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the grayscale image
cv2.imwrite('grayscale_sample.jpg', gray_image)
