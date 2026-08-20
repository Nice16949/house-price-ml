import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

np.random.seed(42)
sample_num = 300
area = np.random.randint(60, 160, sample_num)
room = np.random.randint(1, 5, sample_num)
building_age = np.random.randint(1, 30, sample_num)
price = area * 8500 + room * 22000 - building_age * 1600 + np.random.normal(0, 12000, sample_num)

data = pd.DataFrame({
    "area": area,
    "room": room,
    "building_age": building_age,
    "price": price
})

X = data[["area", "room", "building_age"]]
y = data["price"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("===== 模型训练结果 =====")
print(f"特征系数：{model.coef_}")
print(f"截距：{model.intercept_:.2f}")
print(f"均方误差MSE：{mse:.2f}")
print(f"拟合优度 R²：{r2:.4f}")
house_feature = np.array([[110, 3, 12]])
predict_result = model.predict(house_feature)
print(f"\n【预测示例】面积110㎡，3室，房龄12年，预估房价：{predict_result[0]:.2f} 元")

import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel("真实房价")
plt.ylabel("预测房价")
plt.title("二手房房价预测：真实值 vs 预测值")
plt.show()
