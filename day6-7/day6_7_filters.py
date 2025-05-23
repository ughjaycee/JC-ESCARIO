import cv2
import os

if not os.path.exists('output'):
    os.makedirs('output')
image = cv2.imread('sample.jpg')

if image is None:
    print("Error: Could not load image.")
    exit()
    
image = cv2.resize(image, (300, 300))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
edges = cv2.Canny(blurred, 50, 150)
_, thresholded = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imwrite('output/gray_sample.jpg', gray)
cv2.imwrite('output/blurred_sample.jpg', blurred)
cv2.imwrite('output/edges_sample.jpg', edges)
cv2.imwrite('output/thresholded_sample.jpg', thresholded)

gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
blurred_bgr = cv2.cvtColor(blurred, cv2.COLOR_GRAY2BGR)
edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
thresholded_bgr = cv2.cvtColor(thresholded, cv2.COLOR_GRAY2BGR)

font = cv2.FONT_HERSHEY_SIMPLEX
color = (0, 255, 0)
thickness = 1

cv2.putText(gray_bgr, 'Grayscale', (10, 20), font, 0.6, color, thickness)
cv2.putText(blurred_bgr, 'Blurred', (10, 20), font, 0.6, color, thickness)
cv2.putText(edges_bgr, 'Edges', (10, 20), font, 0.6, color, thickness)
cv2.putText(thresholded_bgr, 'Threshold', (10, 20), font, 0.6, color, thickness)

top_row = cv2.hconcat([gray_bgr, blurred_bgr])
bottom_row = cv2.hconcat([edges_bgr, thresholded_bgr])
combined = cv2.vconcat([top_row, bottom_row])

cv2.imwrite('output/combined_processed.jpg', combined)

cv2.imshow("Original Image", image)
cv2.imshow("Processed Outputs", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()
