import streamlit as st

st.set_page_config(page_title="Cafe Menu", layout="wide")

# Set full-page background to pink
st.markdown(
    """
    <style>
    body {
        background-color: #ffe6f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)


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

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "home"
if "cart" not in st.session_state:
    st.session_state.cart = []
if "customer_info" not in st.session_state:
    st.session_state.customer_info = {"name": "", "mobile": ""}
if "last_added_item" not in st.session_state:
    st.session_state.last_added_item = None
if "last_added_qty" not in st.session_state:
    st.session_state.last_added_qty = 0

# Homepage
if st.session_state.page == "home":
    st.title("☕ Welcome to Brew & Bite Café")
    st.image("https://www.cafeflorista.com/_next/image?url=%2Fimages%2Fcafe%2FIMG-20240922-WA0015.jpg&w=640&q=75", use_container_width=True)
    st.markdown("### Serving delicious food since 2020 🍽️")
    if st.button("View Menu"):
        st.session_state.page = "menu"
        # Reset last added item on navigation
        st.session_state.last_added_item = None
        st.session_state.last_added_qty = 0

# Menu page
elif st.session_state.page == "menu":
    st.title("📋 Menu")
    st.sidebar.title("🛒 Your Cart")

    # Group cart items by name to sum quantities
    grouped_cart = {}
    for item in st.session_state.cart:
        key = item["name"]
        if key in grouped_cart:
            grouped_cart[key]["qty"] += item["qty"]
        else:
            grouped_cart[key] = item.copy()

    total = 0
    for name, item in grouped_cart.items():
        item_total = item["price"] * item["qty"]
        total += item_total
        col1, col2 = st.sidebar.columns([3, 1])
        with col1:
            st.sidebar.write(f"{item['name']} x {item['qty']} = ₹{item_total}")
        with col2:
            if st.sidebar.button("❌", key="remove_" + item["name"]):
                st.session_state.cart = [i for i in st.session_state.cart if i["name"] != item["name"]]
                st.experimental_rerun()

    st.sidebar.markdown(f"**Total: ₹{total}**")

    # Checkout form
    st.sidebar.markdown("---")
    st.sidebar.subheader("👤 Your Details")
    st.session_state.customer_info["name"] = st.sidebar.text_input("Name", value=st.session_state.customer_info["name"])
    st.session_state.customer_info["mobile"] = st.sidebar.text_input("Mobile", value=st.session_state.customer_info["mobile"])

    if st.sidebar.button("Proceed to Checkout"):
        if not st.session_state.customer_info["name"] or not st.session_state.customer_info["mobile"]:
            st.sidebar.warning("Please fill in your name and mobile.")
        elif not grouped_cart:
            st.sidebar.warning("Your cart is empty.")
        else:
            st.session_state.page = "checkout"
            st.session_state.last_added_item = None
            st.session_state.last_added_qty = 0

    # Search bar
    search_query = st.text_input("🔍 Search for items").lower()

    # Category tabs
    tabs = st.tabs(list(menu.keys()))
    for tab, category in zip(tabs, menu.keys()):
        with tab:
            st.markdown(f"## {category}")
            cols = st.columns(2)
            filtered_items = [item for item in menu[category] if search_query in item["name"].lower()]
            for i, item in enumerate(filtered_items):
                with cols[i % 2]:
                    st.image(item["image"], width=200)
                    st.markdown(f"**{item['name']}**  \n💰 ₹{item['price']}")
                    qty_key = "qty_" + item["name"] + category
                    qty = st.number_input(f"Quantity - {item['name']}", min_value=1, max_value=10, value=1, key=qty_key)
                    btn_key = item["name"] + category
                    if st.button(f"Add to Cart - {item['name']}", key=btn_key):
                        st.session_state.cart.append({**item, "qty": qty})
                        st.session_state.last_added_item = btn_key
                        st.session_state.last_added_qty = qty
                    # Show success message just under the button if this item was last added
                    if st.session_state.last_added_item == btn_key:
                        st.success(f"✅ Added {st.session_state.last_added_qty} x {item['name']} to cart")

    if st.button("⬅️ Back to Home"):
        st.session_state.page = "home"
        st.session_state.last_added_item = None
        st.session_state.last_added_qty = 0

# Checkout page
elif st.session_state.page == "checkout":
    st.title("🧾 Order Summary")

    st.markdown(f"**👤 Customer:** {st.session_state.customer_info['name']}  \n📱 **Mobile:** {st.session_state.customer_info['mobile']}")

    st.markdown("---")
    total = 0
    for item in st.session_state.cart:
        subtotal = item["price"] * item["qty"]
        total += subtotal
        st.markdown(f"{item['qty']} x {item['name']} = ₹{subtotal}")
    st.markdown(f"### 🧮 Total: ₹{total}")

    if st.button("✅ Confirm Order"):
        st.success("🎉 Order placed successfully!")
        st.balloons()  # 🎈 Show balloons animation
        st.session_state.cart.clear()
        st.session_state.page = "home"
        st.session_state.last_added_item = None
        st.session_state.last_added_qty = 0

    if st.button("⬅️ Modify Cart"):
        st.session_state.page = "menu"
        st.session_state.last_added_item = None
        st.session_state.last_added_qty = 0
