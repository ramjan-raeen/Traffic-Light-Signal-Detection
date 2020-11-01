# Traffic-Light-Detection
Traffic Light Detection Using Python and OpenCV 
***
Traffic light detection(TLD), it has simple python script to detect traffic light, red? green? or yellow ones.

I'm using
macOS High Sierra, version 10.13.6

installed [Anaconda](https://www.anaconda.com/products/individual#macos) and created [env](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands) for python 3

installed [opencv](https://anaconda.org/conda-forge/opencv) version '3.1.0'

***
I took reference from [opencv](https://docs.opencv.org/3.4/d4/d70/tutorial_hough_circle.html) official doc.

[Draw circle](https://docs.opencv.org/3.4/d4/d70/tutorial_hough_circle.html)

[capture video through webcamera or file](https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html) and [write video](https://www.learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/)
[HoughCircles](https://docs.opencv.org/3.4/dd/d1a/group__imgproc__feature.html#ga47849c3be0d0406ad3ca45db65a25d2d)

## Files
[code](https://github.com/ramjan-raeen/Traffic-Light-Signal-Detection/blob/main/src/traffic.py)

[video](https://drive.google.com/drive/folders/1OP1c5vB1nIY9cQvD9ATJT2h836W-1_Hd) download from my google drive

## How to run 
Download code from my [github](https://github.com/ramjan-raeen/Traffic-Light-Signal-Detection). unzip downloaded file

Download videos from my [google drive](https://drive.google.com/drive/folders/1OP1c5vB1nIY9cQvD9ATJT2h836W-1_Hd) and put into videos folder.

Navigate to src directory and run below command

`python traffic.py ../videos/NVR_01.mp4` or `python traffic.py ../videos/NVR_02.mp4` for video file 01 and 02 respectively. 
