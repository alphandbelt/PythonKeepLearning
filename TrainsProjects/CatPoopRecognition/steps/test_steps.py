# -*- coding: UTF-8 -*-
'''
@Project ：PythonKeepLearning 
@File    ：test_steps.py
@IDE     ：PyCharm 
@Author  ：alphandbelt
@Date    ：2023/11/28 15:31 
'''

# 步骤 1: 收集数据
# 在这个例子中，我们使用 sklearn 库生成一个虚拟数据集
from sklearn.datasets import make_classification
import pandas as pd

# 创建虚拟数据集
X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)

# 转换为 Pandas DataFrame
df = pd.DataFrame(X, columns=[f"feature_{i}" for i in range(X.shape[1])])
df["label"] = y

# 步骤 2: 数据预处理
# 划分训练集和测试集
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 步骤 3: 构建神经网络模型
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import load_model


# 定义模型
model = Sequential()
model.add(Dense(64, input_dim=X.shape[1], activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 编译模型
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 步骤 4: 训练模型
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))


model.save('model.h5')
# 步骤 5: 使用模型进行预测
# 在这个例子中，我们简单地使用测试集进行预测

load_model = load_model('model.h5')


predictions = load_model.predict(X_test)

# 打印预测结果
print(predictions)

