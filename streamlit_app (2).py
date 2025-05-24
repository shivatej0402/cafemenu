import streamlit as st
import time

st.set_page_config(page_title="Cafe Menu", layout="wide")

# Background styling
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

# Category images
category_images = {
    "Starters": "https://c.ndtvimg.com/2023-08/sfc3gcoo_chicken-snack_625x300_21_August_23.jpg?im=FaceCrop,algorithm=dnn,width=1200,height=675",
    "Main Course": "https://cbx-prod.b-cdn.net/COLOURBOX60103276.jpg?width=800&height=800&quality=70",
    "smoothies": "https://thumbs.dreamstime.com/b/colorful-smoothies-glass-jars-fresh-fruit-black-surface-colorful-smoothies-glass-jars-fresh-fruit-black-339067901.jpg",
    "Desserts": "https://cdn.hswstatic.com/gif/desserts-update.jpg",
}

menu = {
    "Starters": [
        {"name": "Veg Spring Roll", "price": 120, "image": "https://www.womansworld.com/wp-content/uploads/2023/09/airfryer13.jpg"},
        {"name": "French Fries", "price": 100, "image": "https://www.cuisinart.com/dw/image/v2/ABAF_PRD/on/demandware.static/-/Sites-us-cuisinart-sfra-Library/default/dw3a257599/images/recipe-Images/french-fries-airfryer-recipe.jpg?sw=1200&sh=1200&sm=fit"},
        {"name": "Paneer Tikka", "price": 150, "image": "https://www.vegrecipesofindia.com/wp-content/uploads/2021/03/paneer-tikka-1.jpg"},
        {"name": "Chicken Lollipop", "price": 160, "image": "https://www.indianhealthyrecipes.com/wp-content/uploads/2021/07/chicken-lollipop.jpg"},
        {"name": "Hara Bhara Kebab", "price": 130, "image": "https://www.cookingcarnival.com/wp-content/uploads/2020/07/Hara-Bhara-Kabab-1.jpg"},
        {"name": "Cheese Balls", "price": 140, "image": "https://www.cookclickndevour.com/wp-content/uploads/2017/06/cheese-balls-recipe-2.jpg"},
        {"name": "Corn Cheese Nuggets", "price": 120, "image": "https://i.ytimg.com/vi/YcB3T6T-0ks/maxresdefault.jpg"},
        {"name": "Onion Rings", "price": 90, "image": "https://www.cookingclassy.com/wp-content/uploads/2022/05/onion-rings-10.jpg"},
        {"name": "Garlic Bread", "price": 110, "image": "https://www.simplyrecipes.com/thmb/dNHsQZbo1eWWCeaLFiitBIr8Eaw=/2000x1333/filters:fill(auto,1)/Simply-Recipes-Garlic-Bread-LEAD-04-4a403d4687da4384b1c1774f9919b6b3.jpg"},
        {"name": "Stuffed Mushrooms", "price": 150, "image": "https://www.loveandlemons.com/wp-content/uploads/2020/12/stuffed-mushrooms-580x629.jpg"},
        {"name": "Masala Papad", "price": 60, "image": "https://hebbarskitchen.com/wp-content/uploads/2021/04/masala-papad-recipe-crispy-masala-papadum.jpg"},
        {"name": "Crispy Baby Corn", "price": 145, "image": "https://www.archanaskitchen.com/images/archanaskitchen/1-Author/Shaheen_Ali/Crispy_Baby_Corn.jpg"},
        {"name": "Tandoori Aloo", "price": 135, "image": "https://static.toiimg.com/photo/72590235.cms"},
        {"name": "Chilli Paneer (Dry)", "price": 150, "image": "https://www.cubesnjuliennes.com/wp-content/uploads/2020/11/Chilli-Paneer-Dry-Recipe.jpg"},
        {"name": "Egg Pakora", "price": 100, "image": "https://www.whiskaffair.com/wp-content/uploads/2018/07/Egg-Pakora-2-3.jpg"},
        {"name": "Fish Fingers", "price": 180, "image": "https://www.indianhealthyrecipes.com/wp-content/uploads/2021/03/fish-fingers.jpg"},
        {"name": "Aloo Tikki", "price": 90, "image": "https://www.vegrecipesofindia.com/wp-content/uploads/2014/04/aloo-tikki-recipe-1a.jpg"},
        {"name": "Mini Samosas", "price": 85, "image": "https://www.cookwithmanali.com/wp-content/uploads/2021/06/Mini-Samosa.jpg"},
        {"name": "Tandoori Momos", "price": 150, "image": "https://img-global.cpcdn.com/recipes/062e6b190e2695ae/1200x630cq70/photo.jpg"},
        {"name": "Cheesy Nachos", "price": 135, "image": "https://www.indianhealthyrecipes.com/wp-content/uploads/2021/12/nachos-recipe.jpg"},
    ],
    "Main Course": [
        {"name": "Paneer Butter Masala", "price": 220, "image": "https://www.ruchiskitchen.com/wp-content/uploads/2020/12/Paneer-butter-masala-recipe-3-500x500.jpg"},
        {"name": "Chicken Biryani", "price": 250, "image": "https://j6e2i8c9.delivery.rocketcdn.me/wp-content/uploads/2020/09/Chicken-Biryani-Recipe-01-1.jpg"},
        {"name": "Dal Makhani", "price": 200, "image": "https://www.whiskaffair.com/wp-content/uploads/2020/07/Dal-Makhani-2-3.jpg"},
        {"name": "Butter Naan", "price": 40, "image": "https://www.vegrecipesofindia.com/wp-content/uploads/2021/07/butter-naan-recipe-1.jpg"},
        {"name": "Jeera Rice", "price": 90, "image": "https://www.whiskaffair.com/wp-content/uploads/2020/08/Jeera-Rice-2-3.jpg"},
        {"name": "Shahi Paneer", "price": 230, "image": "https://www.vegrecipesofindia.com/wp-content/uploads/2021/04/shahi-paneer-1.jpg"},
        {"name": "Veg Pulao", "price": 150, "image": "https://www.indianhealthyrecipes.com/wp-content/uploads/2021/05/vegetable-pulao-recipe.jpg"},
        {"name": "Kadai Chicken", "price": 240, "image": "https://www.cubesnjuliennes.com/wp-content/uploads/2020/12/Kadai-Chicken-Recipe.jpg"},
        {"name": "Chole Bhature", "price": 180, "image": "https://www.cookwithmanali.com/wp-content/uploads/2020/05/Chole-Bhature.jpg"},
        {"name": "Egg Curry", "price": 190, "image": "https://www.indianhealthyrecipes.com/wp-content/uploads/2021/03/egg-curry-recipe.jpg"},
        {"name": "Matar Paneer", "price": 210, "image": "https://www.whiskaffair.com/wp-content/uploads/2020/06/Matar-Paneer-2-3.jpg"},
        {"name": "Chicken Curry", "price": 230, "image": "https://www.cookclickndevour.com/wp-content/uploads/2021/06/easy-chicken-curry.jpg"},
        {"name": "Rajma Chawal", "price": 160, "image": "https://www.vegrecipesofindia.com/wp-content/uploads/2021/07/rajma-recipe-1.jpg"},
        {"name": "Tandoori Roti", "price": 25, "image": "https://www.indianhealthyrecipes.com/wp-content/uploads/2021/12/tandoori-roti.jpg"},
        {"name": "Veg Kofta Curry", "price": 210, "image": "https://www.whiskaffair.com/wp-content/uploads/2020/03/Veg-Kofta-Curry-2-3.jpg"},
        {"name": "Bhindi Masala", "price": 170, "image": "https://www.indianhealthyrecipes.com/wp-content/uploads/2021/07/bhindi-masala-recipe.jpg"},
        {"name": "Fish Curry", "price": 250, "image": "https://www.cookwithkushi.com/wp-content/uploads/2021/06/fish_curry_recipe_1-scaled.jpg"},
        {"name": "Veg Thali", "price": 280, "image": "https://www.whiskaffair.com/wp-content/uploads/2021/02/Veg-Thali-2-3.jpg"},
        {"name": "Chicken Thali", "price": 320, "image": "https://img.onmanorama.com/content/dam/mm/en/food/recipe/images/2020/9/17/thali.jpg"},
        {"name": "Hyderabadi Biryani", "price": 260, "image": "https://www.cookwithmanali.com/wp-content/uploads/2020/06/Hyderabadi-Biryani.jpg"},
    ],
    "smoothies": [
        {"name": "Mango Smoothie", "price": 80, "image": "https://vaya.in/recipes/wp-content/uploads/2017/09/Mango-Smoothie_1-1.jpg"},
        {"name": "Dark Chocolate Iced Coffee", "price": 90, "image": "https://lorcoffee.com/cdn/shop/articles/Dark-Chocolate-Ice-Coffee-with-Provocateur-exc.jpg"},
        {"name": "Strawberry Banana", "price": 85, "image": "https://cdn.loveandlemons.com/wp-content/uploads/2021/07/strawberry-banana-smoothie-580x869.jpg"},
        {"name": "Blueberry Oat", "price": 95, "image": "https://www.wellplated.com/wp-content/uploads/2021/06/Blueberry-Oat-Smoothie.jpg"},
        {"name": "Avocado Green", "price": 100, "image": "https://cdn.loveandlemons.com/wp-content/uploads/2021/07/green-smoothie-580x869.jpg"},
        {"name": "Pineapple Mint", "price": 80, "image": "https://www.runningtothekitchen.com/wp-content/uploads/2020/07/pineapple-mint-smoothie-480x480.jpg"},
        {"name": "Peach Yogurt", "price": 85, "image": "https://www.acouplecooks.com/wp-content/uploads/2021/06/Peach-Smoothie-010.jpg"},
        {"name": "Chocolate Banana", "price": 90, "image": "https://www.wellplated.com/wp-content/uploads/2021/06/Chocolate-Banana-Smoothie.jpg"},
        {"name": "Coconut Mango", "price": 95, "image": "https://www.gimmesomeoven.com/wp-content/uploads/2015/07/Coconut-Mango-Smoothie.jpg"},
        {"name": "Mixed Berry", "price": 100, "image": "https://www.acouplecooks.com/wp-content/uploads/2021/01/Berry-Smoothie-015.jpg"},
        {"name": "Kiwi Spinach", "price": 90, "image": "https://simpleveganblog.com/wp-content/uploads/2016/02/Kiwi-Spinach-Smoothie.jpg"},
        {"name": "Apple Cinnamon", "price": 85, "image": "https://www.wellplated.com/wp-content/uploads/2021/06/Apple-Smoothie.jpg"},
        {"name": "Dates Almond", "price": 95, "image": "https://i.ytimg.com/vi/Kf93IG4UNvc/maxresdefault.jpg"},
        {"name": "Orange Carrot", "price": 90, "image": "https://www.blendwithspices.com/wp-content/uploads/2020/02/orange-carrot-smoothie-recipe.jpg"},
        {"name": "Papaya Delight", "price": 80, "image": "https://www.vegrecipesofindia.com/wp-content/uploads/2015/04/papaya-smoothie-1.jpg"},
        {"name": "Lychee Lush", "price": 85, "image": "https://www.sharmispassions.com/wp-content/uploads/2021/05/Lychee-Smoothie6.jpg"},
        {"name": "Chikoo Milk", "price": 80, "image": "https://www.vegrecipesofindia.com/wp-content/uploads/2021/03/chikoo-milkshake-1.jpg"},
        {"name": "Coffee Banana", "price": 90, "image": "https://www.wellplated.com/wp-content/uploads/2021/06/Banana-Coffee-Smoothie.jpg"},
        {"name": "Fig Honey", "price": 95, "image": "https://www.archanaskitchen.com/images/archanaskitchen/1-Author/sibyl_sunitha/Fig_Honey_Smoothie.jpg"},
        {"name": "Watermelon Slush", "price": 70, "image": "https://www.acouplecooks.com/wp-content/uploads/2021/06/Watermelon-Slushie-013.jpg"},
    ],
    "Desserts": [
        {"name": "Chocolate Brownie", "price": 150, "image": "https://www.spendwithpennies.com/wp-content/uploads/2016/09/Hot-Fudge-Slow-Cooker-Brownies-21.jpg"},
        {"name": "Trifle", "price": 60, "image": "https://media.restless.co.uk/uploads/2021/05/trifle.jpg"},
        {"name": "Gulab Jamun", "price": 70, "image": "https://www.vegrecipesofindia.com/wp-content/uploads/2021/04/gulab-jamun-recipe-1.jpg"},
        {"name": "Rasmalai", "price": 90, "image": "https://www.indianhealthyrecipes.com/wp-content/uploads/2021/07/rasmalai.jpg"},
        {"name": "Cheesecake", "price": 120, "image": "https://sallysbakingaddiction.com/wp-content/uploads/2018/05/classic-cheesecake.jpg"},
        {"name": "Cupcake", "price": 60, "image": "https://www.cookingclassy.com/wp-content/uploads/2020/06/vanilla-cupcakes-6.jpg"},
        {"name": "Ice Cream Sundae", "price": 90, "image": "https://www.simplyrecipes.com/thmb/zGJh8Xc3ZUGSPBD8IDvddE3EGpg=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Simply-Recipes-Ice-Cream-Sundae-LEAD-05-96ce9146e3d94ef6a9d2468f071c5d3b.jpg"},
        {"name": "Choco Lava Cake", "price": 100, "image": "https://www.vegrecipesofindia.com/wp-content/uploads/2021/02/molten-lava-cake-1.jpg"},
        {"name": "Fruit Custard", "price": 70, "image": "https://www.vegrecipesofindia.com/wp-content/uploads/2021/04/fruit-custard-recipe-1.jpg"},
        {"name": "Kheer", "price": 80, "image": "https://www.vegrecipesofindia.com/wp-content/uploads/2021/04/rice-kheer-recipe-1.jpg"},
        {"name": "Mango Mousse", "price": 85, "image": "https://www.indianhealthyrecipes.com/wp-content/uploads/2021/06/mango-mousse.jpg"},
        {"name": "Strawberry Panna Cotta", "price": 95, "image": "https://www.lifeloveandsugar.com/wp-content/uploads/2019/01/Strawberry-Panna-Cotta1.jpg"},
        {"name": "Apple Pie", "price": 120, "image": "https://www.simplyrecipes.com/thmb/TPsEKBFxgH9oG9AWUv2qB17S4-M=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Simply-Recipes-Apple-Pie-LEAD-05-5d88a0bc6a7448f2a2c2a4c2e7c510cd.jpg"},
        {"name": "Tiramisu", "price": 130, "image": "https://www.simplyrecipes.com/thmb/2N3W5QUhHXam8PaSSeAnzOlCmCg=/2000x1333/filters:fill(auto,1)/Simply-Recipes-Tiramisu-LEAD-3-4f6a7e6b896b48a296275e9e9e1e91cc.jpg"},
        {"name": "Carrot Halwa", "price": 90, "image": "https://www.indianhealthyrecipes.com/wp-content/uploads/2021/03/gajar-ka-halwa.jpg"},
        {"name": "Dry Fruit Ladoo", "price": 85, "image": "https://www.vegrecipesofindia.com/wp-content/uploads/2021/10/dry-fruit-ladoo-recipe.jpg"},
        {"name": "Kalakand", "price": 95, "image": "https://www.vegrecipesofindia.com/wp-content/uploads/2021/04/kalakand-recipe-1.jpg"},
        {"name": "Chocolate Mousse", "price": 90, "image": "https://sallysbakingaddiction.com/wp-content/uploads/2020/02/dark-chocolate-mousse.jpg"},
        {"name": "Brownie Sundae", "price": 110, "image": "https://www.lifeloveandsugar.com/wp-content/uploads/2019/07/Brownie-Sundae4.jpg"},
        {"name": "Vanilla Pudding", "price": 80, "image": "https://www.simplyrecipes.com/thmb/BOwWg9AUsT2Q1XjX4QzGqYzUwOE=/2000x1333/filters:fill(auto,1)/Simply-Recipes-Vanilla-Pudding-LEAD-1-6e5cc681b88e49ef80f90f7f6a87c1c1.jpg"},
    ],
}
# Initialize session state
for key, default in {
    "page": "home",
    "cart": [],
    "customer_info": {"name": "", "mobile": ""},
    "last_added_item": None,
    "last_added_qty": 0,
    "just_added": False,
    "selected_category": None,
    "order_placed": False,
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

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
                qty_key = f"qty_{item['name']}_{category}"
                if qty_key not in st.session_state:
                    st.session_state[qty_key] = 1

                qty = st.number_input(f"Quantity for {item['name']}", min_value=1, max_value=10, step=1,
                                      key=f"num_input_{qty_key}")

                if st.button(f"Add to Cart", key=f"add_{item['name']}_{category}"):
                    st.session_state.cart.append({**item, "qty": qty})
                    st.session_state.last_added_item = item['name']
                    st.session_state.last_added_qty = qty
                    st.session_state.just_added = True
                    st.rerun()

                if st.session_state.last_added_item == item['name'] and st.session_state.just_added:
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

    # Floating cart that triggers a hidden button
    total_items = sum(item["qty"] for item in grouped_cart.values())
    total_price = sum(item["qty"] * item["price"] for item in grouped_cart.values())
    if total_items > 0:
        st.markdown("""
            <style>
                .floating-cart {
                    position: fixed;
                    bottom: 20px;
                    right: 20px;
                    background-color: #fff5f5;
                    color: #c80000;
                    padding: 15px 20px;
                    border-radius: 15px;
                    box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
                    z-index: 9999;
                    font-weight: bold;
                    font-size: 16px;
                    border: 2px solid #ffcccc;
                    cursor: pointer;
                }
            </style>
            <div class="floating-cart" onclick="document.getElementById('hidden_checkout_btn').click();">
                🛒 """ + f"{total_items} item(s) | ₹{total_price}" + """
            </div>
        """, unsafe_allow_html=True)

        # Hidden button to navigate to checkout
        if st.button("Go to Checkout", key="hidden_checkout_btn"):
            st.session_state.page = "checkout"
            st.rerun()

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
        st.session_state.order_placed = True
        st.rerun()

    if st.button("⬅️ Modify Cart"):
        st.session_state.page = "menu"
        st.rerun()
