import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # setting threshole of gray scale image
    _,threshold = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
    #use findContour functuon 
    contours,_ = cv.findContours(threshold,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    i=0
	
    for contour in contours:
		if i==0:
			i=1
			continue

			#use approximate for shape
		approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)

			#drawContour funtion
		cv.drawContours(frame, [contour], 0, (0, 0, 255), 5)

			#find center point of shape 
		M = cv.moments(contour)

		if M['m00'] != 0.0:
			x = int(M['m10']/M['m00'])
			y = int(M['m01']/M['m00'])
			# putting shape name at center of each shape
		if len(approx) == 3:
			cv.putText(frame, 'Triangle', (x, y),cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

		elif len(approx) == 4:
			cv.putText(frame, 'Quadrilateral', (x, y),cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

		elif len(approx) == 5:
			cv.putText(frame, 'Pentagon', (x, y),cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

		elif len(approx) == 6:
			cv.putText(frame, 'Hexagon', (x, y),cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

		else:
			cv.putText(frame, 'circle', (x, y),cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
		
		# Display the resulting frame
		cv.imshow('frame', gray)
		if cv.waitKey(1) == ord('q'):
				break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
