# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 10:26:15 2024

@author: Jerome
"""
from scipy.io import loadmat
import cv2
import pandas as pd
import numpy as np

# 读取.mat文件
left = loadmat(r'F:\Git\研究生竞赛\C\LeftRadar.mat')['E1']
right = loadmat(r'F:\Git\研究生竞赛\C\RightRadar.mat')['E2']

resized_left = cv2.resize(left, (left.shape[1]*8, left.shape[0]*8), interpolation=cv2.INTER_LINEAR)
resized_right = cv2.resize(right, (right.shape[1]*8, right.shape[0]*8), interpolation=cv2.INTER_LINEAR)
cv2.imshow('resized_left', resized_left)
cv2.imshow('resized_right', resized_right)
cv2.waitKey(0)
