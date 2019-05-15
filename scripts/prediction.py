#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

mtcars = pd.read_csv("scripts/mtcars.csv")

def predict(json_dict):
    x = mtcars[list(json_dict.keys())]
    y = mtcars['mpg']
    reg = LinearRegression().fit(x, y)
    df = pd.DataFrame(json_dict, index=[0])
    return reg.predict(df)[0]
