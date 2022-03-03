#code by Kanento

#Import urllib request
import urllib.request

#create input
enter = str(input("Enter the link for the download : "))

#script for the downloading
if enter == str(enter):
  rest = urllib.request.urlretrieve(str(enter), "video_dll.mp4")  
  print("Download is finish.")
else:
  print("Download ERROR, please repeat the downloading...")


#Code by Kanento