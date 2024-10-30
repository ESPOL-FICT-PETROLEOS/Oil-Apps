import xlwings as xw
from poes.model.poes import poes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define Sheets Names
SUMMARY = "Summary"
RESULTS = "Results"

# Define Column Names
VARIABLES = "Variables"
VALUES = "Values"
DISTRIBUTION = "Distribution"
LOC = "Loc"
SCALE = "Scale"
C = "c"
LIM_MIN = "Limit min"
LIM_MAX = "Limit max"

# Call cells from Ms Excel
DET_VALUES = "det_values"
DF_POES = "def_poes"
REALIZATIONS = "realizations"
SEED = "seed"

# Write values in Excel from Python
POES_DET = "det_result"


def main():
    wb = xw.Book.caller()
    # Define sheet to use
    sheet = wb.sheets[SUMMARY]
    # Call values for deterministic POES
    params = sheet[DET_VALUES].options(np.array, Transpose=True).value

    sheet[POES_DET].value = poes(*params)


if __name__ == "__main__":
    xw.Book("poes.xlsm").set_mock_caller()
    main()
