# 📊 Exploratory Data Analysis (EDA) Web App

Welcome to the **Exploratory Data Analysis** repository! This project is a Streamlit-based web application designed to perform insightful data analysis on credit card transaction data, providing an interactive way to explore trends, patterns, and spending habits.

## 🚀 Live Demo
Check out the live app here: [Exploratory Data Analysis App](https://exploratory-data-analysis-anirudh.streamlit.app/)

## 🧠 Overview
This EDA app enables users to explore various aspects of credit card transactions, such as:
- **Spending by City**: Visualizes spending trends across different cities.
- **Spending by Card Type**: Breaks down expenses by card types.
- **Expense Type Analysis**: Offers insights on spending categories.
- **Gender-Based Analysis**: Analyzes spending habits based on gender.
- **Monthly and Yearly Trends**: Uncovers trends across months and years.

The data is pre-processed and analyzed with Python, and visualized in an interactive format through Streamlit.

## 📋 Key Features
- **User-Friendly Interface**: Simplified navigation and data visualization with Streamlit.
- **Detailed Analytics**: Analyze spending patterns through multiple filters and categories.
- **Data Insights**: Offers deep insights on spending trends, helping users better understand transaction behaviors.
- **Customizable Visualization**: Interactive graphs, charts, and tables allow for dynamic exploration of data.

## 🛠️ Technologies Used
- **Python**: Core programming language.
- **Streamlit**: Framework for building interactive, data-driven front-end applications.
- **Pandas**: For data cleaning and manipulation.
- **Matplotlib & Seaborn**: Libraries for data visualization.

## 🗂️ Project Structure
- `app.py`: Main Streamlit application script.
- `data/`: Contains pre-processed credit card transactions dataset.
- `notebooks/`: Jupyter Notebooks with initial data analysis and cleaning steps.
- `requirements.txt`: Lists dependencies required to run the app.

## 🚀 Getting Started

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/exploratory-data-analysis.git
   cd exploratory-data-analysis
   ```

2. **Set up the environment**:
   Ensure Python is installed (Python 3.7+ recommended). Install dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app locally**:
   Start the app by executing:
   ```bash
   streamlit run app.py
   ```
   The app will be accessible at `http://localhost:8501`.

## 📊 Dataset Details
This app uses a dataset of credit card transactions containing 26,052 rows and 9 columns with fields such as:
- **City**: Transaction location.
- **Date**: Date of the transaction.
- **Card Type**: Type of card used.
- **Expense Type**: Category of the transaction.
- **Gender**: Gender of the cardholder.
- **Amount**: Transaction amount.
- **Year and Month**: Derived from transaction date for trend analysis.

## 📈 Conclusion and Analysis
This EDA web app offers valuable insights into user spending patterns by allowing an interactive exploration of credit card transaction data. Through various visualizations, users can uncover trends, compare categories, and make data-driven decisions. This tool serves as an efficient way for analysts, businesses, and individuals to gain insights into spending behaviors. 

Explore the app: [Exploratory Data Analysis App](https://exploratory-data-analysis-anirudh.streamlit.app/)

