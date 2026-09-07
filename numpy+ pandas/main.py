import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

arr = np.array([1,29,29,39,9,59])

age = pd.Series([18,19,29,29,89], dtype = pd.Int16Dtype)
print(arr)
print(age)

## adding index to our age

age = pd.Series(
    np.array(age),
    index=["Alice","bob","carol","YoBor","good"],
    name = "Age"

)

print(age)




## creating  a series 

age = pd.Series([12,23,345,45])

