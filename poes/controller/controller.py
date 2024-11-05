import xlwings as xw
from poes.model.poes import poes
import numpy as np
import pandas as pd

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
LIM_MIN = "Lim min"
LIM_MAX = "Lim max"

# Call cells from Ms Excel
DET_VALUES = "det_values"
DF_POES = "def_poes"
REALIZATIONS = "realizations"
SEED = "seed"

# Write values in Excel from Python
POES_DET = "det_result"
POES_PROB = "poes_prob"
POES_ARRAY = "poes_array"

# Index of POES Parameters
AREA_IDX, H_IDX, PORO_IDX, SWI_IDX, BOI_IDX = 0, 1, 2, 3, 4


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
