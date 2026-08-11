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