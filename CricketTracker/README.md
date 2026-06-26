# 🏏 Cricket AI Analytics Dashboard

An interactive Streamlit-based Cricket Analytics + Machine Learning project that analyzes player performance using real match data, visualizations, and predictive modeling.

---

## 🚀 Features

- 📊 Player performance dashboard  
- 🟢 Single player analytics mode  
- 🔵 Player comparison mode  
- 📈 Runs per match visualization  
- 🤖 Machine Learning performance prediction  
- 📉 Batting average & strike rate calculations  
- 🏆 Performance classification (Elite / Average / Developing)  
- 🎛 Interactive Streamlit web UI  

---

## 🧠 Tech Stack

- Python  
- Streamlit  
- NumPy  
- Matplotlib  
- Scikit-learn (Random Forest Classifier)  
- CSV dataset handling  


## 📊 Dataset Format

Your `matches.csv` should follow this format:(my project example is given below)

Player	Match	Runs	Balls	Wickets
divyesh	1	46	32	2
divyesh	2	72	46	3
divyesh	3	34	18	2
divyesh	4	106	62	5
virat	1	65	23	3
rohit	1	22	8	0
virat	2	104	66	0
virat	3	0	2	2
dhoni	1	20	23	0
dhoni	2	40	35	0
rohit	2	72	35	0
hardik	1	20	5	3
hardik	2	65	34	3
hardik	3	43	22	1
divyesh	5	0	4	2
virat	4	89	53	3
rohit	3	100	59	0
hardik	4	20	8	4
rohit	4	79	39	0

---

## ⚙️ Installation

Install required libraries:

python -m pip install streamlit scikit-learn numpy matplotlib

---

## ▶️ How to Run

Run the Streamlit app:

python -m streamlit run cricket_app.py

---

## 🧪 How It Works

### 📊 Data Processing
- Reads match-wise player data
- Calculates:
  - Strike Rate
  - Impact Score
  - Performance metrics

---

### 🤖 Machine Learning Model
- Algorithm: Random Forest Classifier  
- Features used:
  - Runs  
  - Balls faced  
  - Wickets  
  - Strike Rate  
  - Impact Score  

- Output:
  - 🔥 Elite Performance Player  
  - ⚠ Average / Developing Player  

---

## 🟢 Modes

### Single Player Mode
- Individual stats
- Performance graph
- ML prediction result

### Compare Mode
- Compare two players
- Side-by-side stats
- Dual performance graph

---

## 📈 Insights

- High strike rate → better performance
- High runs + wickets → all-rounder impact
- Consistency matters more than single-match performance

## 👨‍💻 Author
BY Divyesh .M

Built as a personal AI + sports analytics project exploring:
- Machine Learning  
- Data Science  
- Streamlit web apps  

