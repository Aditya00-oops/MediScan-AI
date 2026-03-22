from flask import Flask, render_template, request
import os
import numpy as np

app = Flask(__name__, template_folder='project/templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    risks = None
    health_score = None
    tips = None
    
    if request.method == 'POST':
        try:
            age = float(request.form['age'])
            gender = float(request.form['gender'])
            bmi = float(request.form['bmi'])
            # ... other fields ...
            
            # Mock predictions for demo (models local only)
            risks = {
                'Diabetes': 0.25,
                'Heart Disease': 0.18,
                'Hypertension': 0.32,
                'Obesity': 0.45,
                'Insomnia': 0.12
            }
            health_score = 78
            tips = [
                "✅ Good health trajectory!",
                "💪 Add 30min daily walk",
                "🥗 More veggies",
                "⚕️ Annual checkup",
                "📊 Track BMI monthly"
            ]
        except:
            tips = ["❌ Input error. Use numbers 0-250."]
    
    return render_template('index.html', risks=risks, health_score=health_score, tips=tips)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

