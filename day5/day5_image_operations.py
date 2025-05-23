import cv2

# Load the image
image = cv2.imread('sample.jpg')

# Check if the image was loaded properly
if image is None:
    print("Error: Image not found or path is incorrect.")
else:
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resize the grayscale image
    resized_gray = cv2.resize(gray_image, (500, 500))

    # Convert grayscale back to BGR so we can draw in color
    image_with_drawing = cv2.cvtColor(resized_gray, cv2.COLOR_GRAY2BGR)

    # Draw a blue rectangle
    cv2.rectangle(image_with_drawing, (50, 50), (450, 150), (255, 0, 0), 2)

    # Draw a green circle at center
    cv2.circle(image_with_drawing, (250, 300), 50, (0, 255, 0), 3)

    # Write white text
    cv2.putText(image_with_drawing, 'Day 5: JC ESCARIO', (90, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Display all images
    cv2.imshow('Original Image', image)
    cv2.imshow('Grayscale + Drawings', image_with_drawing)

    # Save the final image
    cv2.imwrite('output/day5_gray_with_shapes.jpg', image_with_drawing)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
