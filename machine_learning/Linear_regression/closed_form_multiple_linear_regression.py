import numpy as np
import pandas as pd


n = 10000
df = pd.DataFrame({
    "area_sqft": np.random.randint(500, 4000, n),
    "bedrooms": np.random.randint(1, 7, n),
    "age_years": np.random.randint(0, 40, n),
    "distance_km": np.random.uniform(1, 30, n),
    "floor": np.random.randint(1, 21, n)
})

df["price"] = (
    0.05 * df["area_sqft"]
    + 4.0 * df["bedrooms"]
    - 0.15 * df["age_years"]
    - 0.8 * df["distance_km"]
    + 1.5 * df["floor"]
    + np.random.normal(0, 5, n)
)


X = df[["area_sqft","bedrooms","age_years","distance_km","floor"]].to_numpy()
Y = df["price"].to_numpy()


X = np.column_stack((np.ones(X.shape[0]),X))

theta = np.linalg.solve(X.T @ X , X.T @ Y)
y_pred = X @ theta
residual = Y - y_pred

print(theta)