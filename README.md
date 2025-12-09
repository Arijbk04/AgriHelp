# 🌾 AgriPredict - Crop Recommendation System

A smart crop recommendation system using Machine Learning to help farmers choose the best crop based on soil and climate conditions.

---

##  About

AgriPredict uses a **Decision Tree algorithm** to predict the most suitable crop for your land based on:
- Soil nutrients (N, P, K, pH)
- Climate conditions (Temperature, Humidity, Rainfall)

**Accuracy: 99%+** on 22 different crop types.

---

##  Features

- Machine Learning prediction (Decision Tree)
- 22 crop types supported
- Simple and clean GUI (Tkinter)
- Built-in crop information database
- Fast and accurate predictions

---

**Requirements:**
- Python 3.8+
- NumPy, Pandas, Scikit-learn, Joblib
- Tkinter (included with Python)

---

##  Usage

1. Launch the app: `python app.py`
2. Enter soil parameters (N, P, K, pH)
3. Enter climate data (Temperature, Humidity, Rainfall)
4. Click **PREDICT** to get crop recommendation
5. Click **INFO** to view crop growing conditions

---

##  Dataset

**Source:** [Kaggle - Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)

- 2200+ samples
- 7 features (N, P, K, Temperature, Humidity, pH, Rainfall)
- 22 crop types

**Supported Crops:**
Rice, Maize, Chickpea, Kidneybeans, Pigeonpeas, Mothbeans, Mungbean, Blackgram, Lentil, Pomegranate, Banana, Mango, Grapes, Watermelon, Muskmelon, Apple, Orange, Papaya, Coconut, Cotton, Jute, Coffee

---

##  Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | 99.1% |
| Precision | 99.0% |
| Recall | 99.1% |
| F1-Score | 99.0% |

**Algorithm:** Decision Tree Classifier (Gini, max_depth=15)

---

##  Tech Stack

- **Python** - Programming language
- **Scikit-learn** - Machine Learning
- **Tkinter** - GUI
- **NumPy & Pandas** - Data processing

---

##  Author

**[Boubaker Arij]**
- GitHub: [@arijbk04](https://github.com/arijbk04)
- Email: boubakerarij3@gmail.com

---

##  Acknowledgments

- Kaggle for the dataset
- Scikit-learn community
- Agricultural domain experts
