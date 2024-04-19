import cv2
import cvlearn.HandTrackingModule as htm
import cvlearn.FingerCounter as fc
import serial


ser = serial.Serial('COM15', 9600)  # Replace 'COMX' with your Arduino's COM port

cap = cv2.VideoCapture(0)
det = htm.handDetector()
counter = fc.FingerCounter()


num_fingers = 0

while True:

    ret, frame = cap.read()
    det.findHands(frame)
    lmlist, bbox = det.findPosition(frame)

    if lmlist != 0:
        num_fingers = counter.countFingers(lmlist)


        counter.drawCountedFingers(frame, lmlist, bbox)


        print("Number of fingers:", num_fingers)


        if num_fingers == 1:
            ser.write(b'a')
        elif num_fingers == 2:
            ser.write(b'b')
        elif num_fingers == 3:
            ser.write(b'c')
        elif num_fingers == 4:
            ser.write(b'd')


    if not ret:
        print("Error: Could not capture frame.")
        break


    cv2.imshow('Live Feed', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()