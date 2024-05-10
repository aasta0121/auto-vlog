import cv2
import numpy as np
from moviepy.editor import *

#im = cv2.imread('./banch.jpg')
#cv2.imshow('image', im)
#cv2.waitKey(0)
#test github

img1 = ImageClip("banch.jpg", transparent=True).set_duration(3)
img2 = ImageClip("love.jpg", transparent=True).set_duration(4).set_start(2).crossfadein(1)
img3 = ImageClip("snow.jpg", transparent=True).set_duration(3).set_start(5).crossfadein(1)

output = CompositeVideoClip([img1,img2,img3])
output.write_videofile("output.mp4",fps=30, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
print('ok')
