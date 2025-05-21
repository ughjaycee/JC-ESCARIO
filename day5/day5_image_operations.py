import cv2
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'sample.jpg')
output_dir = os.path.join(script_dir, 'output')

os.makedirs(output_dir, exist_ok=True)

image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not load image at {image_path}")
    exit(1)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

cv2.rectangle(gray_bgr, (50, 50), (200, 200), (255, 0, 0), 2)
cv2.circle(gray_bgr, (300, 300), 75, (0, 255, 0), 3)
cv2.putText(gray_bgr, 'OpenCV Demo', (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

width = gray_bgr.shape[1] // 2
height = gray_bgr.shape[0] // 2
dim = (width, height)
resized = cv2.resize(gray_bgr, dim, interpolation=cv2.INTER_AREA)

cv2.imwrite(os.path.join(output_dir, 'gray.jpg'), gray)
cv2.imwrite(os.path.join(output_dir, 'gray_shapes_text.jpg'), gray_bgr)
cv2.imwrite(os.path.join(output_dir, 'gray_resized.jpg'), resized)

cv2.imshow('Grayscale with Shapes and Text', gray_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
