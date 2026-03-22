from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np
from collections import defaultdict

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    risks = None
    health_score = None
    tips = None
    
    if request.method == 'POST':
        # Common general details
        age = float(request.form['age'])
        gender = float(request.form['gender'])
        bmi = float(request.form['bmi'])
        blood_pressure = float(request.form['blood_pressure'])
        glucose = float(request.form['glucose'])
        cholesterol = float(request.form['cholesterol'])
        smoking = float(request.form['smoking'])
        activity = float(request.form['activity'])
        
        # Base input for all models (common 8 features)
        common_data = [age, gender, bmi, blood_pressure, glucose, cholesterol, smoking, activity]
        
        # Load diabetes model (fallback)
        model = joblib.load('model.pkl')
        
        # Predict for all diseases (using diabetes model as base, adjusted)
        pred = model.predict([common_data])[0]
        proba = model.predict_proba([common_data])[0][1]  # Risk prob
        
        # Mock multi-disease risks based on inputs (real models would use here)
        diabetes_risk = proba
        heart_risk = min(1, 0.7 * proba + 0.3 * (blood_pressure / 200) + 0.1 * smoking)
        hypertension_risk = min(1, 0.6 * proba + 0.4 * (blood_pressure / 180))
        obesity_risk = 0.8 * (bmi / 40) if bmi > 25 else 0.2
        insomnia_risk = min(1, 0.5 * proba + 0.3 * (cholesterol / 300) + 0.2 * smoking)
        
        risks = {
            'Diabetes': round(diabetes_risk, 2),
            'Heart Disease': round(heart_risk, 2),
            'Hypertension': round(hypertension_risk, 2),
            'Obesity': round(obesity_risk, 2),
            'Insomnia': round(insomnia_risk, 2)
        }
        
        # Health score
        bmi_score = 100 if 18.5 <= bmi <= 24.9 else 70 if bmi < 30 else 40
        bp_score = 100 if blood_pressure < 120 else 80 if blood_pressure < 140 else 50
        glucose_score = 100 if glucose < 100 else 80 if glucose < 126 else 50
        
        health_score = int((bmi_score + bp_score + glucose_score) / 3)
        
        # Tips based on highest risk
        highest_risk = max(risks, key=risks.get)
        pred_high = pred == 1 or max(risks.values()) > 0.6
        
        if pred_high:
            tips = [
                "🚨 Highest risk: " + highest_risk,
                "💪 Start exercising 30min daily",
                "🍽️ Focus on balanced diet",
                "⚕️ Consult healthcare professional",
                "📊 Track progress weekly"
            ]
        else:
            tips = [
                "✅ Low overall risk - Good job!",
                "🏃‍♂️ Maintain current activity",
                "🥗 Continue healthy eating",
                "📅 Annual checkups recommended",
                "😊 Stay consistent!"
            ]
    
    return render_template('index.html', risks=risks, health_score=health_score, tips=tips)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
