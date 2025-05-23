import cv2

# Load the image
image = cv2.imread('sample.jpg')

# Check if loaded correctly
if image is None:
    print("Error: Image not found.")
else:
    # 1. Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('output/gray_sample.jpg', gray)

    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    cv2.imwrite('output/blurred_sample.jpg', blurred)

    edges = cv2.Canny(blurred, 50, 150)
    cv2.imwrite('output/edges_sample.jpg', edges)

    _, thresholded = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite('output/thresholded_sample.jpg', thresholded)

    cv2.imshow("Original", image)
    cv2.imshow("Gray", gray)
    cv2.imshow("Blurred", blurred)
    cv2.imshow("Edges", edges)
    cv2.imshow("Thresholded", thresholded)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
