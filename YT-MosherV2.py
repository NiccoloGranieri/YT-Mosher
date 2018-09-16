from __future__ import unicode_literals
import urllib.request
import urllib.parse
import re
import os
import youtube_dl
from moviepy.editor import VideoFileClip, concatenate_videoclips
from random import uniform, random, randint
import time
import datetime
from moviepy.editor import *

word_array = ['ASMR', 'pink noise', 'vine complation', 'slow tv']

for x in range(0, len(word_array)):
    txt_clip = TextClip(word_array[x], fontsize=100, color='white').set_pos("bottom")
    # finishedVideo = VideoFileClip('Output'+str(iterations-1)+'.mp4')
    finishedVideo = VideoFileClip("/Users/Nico/Desktop/YTGlitch/Sqr.mp4")
    videolength = finishedVideo.duration
    subbedVideo = CompositeVideoClip([finishedVideo, txt_clip])
    subbedVideo.subclip(x, x+1).write_videofile('Subbed' + str(x) + '.mp4')