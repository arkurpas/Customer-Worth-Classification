import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class NanPlotter:
    
    def __init__(self, na_column_list):
        self.na_column_list = na_column_list

    def bar_chart_plotter(self, data):
        columns_with_nan = self.na_column_list
        value_count = {
            'NaN': [data[col].isna().sum() for col in columns_with_nan],
            'Value': [data[col].notna().sum() for col in columns_with_nan],
        }
        width = 0.8  # the width of the bars: can also be len(x) sequence


        fig, ax = plt.subplots()
        left = np.zeros(len(columns_with_nan))

        for key, value in value_count.items():
            p = ax.barh(columns_with_nan, value, alpha=0.5, left=left)
            left += value

            ax.bar_label(p, label_type='center', padding=10)

        ax.set_title('Amount of NaNs in columns')
        ax.legend(['NaN', 'not_NaN_Value'], loc=4)

        plt.show()





