import cv2
cap = cv2.VideoCapture("rtsp://user:123456abcd@10.1.42.51/h264/ch1/main/av_stream")
ret, frame = cap.read()
while ret:
    ret, frame = cap.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()