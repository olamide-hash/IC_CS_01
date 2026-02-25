# 🔐 Phishing Detection System

## Internship Project – InternCred

This project was completed as part of my cybersecurity internship task at InternCred.  
The objective was to design and document a simple system capable of detecting phishing websites using practical security concepts and basic machine learning techniques.

The project focuses on understanding how phishing URLs can be analyzed and classified rather than building a production-level security tool.

---

## Project Overview

Phishing attacks are one of the most common ways attackers steal user credentials and personal information. These attacks usually rely on fake websites that look similar to trusted platforms.

This application allows a user to enter a URL and receive a prediction showing whether the website appears safe or potentially malicious.

The system combines rule-based analysis with a machine learning model to reach a decision.

---

## Purpose of the Task

During this internship task, the goals were to:

- understand phishing attack patterns
- extract useful information from URLs
- apply machine learning in cybersecurity
- build a simple web interface for testing
- properly document a technical project

---

## How the System Works

### 1. Rule-Based Detection

The program first checks the URL using predefined security rules.  
Examples include:

- unusually long URLs
- presence of "@" symbols
- excessive subdomains
- missing HTTPS
- suspicious keywords such as login or verify

If multiple warning signs are detected, the URL is flagged as phishing.

---

### 2. Machine Learning Detection

If rule checks are not enough, the system extracts features from the URL and sends them to a trained model.

Features used:

- URL length
- HTTPS usage
- number of dots in the domain
- detection of IP-based domains

A Random Forest classifier is used to predict the result.

---

## Technology Used

- Python
- Flask
- Scikit-learn
- Pandas
- HTML

---

## Project Structure

phishing-detection-system/

app.py                -> Main Flask application  
train_model.py        -> Model training script  
feature_extractor.py  -> URL feature extraction  
rule_engine.py        -> Rule-based checks  
phishing_model.pkl    -> Saved machine learning model  
requirements.txt      -> Project dependencies  
templates/            -> HTML interface  

---

## How to Run the Project

1. Install Python 3 on your system.

2. Install dependencies:

pip install -r requirements.txt

3. Train the machine learning model:

python train_model.py

4. Run the application:

python app.py

5. Open your browser and visit:

http://localhost:5000

Enter any URL to test the detection system.

---

## Example

Input:
http://fake-login-secure-bank.com

Output:
Phishing detected

---

## What I Learned

Through this internship task, I gained practical experience in:

- identifying phishing indicators
- feature extraction from URLs
- training and saving ML models
- connecting backend logic with a web interface
- documenting a cybersecurity project clearly

---

## Possible Improvements

Future improvements could include:

- domain age checking using WHOIS data
- integration with live phishing databases
- email phishing detection
- browser extension integration
- improved datasets for higher accuracy

---

## Author

Olamide Basit Alabi  
Cybersecurity Intern (InternCred)

---

## Note

This project was developed for educational and internship learning purposes.
