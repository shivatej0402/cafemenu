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
        {"name": "Paneer Tikka", "price": 150, "image": "https://carveyourcraving.com/wp-content/uploads/2021/10/paneer-tikka-skewers.jpg"},
        {"name": "Chicken Lollipop", "price": 160, "image": "https://www.bradleysmoker.com/cdn/shop/files/Screen-Shot-2021-08-19-at-11_26_55-AM.png?v=6727898055398431908"},
        {"name": "Hara Bhara Kebab", "price": 130, "image": "https://rumkisgoldenspoon.com/wp-content/uploads/2023/11/Hara-bhara-kabab.jpg"},
        {"name": "Cheese Balls", "price": 140, "image": "https://www.homecookingadventure.com/wp-content/uploads/2023/11/Crispy-Cheese-Balls-main1.webp"},
        {"name": "Corn Cheese Nuggets", "price": 120, "image": "https://www.greenchickchop.in/cdn/shop/files/CheeseCornNuggets_1__result_grande.webp?v=1682661909"},
        {"name": "Onion Rings", "price": 90, "image": "https://media.istockphoto.com/id/451682899/photo/homemade-crunchy-fried-onion-rings.jpg?s=612x612&w=0&k=20&c=G-lrdrU2t_LDBqL1Ds2ZwyWHnx-q4jyykB8DX9G9c2E="},
        {"name": "Garlic Bread", "price": 110, "image": "https://t4.ftcdn.net/jpg/03/19/22/35/360_F_319223572_ILWIWBuhaeyTzGPLQ0rJCVtBSGOqw864.jpg"},
        {"name": "Stuffed Mushrooms", "price": 150, "image": "https://media.istockphoto.com/id/1410877204/photo/stuffed-mushrooms.jpg?s=612x612&w=0&k=20&c=QBqvGx14n1XD7Q61TJu_IQj65zdy0cRLVmkZp7bQDOk="},
        {"name": "Masala Papad", "price": 60, "image": "https://t4.ftcdn.net/jpg/09/34/65/85/360_F_934658531_7yhFm5BQ6NJ9lieQr9hc31RFqMe1cycQ.jpg"},
        {"name": "Crispy Baby Corn", "price": 145, "image": "https://thatdeliciousdish.com/wp-content/uploads/2019/03/Crispy-babycorn.jpg"},
        {"name": "Tandoori Aloo", "price": 135, "image": "https://www.vegrecipesofindia.com/wp-content/uploads/2016/03/aloo-tikka-recipe-1.jpg"},
        {"name": "Chilli Paneer (Dry)", "price": 150, "image": "https://images.news18.com/webstories/uploads/2024/08/Dry-Paneer-Chilli-2024-08-45a38f3d18e2d75a9488178fc34c6fc2.jpg"},
        {"name": "Egg Pakora", "price": 100, "image": "https://i.pinimg.com/736x/5a/82/84/5a8284b2a01fb1e9b3b9fbe4b6eaad70.jpg"},
        {"name": "Fish Fingers", "price": 180, "image": "https://media.istockphoto.com/id/695111216/photo/fried-fish-sticks.jpg?s=612x612&w=0&k=20&c=9o1_KUqVBClyiXkVbIUgL3mi-9VS2HLRhdH_-5z2mck="},
        {"name": "Aloo Tikki", "price": 90, "image": "https://media.istockphoto.com/id/1204866788/photo/aloo-tikki%C2%A0is-a-popular-snack-across-india-made-using-mashed-potatoes-close-up-in-a-plate.jpg?s=612x612&w=0&k=20&c=uIHS-lep8KBwI_TxWUIgnKt_5s2pyiJPtvYzqc22JjY="},
        {"name": "Mini Samosas", "price": 85, "image": "https://t4.ftcdn.net/jpg/04/29/00/69/360_F_429006990_Qy0OUeK2NHoYcdMMyCjZ0GoxLGXpoZD5.jpg"},
        {"name": "Tandoori Momos", "price": 150, "image": "https://static.vecteezy.com/system/resources/previews/013/754/813/large_2x/tandoori-momo-veg-or-non-veg-in-red-and-cream-sauce-served-with-sauce-nepal-and-tibet-recipe-free-photo.jpg"},
        {"name": "Cheesy Nachos", "price": 135, "image": "https://media.istockphoto.com/id/474048190/photo/nachos-supreme.jpg?s=612x612&w=0&k=20&c=CWnaGAVNGeF8sOF92BuZz7iM_JVBdfgO4TmPNokWcIg="},
    ],
    "Main Course": [
        {"name": "Paneer Butter Masala", "price": 220, "image": "https://www.ruchiskitchen.com/wp-content/uploads/2020/12/Paneer-butter-masala-recipe-3-500x500.jpg"},
        {"name": "Chicken Biryani", "price": 250, "image": "https://j6e2i8c9.delivery.rocketcdn.me/wp-content/uploads/2020/09/Chicken-Biryani-Recipe-01-1.jpg"},
        {"name": "Dal Makhani", "price": 200, "image": "https://media.istockphoto.com/id/1170374719/photo/dal-makhani-at-dark-background.jpg?s=612x612&w=0&k=20&c=49yLaUAE2apakVk2AAiRQimZd98WtSjIQ0hzCzWsmns="},
        {"name": "Butter Naan", "price": 40, "image": "https://media.istockphoto.com/id/1143530040/photo/indian-naan-bread-with-garlic-butter-on-wooden-table.jpg?s=612x612&w=0&k=20&c=71SgbJtnfiHUiud1oGxnhiZsx5nuivWwZt8DlIk8hi0="},
        {"name": "Jeera Rice", "price": 90, "image": "https://www.shutterstock.com/image-photo/cumin-rice-jeera-popular-indian-260nw-1785410987.jpg"},
        {"name": "Shahi Paneer", "price": 230, "image": "https://media.istockphoto.com/id/1665320059/photo/indian-paneer-butter-masala-directly-above-photo-on-white-background.jpg?s=612x612&w=0&k=20&c=j93V2k5YgeGYeVQCvsm-hTmC2vGJX1Rj32AmqxTnAzw="},
        {"name": "Veg Pulao", "price": 150, "image": "https://thumbs.dreamstime.com/b/fragrant-veg-pulao-bliss-colorful-rice-fresh-veggies-bowl-aromatic-vegetable-pulao-india-colorful-veggies-372269437.jpg"},
        {"name": "Kadai Chicken", "price": 240, "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIHzBQ97iunLJNFiP_rIIiMBwOfcwnawtWQA&s"},
        {"name": "Chole Bhature", "price": 180, "image": "https://media.istockphoto.com/id/1321061416/photo/chickpeas-masala-and-bhatura-or-puri-garnished-with-fresh-green-coriander-and-ingredients.jpg?s=612x612&w=0&k=20&c=CH7Eyy31a2F9BlzkLmvcqLDm6V9qJSdJ37N-gphrx0M="},
        {"name": "Egg Curry", "price": 190, "image": "https://www.shutterstock.com/image-photo/south-indian-style-egg-curry-260nw-1548758192.jpg"},
        {"name": "Matar Paneer", "price": 210, "image": "https://www.shutterstock.com/image-photo/matar-paneer-curry-recipe-made-260nw-1250565685.jpg"},
        {"name": "Chicken Curry", "price": 230, "image": "https://img.freepik.com/premium-photo/top-view-indian-style-chicken-curry-masala-chicken-curry-bowl_198067-494092.jpg"},
        {"name": "Rajma Chawal", "price": 160, "image": "https://media.istockphoto.com/id/1310123941/photo/rajma-chawal-an-indian-food.jpg?s=612x612&w=0&k=20&c=xKpoTWgir39Hf1MFrVnurSY_Sv8izVHNLB3_Iqmserw="},
        {"name": "Tandoori Roti", "price": 25, "image": "https://inredberry.com/wp-content/uploads/2023/10/Tandoori-Roti.png"},
        {"name": "Veg Kofta Curry", "price": 210, "image": "https://maharajaroyaldining.com/wp-content/uploads/2024/03/VKC-1.webp"},
        {"name": "Bhindi Masala", "price": 170, "image": "https://thegreatgujarat.com/wp-content/uploads/2024/06/punjabi_bhindi_masala_gravy_featured.jpg"},
        {"name": "Fish Curry", "price": 250, "image": "https://media.istockphoto.com/id/1295772372/photo/macher-jhol-in-black-bowl-on-dark-slate-table-top-indian-cuisine-bengali-fish-curry-asian.jpg?s=612x612&w=0&k=20&c=GnOAAcTPI5cRAbKLcA9-riRnmDEy1EAtn4LJwx1cmWo="},
        {"name": "Veg Thali", "price": 280, "image": "https://media.istockphoto.com/id/1158623408/photo/indian-hindu-veg-thali-food-platter-selective-focus.jpg?s=612x612&w=0&k=20&c=MOm3sfIfL22URV6juSCxpA3yfr4O63yJUV5vitufR7Y="},
        {"name": "Chicken Thali", "price": 320, "image": "https://b.zmtcdn.com/data/dish_photos/1c1/d7e7e1b02ccc334cd86b1dff43dea1c1.png"},
        {"name": "Hyderabadi Biryani", "price": 260, "image": "https://t4.ftcdn.net/jpg/12/98/67/47/360_F_1298674783_yP6ywrYg8DOm4mTdF5iz0pK8LVBpiDv2.jpg"},
    ],
    "smoothies": [
        {"name": "Mango Smoothie", "price": 80, "image": "https://vaya.in/recipes/wp-content/uploads/2017/09/Mango-Smoothie_1-1.jpg"},
        {"name": "Dark Chocolate Iced Coffee", "price": 90, "image": "https://lorcoffee.com/cdn/shop/articles/Dark-Chocolate-Ice-Coffee-with-Provocateur-exc.jpg"},
        {"name": "Strawberry Banana", "price": 85, "image": "https://gimmedelicious.com/wp-content/uploads/2024/08/Strawberry-Banana-Smoothie-SQ-500x500.jpg"},
        {"name": "Blueberry Oat", "price": 95, "image": "https://www.proteincakery.com/wp-content/uploads/2023/11/blueberry-muffin-protein-shake-sq-2.jpg"},
        {"name": "Avocado Green", "price": 100, "image": "https://cdn.foodfaithfitness.com/uploads/2024/03/Avocado-Smoothie-A_Avocado-Smoothie_Featured_3.jpg"},
        {"name": "Pineapple Mint", "price": 80, "image": "https://static.vecteezy.com/system/resources/previews/055/685/096/non_2x/fresh-tropical-pineapple-mint-smoothie-for-refreshing-summer-indulgence-photo.jpg"},
        {"name": "Peach Yogurt", "price": 85, "image": "https://monin.in/cdn/shop/files/1b_800x.jpg?v=1731669607"},
        {"name": "Chocolate Banana", "price": 90, "image": "https://www.ambitiouskitchen.com/wp-content/uploads/fly-images/52949/Chocolate-Peanut-Butter-Banana-Smoothie-5-500x375-c.jpg"},
        {"name": "Coconut Mango", "price": 95, "image": "https://mixop.net/wp-content/uploads/136A3355-735x1103.jpg"},
        {"name": "Mixed Berry", "price": 100, "image": "https://www.houstonfoodbank.org/wp-content/uploads/2024/03/BerrySmoothie.jpg"},
        {"name": "Kiwi Spinach", "price": 90, "image": "https://thumbs.dreamstime.com/b/green-smoothie-kiwi-spinach-mason-jar-dark-background-fresh-natural-drink-349387920.jpg"},
        {"name": "Apple Cinnamon", "price": 85, "image": "https://nyssaskitchen.com/wp-content/uploads/2019/11/Cinnamon-Apple-Smoothie-4-of-31.jpg"},
        {"name": "Dates Almond", "price": 95, "image": "https://nadialim.com/wp-content/uploads/2020/09/Banana-date-and-nut-smoothie_square.jpg"},
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
