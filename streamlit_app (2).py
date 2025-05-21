import streamlit as st
import time

st.set_page_config(page_title="Cafe Menu", layout="wide")

# Background color styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffe6f0;
    }
    [data-testid="stSidebar"] {
        background-color: #ffe6f0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Category Icons
category_images = {
    "Starters": "https://c.ndtvimg.com/2023-08/sfc3gcoo_chicken-snack_625x300_21_August_23.jpg?im=FaceCrop,algorithm=dnn,width=1200,height=675",
    "Main Course": "https://cbx-prod.b-cdn.net/COLOURBOX60103276.jpg?width=800&height=800&quality=70",
    "smoothies": "https://thumbs.dreamstime.com/b/colorful-smoothies-glass-jars-fresh-fruit-black-surface-colorful-smoothies-glass-jars-fresh-fruit-black-339067901.jpg",
    "Desserts": "https://cdn.hswstatic.com/gif/desserts-update.jpg",
}

menu = {
    "Starters": [
        {"name": "Veg Spring Roll", "price": 120, "image": "https://www.womansworld.com/wp-content/uploads/2023/09/airfryer13.jpg?quality=86&strip=all"},
        {"name": "French Fries", "price": 100, "image": "https://www.cuisinart.com/dw/image/v2/ABAF_PRD/on/demandware.static/-/Sites-us-cuisinart-sfra-Library/default/dw3a257599/images/recipe-Images/french-fries-airfryer-recipe.jpg?sw=1200&sh=1200&sm=fit"},
    ],
    "Main Course": [
        {"name": "Paneer Butter Masala", "price": 220, "image": "https://www.ruchiskitchen.com/wp-content/uploads/2020/12/Paneer-butter-masala-recipe-3-500x500.jpg"},
        {"name": "Chicken Biryani", "price": 250, "image": "https://j6e2i8c9.delivery.rocketcdn.me/wp-content/uploads/2020/09/Chicken-Biryani-Recipe-01-1.jpg"},
    ],
    "smoothies": [
        {"name": "Mango Smoothie", "price": 80, "image": "https://vaya.in/recipes/wp-content/uploads/2017/09/Mango-Smoothie_1-1.jpg"},
        {"name": "Dark Chocolate Iced Coffee", "price": 90, "image": "https://lorcoffee.com/cdn/shop/articles/Dark-Chocolate-Ice-Coffee-with-Provocateur-exc.jpg?v=1675806078"},
    ],
    "Desserts": [
        {"name": "Chocolate Brownie", "price": 150, "image": "https://www.spendwithpennies.com/wp-content/uploads/2016/09/Hot-Fudge-Slow-Cooker-Brownies-21.jpg"},
        {"name": "Trifle", "price": 60, "image": "https://media.restless.co.uk/uploads/2021/05/trifle.jpg"},
    ],
}

# Session state variables
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
if "just_added" not in st.session_state:
    st.session_state.just_added = False
if "selected_category" not in st.session_state:
    st.session_state.selected_category = None

# --- Home Page ---
if st.session_state.page == "home":
    st.title("☕ Welcome to Brew & Bite Café")
    st.image("https://www.cafeflorista.com/_next/image?url=%2Fimages%2Fcafe%2FIMG-20240922-WA0015.jpg&w=640&q=75", use_container_width=True)
    st.markdown("### Serving delicious food since 2020 🍽️")
    if st.button("View Menu"):
        st.session_state.page = "menu"
        st.session_state.selected_category = None
        st.rerun()

# --- Menu Page ---
elif st.session_state.page == "menu":
    st.sidebar.title("🛒 Your Cart")

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
                st.rerun()

    st.sidebar.markdown(f"**Total: ₹{total}**")
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
            st.rerun()

    if st.session_state.selected_category is None:
        st.title("📋 Select a Category")
        cat_cols = st.columns(2)
        for i, (category, img_url) in enumerate(category_images.items()):
            with cat_cols[i % 2]:
                if st.button(f"🍽️ {category}", use_container_width=True, key=f"cat_btn_{category}"):
                    st.session_state.selected_category = category
                    st.rerun()
                st.image(img_url, width=150)
    else:
        category = st.session_state.selected_category
        st.title(f"📂 {category}")
        if st.button("⬅️ Back to Categories"):
            st.session_state.selected_category = None
            st.rerun()

        cols = st.columns(2)
        for i, item in enumerate(menu[category]):
            with cols[i % 2]:
                st.image(item["image"], width=200)
                st.markdown(f"**{item['name']}**  \n💰 ₹{item['price']}")
                qty_key = "qty_" + item["name"] + category
                if qty_key not in st.session_state:
                    st.session_state[qty_key] = 1
                btn_key = item["name"] + category
                col_minus, col_qty_display, col_plus, col_add = st.columns([1, 2, 1, 3])
                if col_minus.button("➖", key=f"minus_{btn_key}"):
                    if st.session_state[qty_key] > 1:
                        st.session_state[qty_key] -= 1
                col_qty_display.markdown(
                    f"<h5 style='text-align: center; margin-top: 5px'>{st.session_state[qty_key]}</h5>",
                    unsafe_allow_html=True
                )
                if col_plus.button("➕", key=f"plus_{btn_key}"):
                    if st.session_state[qty_key] < 10:
                        st.session_state[qty_key] += 1
                if col_add.button(f"Add to Cart - {item['name']}", key=btn_key):
                    st.session_state.cart.append({**item, "qty": st.session_state[qty_key]})
                    st.session_state.last_added_item = btn_key
                    st.session_state.last_added_qty = st.session_state[qty_key]
                    st.session_state.just_added = True
                    st.rerun()
                if st.session_state.last_added_item == btn_key and st.session_state.just_added:
                    st.markdown(
                        f"""
                        <div style="background-color: white; color: green; padding: 5px;
                            border-radius: 9px; border: 1px solid green; margin-top: 5px;
                            font-weight: bold; margin-bottom: 15px; text-align: center;">
                            ✅ Added {st.session_state.last_added_qty} x {item['name']} to cart
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    st.session_state.just_added = False

    if st.button("⬅️ Back to Home"):
        st.session_state.page = "home"
        st.rerun()

# --- Checkout Page ---
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
        st.markdown(
            """
            <div style="background-color: white; color: green; padding: 8px;
                border-radius: 8px; border: 2px solid green; font-weight: bold;
                text-align: center; margin-bottom: 15px;">
                🎉 Order placed successfully!
            </div>
            """,
            unsafe_allow_html=True
        )
        time.sleep(2)
        st.session_state.cart.clear()
        st.session_state.page = "menu"
        st.session_state.selected_category = None
        st.rerun()

    if st.button("⬅️ Modify Cart"):
        st.session_state.page = "menu"
        st.rerun()
