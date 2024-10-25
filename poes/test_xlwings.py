# %% Import Python Libraries
import xlwings as xw
import numpy as np
import pandas as pd
from scipy.stats import norm

# %% Create Excel workbook from Python
wb = xw.Book()

# %% Select the sheet of workbook
sheet = wb.sheets["Sheet1"]


# %% Create a value from Python to Ms. Excel
sheet["C3"].value = "Hello World"

# %% Call a cell from Ms. Excel to Python
value = sheet["C3"].value
print(value)

# %% Generate an array from Python to Ms. Excel
sheet["C7"].options(np.array, Transpose=True).value = np.array([1, 2, 3, 4, 5])


# %% Call an array from Ms. Excel to Python
arrays = sheet["C7:G7"].value
print(arrays)


# %% Generate a pandas DataFrame from Python to Ms. Excel
sheet["D12"].options(pd.DataFrame, expand="table", index=False).value = pd.DataFrame(
    {
        "Oilfield": ["Sacha", "Auca", "Oso_yuralpa"],
        "Well": ["Sacha1", "Auc2", "Oso3"],
        "Oil production (bpd)": [500, 200, 620],
    }
)


# %% Call a DataFrame from Ms. Excel to Python
df = sheet["D12"].options(pd.DataFrame, expand="table", index=False).value
print(df)


# %% Generate random values by using the norm distribution
array_random = norm.rvs(loc=0, scale=2, size=10)
sheet["C19"].options(np.array, Transpose=True).value = array_random
