from flask import Flask, render_template, request
import os

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
            blood_pressure = float(request.form.get('blood_pressure', 120))
            glucose = float(request.form.get('glucose', 100))
            cholesterol = float(request.form.get('cholesterol', 200))
            smoking = float(request.form['smoking'])
            activity = float(request.form['activity'])
            
            # Dynamic formula-based predictions (0-1 scale)
            diabetes_risk = min(1.0, 0.4 * (glucose / 200) + 0.3 * (bmi / 40) + 0.2 * (age / 100) + 0.1 * (1-activity))
            heart_risk = min(1.0, 0.35 * (blood_pressure / 200) + 0.25 * (cholesterol / 300) + 0.2 * smoking + 0.1 * (age / 100))
            hypertension_risk = min(1.0, 0.6 * (blood_pressure / 180) + 0.2 * (age / 100) + 0.1 * (bmi / 35))
            obesity_risk = min(1.0, 0.7 * (bmi / 40) + 0.2 * (1-activity) + 0.1 * smoking)
            insomnia_risk = min(1.0, 0.3 * (1-activity) + 0.3 * smoking + 0.2 * (age / 100) + 0.2 * (cholesterol / 400))
            
            risks = {
                'Diabetes': round(diabetes_risk, 2),
                'Heart Disease': round(heart_risk, 2),
                'Hypertension': round(hypertension_risk, 2),
                'Obesity': round(obesity_risk, 2),
                'Insomnia': round(insomnia_risk, 2)
            }
            
            # Dynamic health score (0-100)
            bmi_score = max(0, 100 - 60 * max(0, (bmi-25)/25) - 40 * max(0, (18.5-bmi)/18.5))
            bp_score = max(0, 100 - 50 * max(0, (blood_pressure-120)/60) )
            glucose_score = max(0, 100 - 60 * max(0, (glucose-100)/100))
            activity_score = activity * 100
            age_score = max(0, 100 - age)
            
            health_score = int((bmi_score + bp_score + glucose_score + activity_score + age_score) / 5)
            
            # Dynamic tips based on max risk
            max_risk_disease = max(risks, key=risks.get)
            max_risk = risks[max_risk_disease]
            
            base_tips = [
                f"🚨 Priority: {max_risk_disease} ({max_risk*100:.0f}%)",
                "💪 Exercise 30min daily (walk/swim)",
                "🍽️ Low sugar, more fiber/protein",
                "⚕️ Schedule doctor visit",
                "📊 Track weekly (app/journal)"
            ]
            if health_score > 80:
                base_tips[0] = "✅ Excellent! Keep it up"
            elif health_score < 50:
                base_tips.append("🚨 Urgent lifestyle changes needed")
            
            tips = base_tips
        except Exception as e:
            tips = [f"❌ Input error: {str(e)}. Use numbers 0-500."]
    
    return render_template('index.html', risks=risks, health_score=health_score, tips=tips)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

