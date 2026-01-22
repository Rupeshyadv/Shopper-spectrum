import joblib
import pandas as pd
import streamlit as st

# Product Recommendation part
item_similarity_df = joblib.load("./models/item_similarity.pkl")

def recommend_products(product_name, similarity_df, top_n=5):
    if product_name not in similarity_df.index:
        return []

    similar_scores = similarity_df[product_name].sort_values(ascending=False)
    recommendations = similar_scores.iloc[1:top_n+1].index.tolist()
    return recommendations

st.header("🛒 Product Recommendation System")

product_name = st.text_input("Enter Product Name")

if st.button("Get Recommendations"):
    recommendations = recommend_products(product_name, item_similarity_df)

    if recommendations:
        st.subheader("Recommended Products")
        for product in recommendations:
            st.markdown(f"✅ **{product}**")
    else:
        st.warning("Product not found. Please try another product.")


# Customer Segmentation part
kmeans = joblib.load("./models/kmeans_model.pkl")
scaler = joblib.load("./models/scaler.pkl")
cluster_labels = joblib.load("./models/cluster_labels.pkl")

def predict_customer_segment(recency, frequency, monetary):
    input_df = pd.DataFrame(
        [[recency, frequency, monetary]],
        columns=["Recency", "Frequency", "Monetary"]
    )

    scaled_input = scaler.transform(input_df)
    cluster = kmeans.predict(scaled_input)[0]

    return cluster_labels[cluster]

st.header("👤 Customer Segmentation")

recency = st.number_input("Recency (days since last purchase)", min_value=0)
frequency = st.number_input("Frequency (number of purchases)", min_value=0)
monetary = st.number_input("Monetary (total spend)", min_value=0.0)

if st.button("Predict Cluster"):
    segment = predict_customer_segment(recency, frequency, monetary)
    st.success(f"Customer Segment: **{segment}**")
