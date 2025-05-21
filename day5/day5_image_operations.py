import cv2
import os

# Setup paths
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'sample.jpg')
output_dir = os.path.join(script_dir, 'output')
os.makedirs(output_dir, exist_ok=True)

# Load image
image = cv2.imread(image_path)
if image is None:
    print(f"Error: Could not load image at {image_path}")
    exit(1)

# Convert to grayscale and back to BGR to allow colored shapes
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

# Get image dimensions
height, width = gray_bgr.shape[:2]

# Draw shapes for design
cv2.rectangle(gray_bgr, (30, 30), (width - 30, height - 30), (0, 255, 255), 4)  # Border rectangle
cv2.circle(gray_bgr, (width // 2, height // 3), 60, (100, 100, 255), -1)        # Filled circle in upper third

# Add centered text
text = "JC ESCARIO"
font = cv2.FONT_HERSHEY_DUPLEX
font_scale = 2
thickness = 3
(text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness)
text_x = (width - text_width) // 2
text_y = (height + text_height) // 2
cv2.putText(gray_bgr, text, (text_x, text_y), font, font_scale, (255, 255, 255), thickness)

# Resize for preview
resized = cv2.resize(gray_bgr, (width // 2, height // 2), interpolation=cv2.INTER_AREA)

# Save outputs
cv2.imwrite(os.path.join(output_dir, 'gray.jpg'), gray)
cv2.imwrite(os.path.join(output_dir, 'gray_shapes_text.jpg'), gray_bgr)
cv2.imwrite(os.path.join(output_dir, 'gray_resized.jpg'), resized)

# Display
cv2.imshow('Styled JC ESCARIO Image', gray_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
