import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Example dummy dataset
data = {
    "url_length":[20,120,35,90],
    "https":[1,0,1,0],
    "dots":[2,5,2,6],
    "ip":[0,1,0,1],
    "label":[0,1,0,1]
}

df = pd.DataFrame(data)

X = df.drop("label", axis=1)
y = df["label"]

model = RandomForestClassifier()
model.fit(X,y)

joblib.dump(model,"phishing_model.pkl")

print("Model trained successfully")
