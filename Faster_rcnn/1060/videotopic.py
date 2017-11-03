#coding=utf-8
import cv2

if __name__ == '__main__':
    #获得视频的格式
    videoCapture = cv2.VideoCapture('test.mp4')
 
    #获得码率及尺寸
    fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)
    size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)), 
            int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
     
    #指定写视频的格式, I420-avi, MJPG-mp4
    videoWriter = cv2.VideoWriter('oto_other.mp4', cv2.cv.CV_FOURCC('M', 'J', 'P', 'G'), fps, size)
     
    #读帧
    success, frame = videoCapture.read()
    count = 1 
    while success :
        cv2.imshow('video', frame) #显示
        cv2.waitKey(1000/int(fps)) #延迟
        cv2.imwrite('img/'+str(count) + '.jpg',frame) #存储为图像
        count += 1
        #videoWriter.write(frame) #写视频帧
        success, frame = videoCapture.read() #获取下一帧




