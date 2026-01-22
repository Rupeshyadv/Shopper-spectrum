# 🛒 E-Commerce Customer Segmentation & Product Recommendation System

## 📌 Project Overview

The global e-commerce industry generates vast amounts of transaction data daily, providing valuable insights into customer purchasing behavior. Effectively analyzing this data enables businesses to identify meaningful customer segments and recommend relevant products, ultimately improving customer experience and driving business growth.

This project analyzes online retail transaction data to:

- Perform detailed Exploratory Data Analysis (EDA)
- Segment customers using RFM (Recency, Frequency, Monetary) analysis
- Apply KMeans clustering to identify customer groups
- Build an item-based collaborative filtering recommendation system
- Deploy an interactive web application using Streamlit

---

## 📂 Dataset Description

The dataset contains transactional records from an online retail store with the following attributes:

| Column      | Description                |
| ----------- | -------------------------- |
| InvoiceNo   | Unique invoice identifier  |
| StockCode   | Product code               |
| Description | Product name               |
| Quantity    | Quantity purchased         |
| InvoiceDate | Date and time of purchase  |
| UnitPrice   | Price per unit             |
| CustomerID  | Unique customer identifier |
| Country     | Customer country           |

---

## 🔍 Exploratory Data Analysis (EDA)

The following analyses were conducted:

- Transaction volume by country
- Identification of top-selling products
- Purchase trends over time
- Monetary distribution per transaction and per customer
- RFM distributions
- Elbow curve for cluster selection
- Customer cluster profiling
- Product similarity heatmap using collaborative filtering

---

## 🧠 RFM Analysis & Customer Segmentation

### 📌 RFM Feature Engineering

- **Recency (R):** Number of days since the customer’s last purchase
- **Frequency (F):** Total number of transactions made by the customer
- **Monetary (M):** Total amount spent by the customer

### 📌 Clustering Methodology

1. RFM feature computation
2. Feature standardization using `StandardScaler`
3. KMeans clustering
4. Optimal number of clusters selected using:
   - Elbow Method
   - Silhouette Score
5. Cluster profiling and interpretation
6. Customer segment labeling:
   - **High-Value:** Recent, frequent, high spenders
   - **Regular:** Moderate frequency and spending
   - **Occasional:** Infrequent and low spending customers
   - **At-Risk:** Customers inactive for a long time with low engagement

---

## 🎯 Product Recommendation System

An **item-based collaborative filtering** approach was used to recommend products.

### 🔧 Methodology

- Constructed a Customer–Product purchase matrix
- Computed cosine similarity between products
- Identified products frequently purchased together
- Visualized product similarities using a heatmap

### 🔍 Recommendation Logic

When a user enters a product name, the system recommends the **top 5 most similar products** based on cosine similarity scores.

---

## 🌐 Streamlit Web Application

The project is deployed as an interactive Streamlit application with the following modules:

### 1️⃣ Product Recommendation Module

- Input: Product name
- Output: Top 5 similar product recommendations

### 2️⃣ Customer Segmentation Module

- Inputs:
  - Recency (days)
  - Frequency (number of purchases)
  - Monetary (total spend)
- Output: Predicted customer segment (High-Value, Regular, Occasional, At-Risk)

---

## 🛠️ Technologies Used

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Streamlit
- Joblib

---

## ▶️ How to Run the Project Locally

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

## 2️⃣ Create Virtual Environment

Create and activate a virtual environment to manage dependencies.

### On Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### On macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

Install all required Python libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install manually:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit
```

---

## 4️⃣ Run the Streamlit App

Start the Streamlit application using:

```bash
streamlit run app.py
```

After running the command, open the browser link shown in the terminal  
(usually `http://localhost:8501`).

---

## ☁️ Deployment

The application is deployed on Streamlit Cloud.
All trained models and similarity matrices are saved using joblib and loaded at runtime.

---

## 📈 Results & Insights

- Clear separation of customer segments using RFM-based KMeans clustering
- Identification of high-value and at-risk customers for targeted strategies
- Meaningful product recommendations based on co-purchase behavior
- Fully functional, end-to-end ML-powered web application

---

## 📌 Conclusion

This project demonstrates how transaction data can be leveraged to extract actionable insights through customer segmentation and personalized recommendations. The combination of RFM analysis, clustering, and collaborative filtering provides a scalable solution for enhancing customer engagement in e-commerce platforms.

---
