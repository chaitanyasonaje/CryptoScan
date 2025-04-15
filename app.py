from flask import Flask, render_template, request
import joblib
from feature_extractor import extract_features

from sklearn.metrics import classification_report, accuracy_score
import pandas as pd

app = Flask(__name__)

# Load model and encoder
model = joblib.load("models/stat_feature_model.pkl")
label_encoder = joblib.load("models/stat_label_encoder.pkl")

# Load dataset for reference metrics
df = pd.read_csv("cryptography_dataset_enhanced.csv")
df = df[~df['Algorithm'].isin(['RSA', 'SHA-256'])].dropna(subset=['Key'])
combined = df['Ciphertext'] + df['Key']
X = extract_features(combined)
y = label_encoder.transform(df['Algorithm'])
accuracy = round(accuracy_score(y, model.predict(X)) * 100, 2)
report = classification_report(y, model.predict(X))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    ciphertext = request.form['ciphertext']
    features = extract_features([ciphertext])[0]
    pred = model.predict([features])[0]
    algorithm = label_encoder.inverse_transform([pred])[0]

    char_counts = features[:256].tolist()
    mean_ascii = round(features[-3], 2)
    std_ascii = round(features[-2], 2)

    return render_template('result.html', algorithm=algorithm,
                           char_counts=char_counts,
                           mean_ascii=mean_ascii,
                           std_ascii=std_ascii,
                           accuracy=accuracy,
                           report=report)

if __name__ == "__main__":
    app.run(debug=True)
