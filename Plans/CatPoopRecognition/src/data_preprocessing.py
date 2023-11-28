# -*- coding: UTF-8 -*-
'''
@Project ：PythonKeepLearning 
@File    ：data_preprocessing.py
@IDE     ：PyCharm 
@Author  ：alphandbelt
@Date    ：2023/11/28 15:11 
'''

from PIL import Image
from keras.preprocessing.image import ImageDataGenerator
from sklearn.preprocessing import LabelEncoder

from sklearn.model_selection import train_test_split

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def resize_images():
    pass


def data_preprocessing():
    # Open an image
    img = Image.open("cat.jpg")

    # Resize the image to (width, height)
    img_resized = img.resize((224, 224))

    # 图像归一化：
    # 将图像的像素值归一化到 [0, 1] 或 [-1, 1] 的范围内。这有助于加速模型的训练过程。

    img_array = img_resized / 255.0  # Normalize pixel values to [0, 1]

    # 图像增强：
    # 通过对图像进行随机变换来增加数据量，从而提高模型的泛化能力。

    # 创建数据增强生成器
    datagen = ImageDataGenerator(
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    # 对图像应用数据增强
    augmented_img = datagen.random_transform(img_array)

    # 标签编码：
    #
    # 如果你的标签是字符串形式，将其转换为模型可理解的数字形式。可以使用 scikit-learn 的 LabelEncoder。

    labels = ["cat", "dog", "bird"]

    # 创建LabelEncoder对象
    label_encoder = LabelEncoder()

    # 标签编码
    encoded_labels = label_encoder.fit_transform(labels)

    # 划分训练集和测试集：
    #
    # 将数据集划分为训练集和测试集，以便评估模型的性能。可以使用 scikit-learn 的 train_test_split。

    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)



    # model 是指代您所选择的机器学习模型的实例。在使用机器学习框架时，您会首先定义和构建一个模型，然后创建该模型的实例，最后使用该实例来训练、评估和进行预测。
    #
    # 在使用 TensorFlow 或 Keras 这样的深度学习框架时，您可能首先会定义一个模型，例如，Sequential 模型，然后使用该模型的实例来训练、评估和进行预测。




    # 创建一个简单的Sequential模型
    model = Sequential()
    model.add(Dense(64, input_shape=(input_dim,), activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    # 训练模型
    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))


    # 评估模型
    # 模型评估：
    #
    # 在测试集上评估训练好的模型，以评估其性能和对新数据的泛化能力。
    loss, accuracy = model.evaluate(X_test, y_test)

    # 模型调优
    # 根据评估结果微调模型。这可能涉及调整超参数、更改模型架构或收集更多数据。

    # 预测
    # 一旦对模型满意，使用它对新的未见数据进行预测。
    predictions = model.predict(X_test)