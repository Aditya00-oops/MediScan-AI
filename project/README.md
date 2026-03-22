# MediScan AI — Lifestyle Disease Risk Predictor & Compliance Coach

## 🏃‍♂️ Quick Start (Windows)

### Step 1: Navigate to project folder
```cmd
cd project
```

### Step 2: Create & activate virtual environment (recommended)
```cmd
python -m venv mediscan_env
mediscan_env\Scripts\activate

```

### Step 3: Install required packages
```cmd
pip install flask scikit-learn pandas numpy joblib
```

### Step 4: Train the AI model
```cmd
python train_model.py
```
*This creates `model.pkl` (takes ~2 seconds)*

### Step 5: Run the web app
```cmd
python app.py
```

### Step 6: Open in browser
http://127.0.0.1:5000

## 🎯 Features
- ✅ AI Diabetes Risk Prediction (Random Forest)
- ✅ Health Score (0-100)
- ✅ Personalized Prevention Tips
- ✅ Clean, responsive UI
- ✅ Works 100% offline
- ✅ Beginner-friendly

## 📁 Files Created
```
project/
├── diabetes.csv              # Training data
├── train_model.py           # AI model training
├── app.py                   # Flask web app
├── model.pkl               # Trained AI model (auto-generated)
└── templates/
    └── index.html          # Frontend UI
```

## 🧪 Test with sample data:
- **High Risk**: Age=50, Glucose=148, BMI=33.6, Pregnancies=6
- **Low Risk**: Age=31, Glucose=85, BMI=26.6, Pregnancies=1

## 🚀 Deploy to Render.com (Free)

1. **Push to GitHub**:
```
git init
git add .
git commit -m "MediScan AI v1"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/mediscan-ai.git
git push -u origin main
```

2. **Render.com**:
- Sign up (GitHub login)
- New > Web Service > Connect GitHub repo
- Runtime: Python
- Build: `pip install -r requirements.txt`
- Start: `gunicorn app:app`
- FREE tier auto!

**Live URL**: https://your-app.onrender.com

## 🔧 Troubleshooting
- Model accuracy: ~75-80% 
- Install: `pip install -r requirements.txt`
**Deployed with ❤️ for healthcare awareness**



