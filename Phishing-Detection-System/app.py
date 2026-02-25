from flask import Flask, render_template, request
import joblib
from feature_extractor import extract_features
from rule_engine import rule_based_check

app = Flask(__name__)
model = joblib.load("phishing_model.pkl")

@app.route("/", methods=["GET","POST"])
def home():
    result = None

    if request.method == "POST":
        url = request.form["url"]

        rule_score = rule_based_check(url)

        if rule_score >= 3:
            result = "⚠️ Phishing (Rule-Based Detection)"
        else:
            features = extract_features(url)
            prediction = model.predict([features])[0]
            result = "✅ Safe" if prediction == 0 else "⚠️ Phishing"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
