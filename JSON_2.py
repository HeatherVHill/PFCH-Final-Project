#NEVERMIND - need way too much space to install this

import pandas as pd

dic = open("Paston_Letters.json","r")

pd.DataFrame(dic).T.reset_index().to_csv('Paston_attempt_2.csv', header=False, index=False)
