import cv2
import face_recognition

# opening the templates/images then converting it to a color that opencv supports
cam = cv2.VideoCapture(0)
c_hat = cv2.imread("template2/christmashat2.png", -1)
hoho = cv2.imread("template2/hohoho2.png", -1)
c_hat = cv2.cvtColor(c_hat, cv2.COLOR_BGR2BGRA)
hoho = cv2.cvtColor(hoho, cv2.COLOR_BGR2BGRA)

while(cam.isOpened()):

	#initializing the webcam
    ret, frame = cam.read()
    fh,fw,fc = frame.shape 
    face_locations = face_recognition.face_locations(frame)
    face_landmarks_list = face_recognition.face_landmarks(frame)
    im = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
   
    #print(face_landmarks_list)
    for elements in face_landmarks_list:

		#resizing the templates/images
        hoho = cv2.resize(hoho, (350, 350))
        c_hat = cv2.resize(c_hat, (300, 420))
 
		#adjusting the position of the images when the webcam is opened and detects the landmarks (left eye is only used for it to be organized or easy to do trial and error)
        height_offset1 = elements['left_eye'][2][1] - 155
        width_offset1 = elements['left_eye'][0][0] + 80
        height_offset2 = elements['left_eye'][2][1] - 270
        width_offset2 = elements['left_eye'][0][0] - 97

		#this is where the making of the image happens, when the frame of the image/template exceeds the frame, it moves to the other part of the frame
        hh,hw,hc = hoho.shape
        for i in range(0, hh):
            if height_offset1 + i >= fh:
                break
            for j in range(0, hw):
                if hoho[i,j][3] != 0:
                    if width_offset1 + j >= fw:
                        break
                    else:
                        im[height_offset1 + i,width_offset1 + j] = hoho[i,j]
        ch,cw,cc = c_hat.shape
        for i in range(0,ch):
            if height_offset2 + i >= fh:
                break
            for j in range(0, cw):
                if c_hat[i,j][3] != 0:
                    if width_offset2 + j >= fw:
                        break
                    else:
                        im[height_offset2 + i,width_offset2 + j] = c_hat[i,j]

    
    cv2.imshow("Diyyinah's Snapchat", im)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
