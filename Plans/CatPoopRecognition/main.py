# -*- coding: UTF-8 -*-
'''
@Project ：PythonKeepLearning 
@File    ：main.py
@IDE     ：PyCharm 
@Author  ：alphandbelt
@Date    ：2023/11/28 16:21 
'''
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# 1. 创建ImageDataGenerator
datagen = ImageDataGenerator(rescale=1./255,  # 缩放像素值到0-1之间
                             shear_range=0.2,  # 随机错切变换
                             zoom_range=0.2,  # 随机缩放
                             horizontal_flip=True)  # 水平翻转

# 2. 划分数据集
train_set = datagen.flow_from_directory('./training_data',
                                       target_size=(64, 64),  # 图像将被调整为该大小
                                       batch_size=32,
                                       class_mode='binary')  # 二分类问题

validation_set = datagen.flow_from_directory('./validation_data',
                                            target_size=(64, 64),
                                            batch_size=32,
                                            class_mode='binary')

# 3. 定义模型
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))

# 4. 编译模型
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 5. 训练模型
model.fit(train_set, epochs=25, validation_data=validation_set)

# 6. 保存模型
model.save('cat_poop_model.keras')
