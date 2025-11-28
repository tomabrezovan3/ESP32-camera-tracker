import cv2
import numpy as np

def main():
    # Open webcam (0 = default)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Could not open webcam")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert to grayscale (simple for now)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Show window
        cv2.imshow("Camera Feed", gray)

        # Quit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

