# -*- coding: UTF-8 -*-
'''
@Project ：PythonKeepLearning 
@File    ：use_model.py
@IDE     ：PyCharm 
@Author  ：alphandbelt
@Date    ：2023/11/28 16:25 
'''
import numpy as np
from keras.models import load_model
from keras.preprocessing import image

# 加载保存的模型
model = load_model('cat_poop_model.keras')


# 用于将图像转换为模型输入的预处理函数
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(64, 64))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


# 预测图像
def predict_image(model, img_path):
    img_array = preprocess_image(img_path)
    result = model.predict(img_array)
    return result


# 图像文件路径
img_path = 'test_mode3.jpg'

# 进行预测
prediction = predict_image(model, img_path)

# 打印预测结果
print(prediction)
