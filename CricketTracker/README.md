# 🏏 Cricket AI Analytics Dashboard

An interactive Streamlit-based Cricket Analytics and Machine Learning project that analyzes player performance using real match data, statistical features, and predictive modeling.

---

## 🎯 Problem Statement

Cricket player performance is often judged using simple totals like runs or wickets, which fail to capture consistency, impact, and overall contribution across multiple matches.

This project builds a data-driven system to analyze player performance more effectively using statistical features and machine learning classification.

---

## 🚀 Features

- 📊 Player performance dashboard  
- 🟢 Single player analytics mode  
- 🔵 Player comparison mode  
- 📈 Runs per match visualization  
- 📉 Batting average & strike rate calculations  
- 🧠 Feature-based performance evaluation  
- 🤖 Machine Learning-based player classification  
- 🏆 Performance categories: Elite / Average / Developing  
- 🎛 Interactive Streamlit web UI  

---

## 🧠 Why Machine Learning?

Machine learning is used to identify patterns in player performance across multiple matches.

Instead of relying on single-match statistics, the model learns relationships between:
- Runs  
- Balls faced  
- Wickets  
- Strike Rate  
- Impact Score  

This helps in evaluating **overall performance trends rather than isolated performances**.

---

## 🧠 Tech Stack

- Python  
- Streamlit  
- NumPy  
- Matplotlib  
- Scikit-learn (Random Forest Classifier)  
- CSV dataset handling  

---

## 📊 Dataset Format

The dataset should follow this structure:

Player | Match | Runs | Balls | Wickets  

Example:

Divyesh 1 46 32 2  
Divyesh 2 72 46 3  
Virat 1 65 23 3  
Rohit 1 22 8 0  
Dhoni 2 40 35 0  
Hardik 1 20 5 3  

---

## ⚙️ How It Works

### 📊 Data Processing

Reads match-wise player data and calculates:

- Strike Rate  
- Batting Average  
- Impact Score  
- Performance metrics  

---

### 🤖 Machine Learning Model

Algorithm: Random Forest Classifier  

Features used:

- Runs  
- Balls faced  
- Wickets  
- Strike Rate  
- Impact Score  

Output:

- 🔥 Elite Player  
- ⚠ Average / Developing Player  
- 🟢 Classification based on overall performance trends  

---

## 🟢 Modes

### Single Player Mode

- Individual stats analysis  
- Performance graph visualization  
- ML prediction result  

---

### Compare Mode

- Compare two players  
- Side-by-side stats  
- Dual performance graphs  

---

## 📈 Insights

- High strike rate improves performance rating  
- Consistent performance is more important than single-match peaks  
- All-round performance (runs + wickets) increases impact score  
- Long-term trends matter more than isolated matches  

---

## 📌 Future Improvements

- Compare multiple ML models (Logistic Regression, XGBoost)  
- Add feature importance visualization  
- Improve dataset realism with larger datasets  
- Add time-series performance trends  

---

## 👨‍💻 Author

BY Divyesh M Perabattula  

Built as a personal AI + sports analytics project exploring:

- Machine Learning  
- Data Science  
- Streamlit web apps  

---

## 🎯 Project Goal

To explore how Machine Learning can be applied to sports analytics for better understanding of player performance trends and decision-making.
