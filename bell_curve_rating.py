import csv
import plotly.figure_factory as ff
import pandas as pd

df=pd.read_csv("data_mobile.csv")
fig=ff.create_distplot([df["Avg Rating"].tolist()],["rating"],
                       show_hist=False)
fig.show()