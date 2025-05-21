import streamlit as st

st.set_page_config(page_title="Cafe Menu", layout="wide")
st.title("☕ Welcome to Brew & Bite Café")
st.subheader("Browse by category")

# Define menu
menu = {
    "Starters": [
        {"name": "Veg Spring Roll", "price": 120, "image": "https://www.womansworld.com/wp-content/uploads/2023/09/airfryer13.jpg?quality=86&strip=all"},
        {"name": "French Fries", "price": 100, "image": "https://www.cuisinart.com/dw/image/v2/ABAF_PRD/on/demandware.static/-/Sites-us-cuisinart-sfra-Library/default/dw3a257599/images/recipe-Images/french-fries-airfryer-recipe.jpg?sw=1200&sh=1200&sm=fit"},
    ],
    "Main Course": [
        {"name": "Paneer Butter Masala", "price": 220, "image": "https://www.ruchiskitchen.com/wp-content/uploads/2020/12/Paneer-butter-masala-recipe-3-500x500.jpg"},
        {"name": "Chicken Biryani", "price": 250, "image": "https://j6e2i8c9.delivery.rocketcdn.me/wp-content/uploads/2020/09/Chicken-Biryani-Recipe-01-1.jpg"},
    ],
    "Drinks": [
        {"name": "Mango Smoothie", "price": 80, "image": "https://vaya.in/recipes/wp-content/uploads/2017/09/Mango-Smoothie_1-1.jpg"},
        {"name": "Dark Chocolate Iced Coffee", "price": 90, "image": "https://lorcoffee.com/cdn/shop/articles/Dark-Chocolate-Ice-Coffee-with-Provocateur-exc.jpg?v=1675806078"},
    ],
    "Desserts": [
        {"name": "Chocolate Brownie", "price": 150, "image": "https://www.spendwithpennies.com/wp-content/uploads/2016/09/Hot-Fudge-Slow-Cooker-Brownies-21.jpg"},
        {"name": "Trifle", "price": 60, "image": "https://media.restless.co.uk/uploads/2021/05/trifle.jpg"},
    ],
}

# Tabs for each category
tabs = st.tabs(list(menu.keys()))
for tab, category in zip(tabs, menu.keys()):
    with tab:
        st.markdown(f"## {category}")
        cols = st.columns(2)
        for i, item in enumerate(menu[category]):
            with cols[i % 2]:
                st.image(item["image"], width=200)
                st.markdown(f"**{item['name']}**  \n💰 ₹{item['price']}")
                st.markdown("---")
