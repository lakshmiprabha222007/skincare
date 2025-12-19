import streamlit as st
import pandas as pd

# Title
st.title("Skincare Product Recommender")
st.write("Select your skin type and get recommended skincare products!")

# Load dataset
df = pd.read_excel("skincare_100_rows.xlsx")

# User input for skin type
skin_type = st.selectbox(
    "Select your Skin Type:",
    df["Skin_Type"].unique()
)

# Filter products based on skin type
recommended = df[df["Skin_Type"] == skin_type]

# Display recommended products
st.subheader(f"Recommended Products for {skin_type} skin:")
st.dataframe(recommended[["Product_Code", "Product_Name", "Brand", "Category"]])

# Optional: Download CSV of recommendations
csv = recommended.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Recommendations as CSV",
    data=csv,
    file_name='recommended_products.csv',
    mime='text/csv'
)
