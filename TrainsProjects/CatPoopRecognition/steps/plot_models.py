# -*- coding: UTF-8 -*-
'''
@Project ：PythonKeepLearning 
@File    ：plot_models.py
@IDE     ：PyCharm 
@Author  ：alphandbelt
@Date    ：2023/11/28 15:43 
'''


'''
    在使用的过程中直接使用pip安装pydot和graphviz会出现一些问题，所以需要手动安装
    1.下载graphviz  https://graphviz.gitlab.io/download/
    2.安装graphviz
    3.配置环境变量
    4.安装pydot
    5.安装pydotplus
    6.在代码中加载环境变量


'''



import os
os.environ["PATH"] += os.pathsep + 'D:/Program Files/Graphviz/bin/'


from keras.models import load_model
from tensorflow.keras.utils import plot_model


# 替换为您的模型路径
model_path = 'model.h5'

# 加载模型
model = load_model(model_path)

# 可视化模型结构
plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)
