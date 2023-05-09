import pickle
from sklearn.preprocessing import StandardScaler

# load the model
model = pickle.load(open('final_model.sav', 'rb'))

sc = StandardScaler()

def preprocess_data(df):
  return sc.fit_transform(df)

def predict_stroke(df):
  result = model.predict(df)
  return result[0]
  