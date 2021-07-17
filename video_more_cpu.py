 #使用线程化的方式提高FPS（每秒帧数 Frams per second）
# python fps_demo.py
# python fps_deom.py -d 1

# 导入必要的包
from __future__ import print_function
from imutils.video import WebcamVideoStream
from imutils.video import FPS
import argparse
import imutils
import cv2
import time

# 构建命令行参数
# --num-frames 获取FPS估算值而要循环播放的帧数
# --display 指标变量，指定是否应用cv2.imshow()显示帧
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=100,
                help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=-1,
                help="Whether or not frames should be displayed")
args = vars(ap.parse_args())

# 获取视频流指针，初始化FPS计数器
print("[INFO] sampling frames from webcam...")
stream = cv2.VideoCapture("testvideo.mp4")
fps = FPS().start()
"""
# 循环遍历一些帧
fps_count = 0.0
while  (True):
    t1 = time.time()
    # 从流中获取帧，resize 宽度为400
    (grabbed, frame) = stream.read()
    frame = imutils.resize(frame, width=1080)

    # 检查帧是否要展示
    if args["display"] > 0:
        fps_count  = ( fps_count + (1./(time.time()-t1)) ) / 2
        frame = cv2.putText(frame, "fps= %.2f"%(fps_count), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        
        if key==27:
            #capture.release()
            break
    
    # 更新FPS计数器
    fps.update()
"""
    

# 停止计数器
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# 清理、释放资源
stream.release()
cv2.destroyAllWindows()

# 创建线程化的视频流，允许摄像机传感器预热，并且启动FPS计数器
print("[INFO] sampling THREADED frames from webcam...")
vs = WebcamVideoStream(src=0).start()
fps = FPS().start()

# 使用线程循环处理每一帧
fps_count = 0.0
while (True):
    t1 = time.time()
    # 从线程化的视频流中获取帧，resize到宽度为400像素
    frame = vs.read()
    frame = imutils.resize(frame, width=1080)
    
    # 检查是否需要把帧通过cv2展示
    if args["display"] > 0:
        fps_count  = ( fps_count + (1./(time.time()-t1)) ) / 2
        frame = cv2.putText(frame, "fps= %.2f"%(fps_count), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        
    if key==27:
            #capture.release()
            break
    # 更新FPS计数器
    fps.update()

# 停止计数 展示FPS的统计信息
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
# 做一些清理工作 释放摄像头 关闭打开的窗口
cv2.destroyAllWindows()
vs.stop()
