# -*- coding: UTF-8 -*-
'''
@Project ：PythonKeepLearning 
@File    ：check_content_model.py
@IDE     ：PyCharm 
@Author  ：alphandbelt
@Date    ：2023/11/28 15:41 
'''
import h5py

# 读取模型文件
model_file_path = 'model.h5'  # 替换为实际的文件路径
with h5py.File(model_file_path, 'r') as f:
    # 查看文件结构
    print("File structure:")
    print(list(f.keys()))

    # 查看模型的各个层
    model_weights = f['model_weights']
    print("\nModel weights:")
    print(list(model_weights.keys()))

    # 查看每个层的权重
    for layer_name in model_weights.keys():
        layer_group = model_weights[layer_name]
        print(f"\nLayer: {layer_name}")
        print(list(layer_group.keys()))

        # 查看权重的具体内容
        for param_name, param_value in layer_group.items():
            print(f"{param_name}: {param_value}")
