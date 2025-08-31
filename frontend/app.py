import streamlit as st
import pandas as pd
import requests

API_URL = "http://localhost:8000"

def fetch_products():
    """Fetch product data from the backend API."""
    try:
        response = requests.get(f"{API_URL}/products")
        response.raise_for_status()
        data = response.json()
        # Expecting a JSON object with a 'products' key returning a list
        return data.get("products", [])
    except Exception as e:
        st.error(f"Error fetching products: {e}")
        return []

def main():
    st.title("RoomPlanner")
    st.sidebar.title("Upload Room")

    # File uploader for room images or videos
    uploaded_files = st.sidebar.file_uploader(
        "Upload room images or video", type=["jpg", "jpeg", "png", "mp4"], accept_multiple_files=True
    )

    if uploaded_files:
        st.write(f"Uploaded {len(uploaded_files)} file(s)")

    st.header("Product Catalog")
    products = fetch_products()
    if products:
        df = pd.DataFrame(products)
        # Convert price to numeric if needed
        if "price_gbp" in df.columns:
            df["price_gbp"] = pd.to_numeric(df["price_gbp"], errors="coerce")
            min_price = float(df["price_gbp"].min())
            max_price = float(df["price_gbp"].max())
            price_range = st.slider(
                "Price range (£)",
                min_value=min_price,
                max_value=max_price,
                value=(min_price, max_price),
            )
            df = df[(df["price_gbp"] >= price_range[0]) & (df["price_gbp"] <= price_range[1])]

        st.dataframe(df)
    else:
        st.info("No products available. Make sure the backend API is running and returns data.")


if __name__ == "__main__":
    main()
