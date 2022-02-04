import pandas as pd
from xgboost import XGBClassifier

def cal(data):
  print(data)
  xnew = pd.DataFrame.from_dict(data)
  xnew = xnew.drop(['orario'],1).drop(['ospite'],1).drop(['casa'],1)
  model = XGBClassifier()
  model.load_model("model.txt")
  ynew1 = str(model.predict(xnew)[-1])
  ynew2 = str(model.predict_proba(xnew)[-1])
  result = ynew1 + ynew2
  return result
