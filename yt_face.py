import cv2
import os
import time
from pytube import YouTube

# Download the video using PyTube
yt = YouTube('https://www.youtube.com/watch?v=rMPkUuMq024') #YouTube video URL
yt.streams.filter(file_extension='mp4').first().download()

# Open the video using OpenCV and extract the frames
vidcap = cv2.VideoCapture('./SEEN - A 1 Minute Short Film.mp4') #Name of youtube video this can be found in YOutube
success, image = vidcap.read()
count = 0
success = True
while success:
    success, image = vidcap.read()
    # print(count, image.shape)
    # Save the extracted frames as JPEG images
    try:
        cv2.imwrite("./frames/frame%d.jpg" % count, image) #path to save frame
    except:
        pass
    count += 1

# Use OpenCV to detect faces in the images and crop them
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
for file_name in os.listdir('./frames/'):
    if file_name.endswith('.jpg'):
        img = cv2.imread('./frames/'+file_name)
        # print(file_name)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
        for (x,y,w,h) in faces:
            crop_img = img[y:y+h, x:x+w]
            cv2.imwrite("./faces/face%d.jpg" % count, crop_img) #path to save faces in the video
            count += 1
