
import sys
import cv2
import numpy as np


def detect(cap):

    while (cap.isOpened()):

        ret, frame = cap.read()
        rows = frame.shape[0]

        if (ret == True):

            font = cv2.FONT_HERSHEY_SIMPLEX
            # since each frame read as image
            img = frame
            cimg = img
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            # color range
            lower_red1 = np.array([0,100,180])
            upper_red1 = np.array([10,255,255])
            lower_red2 = np.array([160,100,180])
            upper_red2 = np.array([180,255,255])

            lower_green = np.array([40,80,50])
            upper_green = np.array([90,255,255])
        
            lower_yellow = np.array([15,150,180])
            upper_yellow = np.array([35,255,255])

            mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
            mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
            maskg = cv2.inRange(hsv, lower_green, upper_green)
            masky = cv2.inRange(hsv, lower_yellow, upper_yellow)
            maskr = cv2.add(mask1, mask2)

            # hough circle detect
            r_circles = cv2.HoughCircles(maskr, cv2.HOUGH_GRADIENT, 1, rows/8,
                                       param1=50, param2=10, minRadius=0, maxRadius=30)

            g_circles = cv2.HoughCircles(maskg, cv2.HOUGH_GRADIENT, 1, rows/8,
                                         param1=50, param2=10, minRadius=0, maxRadius=30)

            y_circles = cv2.HoughCircles(masky, cv2.HOUGH_GRADIENT, 1, 30,
                                         param1=50, param2=5, minRadius=0, maxRadius=30)

            if r_circles is not None:
                r_circles = np.uint16(np.around(r_circles))
                for i in r_circles[0, :]:
                    cv2.circle(cimg, (i[0], i[1]), i[2]+10, (0, 255, 0), 2)
                    cv2.circle(maskr, (i[0], i[1]), i[2]+30, (255, 255, 255), 2)
                    cv2.putText(cimg,'RED',(i[0], i[1]), font, 1,(255,0,0),2,cv2.LINE_AA)


            if g_circles is not None:
                g_circles = np.uint16(np.around(g_circles))
                for i in g_circles[0, :]:
                    cv2.circle(cimg, (i[0], i[1]), i[2]+20, (0, 255, 0), 2)
                    cv2.circle(maskg, (i[0], i[1]), i[2]+50, (255, 255, 255), 2)
                    cv2.putText(cimg,'GREEN',(i[0], i[1]), font, 1,(255,0,0),2,cv2.LINE_AA)


            if y_circles is not None:
                y_circles = np.uint16(np.around(y_circles))
                for i in y_circles[0, :]:
                    cv2.circle(cimg, (i[0], i[1]), i[2]+10, (0, 255, 0), 2)
                    cv2.circle(masky, (i[0], i[1]), i[2]+30, (255, 255, 255), 2)
                    cv2.putText(cimg,'YELLOW',(i[0], i[1]), font, 1,(255,0,0),2,cv2.LINE_AA)

            

            cv2.imshow('detected results', cimg)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            cv2.destroyAllWindows()


        else:
            break



if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: python file.py <path of your video file>')
        #In this case,
        #python traffic.py ../videos/NVR_01.mp4
        exit(-1)

    video = sys.argv[1]
    cap = cv2.VideoCapture(video)

    if (cap.isOpened() == False):
        print('Error in opening video file or video')

    detect(cap)
