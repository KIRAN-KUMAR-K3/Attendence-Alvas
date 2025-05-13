import cv2

# Open default camera (index 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly, ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Display the resulting frame
    cv2.imshow('Camera Stream', frame)

    # Exit on 'q' key
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
