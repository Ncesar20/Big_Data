\# 💤 BDSP Sleep Study Analysis



\## 📌 Overview

This project explores the \*\*BDSP Sleep Dataset\*\* to uncover patterns and insights related to patient demographics, study types, and the presence of annotations. It is divided into two main components:



\- \*\*Python Analytics\*\*: Cleaning, analyzing, modeling, and evaluating data using machine learning.

\- \*\*Power BI Dashboard\*\*: Visualizing the key insights interactively.







\# Project Structure



```

bdsp\_sleep\_analysis/

│

├── data/

│   └── bdsp\_cleaned\_data.csv          # Cleaned dataset used for modeling \& Power BI

│

├── notebooks/

│   └── bdsp\_analysis.ipynb            # Jupyter notebook with full Python analysis

│

├── models/

│   └── final\_model.pkl                # Saved ML model (optional)

│

├── powerbi/

│   └── bdsp\_dashboard.pbix            # Power BI dashboard file

│

├── README.md                          # Project overview and instructions

└── requirements.txt                   # Python dependencies

```



---



\## 🧪 Part 1: Python Analytics



\### 1️⃣ Data Cleaning

\- Handled missing values in `AgeAtVisit`

\- Encoded `SexDSC` and `StudyTypeName`

\- Scaled numeric features (e.g., `AgeAtVisit`)

\- Removed or imputed NaN values



\### 2️⃣ Exploratory Data Analysis (EDA)

\- Explored class imbalance in `HasAnnotations`

\- Visualized patient age distribution and gender split

\- Analyzed relationships among study types, age, and annotations



\### 3️⃣ Modeling (Classification)

\- \*\*Goal:\*\* Predict if a patient has annotations (`HasAnnotations`)

\- Used \*\*RandomForestClassifier\*\*, tuned for class imbalance

\- Applied ensemble with `VotingClassifier` (Logistic, RF, GradientBoosting)



\### 4️⃣ Evaluation

\- Metrics used: Accuracy, Precision, Recall, F1-score

\- Addressed class imbalance using `class\_weight='balanced'` and stratified sampling



\### 5️⃣ Modularity \& Documentation

\- Modular functions: data cleaning, training, evaluation

\- Explanations provided in markdown cells for reproducibility



\### 6️⃣ Innovation

\- Used ensemble learning (soft voting)

\- Applied pipeline-based preprocessing (optional)

\- Feature importance chart generated







\##  Setup Instructions



\### Python Environment



1\. Clone the repository:

```bash

git clone https://github.com/your-username/bdsp\_sleep\_analysis.git

cd bdsp\_sleep\_analysis

```



2\. Create and activate a virtual environment:

```bash

python -m venv venv

source venv/bin/activate       # macOS/Linux

venv\\Scripts\\activate        # Windows

```



3\. Install dependencies:

```bash

pip install -r requirements.txt

```



4\. Run the Jupyter notebook:

```bash

jupyter notebook notebooks/eda\_and\_modeling.ipynb

```





\## 📌 Notes



\- Ensure that `bdsp\_cleaned\_data.csv` is in both your Jupyter Notebook environment and Power BI source folder.

\- You may need to adjust column data types manually in Power BI if not inferred correctly.



---



\## 📬 Contact



Maintained by \*\*Nshuti Cesar\*\*  

For questions or collaboration: \[your-email@example.com]

