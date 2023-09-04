import numpy as np
import cv2 



camera = cv2.VideoCapture(0)


def mse(img1, img2):
   h, w, d = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse

def ta_bilde():
  if not camera.isOpened():
    print("kamera kunne ikke åpnes din hore dø")
    return False
  
  ret, frame = camera.read()
  
  if not ret:
  
    print("kunne ikke ta bilde, kanskje du er for stygg?")
    return False

  #cv2.imshow("Tatt bilde", frame)

 
  #cv2.imwrite("Bilde.jpg", frame)
  return frame

imgCount = 0
rms = 101
img1 = ta_bilde()
while rms > 3 and imgCount < 25: 
    img2 = ta_bilde() 
    rms = mse(img1, img2)
    print(rms)
    img1 = img2
    imgCount+=1
print("I fokus", rms) 
camera.release()