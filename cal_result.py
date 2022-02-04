import pandas as pd
from xgboost import XGBClassifier

def cal(data):
  print(data)
  x = pd.DataFrame.from_dict(data)
  xnew = x.drop(['orario'],1).drop(['ospite'],1).drop(['casa'],1)
  model = XGBClassifier()
  model.load_model("model.txt")
  ynew1 = str(model.predict(xnew)[-1])
  ynew2 = model.predict_proba(xnew)[-1]
  result = {'casa':x['casa'].iloc[0],'ospite':x['ospite'].iloc[0],'orario':x['orario'].iloc[0],'pred':ynew1,'prob_1':ynew2[1].item(),'prob_X':ynew2[0].item(),'prob_2':ynew2[2].item()}
  return result
