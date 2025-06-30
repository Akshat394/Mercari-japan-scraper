import streamlit as st
from query import get_products_by_tags, get_products_by_category, search_products_by_title

st.set_page_config(layout="wide", page_title="🛒 Mercari Product Explorer")

st.sidebar.title("🔍 Filter Products")

category = st.sidebar.text_input("Category")
tag_filter = st.sidebar.multiselect("SEO Tags", ["apple", "android", "smartphone", "gaming", "bag", "audio"])
min_price, max_price = st.sidebar.slider("Price Range", 0, 50000, (0, 20000))
min_rating = st.sidebar.slider("Min Seller Rating", 0.0, 5.0, 0.0, 0.1)

# Add a search bar at the top of the main page
search_term = st.text_input("🔎 Search for products", "")

st.title("🛍️ Mercari Product Explorer")

# Search logic: prioritize search bar, then category, then tags
if search_term:
    products = search_products_by_title(search_term)
elif category:
    products = get_products_by_category(category)
elif tag_filter:
    products = get_products_by_tags(tag_filter)
else:
    products = search_products_by_title("")

cols = st.columns(3)

for idx, product in enumerate(products):
    with cols[idx % 3]:
        st.image(product["image_url"], width=180)
        st.markdown(f"**{product['title']}**")
        st.markdown(f"💴 ¥{product['price']}")
        if product.get("condition"):
            st.markdown(f"📦 Condition: {product['condition']}")
        if product.get("seo_tags"):
            st.markdown("🏷️ Tags: " + ", ".join(product["seo_tags"]))
        st.link_button("View on Mercari", product["product_url"]) 