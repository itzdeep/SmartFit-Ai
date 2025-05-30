import streamlit as st
import random

# --- Page Config ---
st.set_page_config(page_title="SmartFit AI", page_icon="🏋️", layout="centered")

# --- Initial Header ---
st.markdown("""
    <div style='text-align: center; padding: 20px 0;'>
        <h2 style='color: #0F4C81;'>Welcome to SmartFit AI</h2>
        <p style='font-size: 18px; color: #1f2f56;'>Your journey to a healthier, stronger you starts here.</p>
    </div>
""", unsafe_allow_html=True)

# --- Custom CSS Styling ---
st.markdown("""
    <style>
        .main {
            background-color: #f0f9ff;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: 8px;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #0F4C81;
        }
        .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>div {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 10px;
        }
        .block-container {
            padding-top: 2rem;
        }
        label, .stMultiSelect label {
            color: #1f2f56;
            font-weight: 600;
        }

        .hero-section {
            background: linear-gradient(to right, rgba(46,139,87,0.85), rgba(0,100,0,0.85)),
                        url('https://images.unsplash.com/photo-1558611848-73f7eb4001a1?fit=crop&w=1350&q=80');
            background-size: cover;
            background-position: center;
            padding: 50px 30px;
            border-radius: 12px;
            color: white;
            margin-bottom: 50px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("""
    <div class="hero-section">
        <h1 style='text-align: center;'>SmartFit AI 💪</h1>
        <h3 style='text-align: center;'>Transform your health with a personalised plan powered by machine learning</h3>
        <p style='text-align: center; font-size: 18px;'>Whether you want to lose fat, build muscle, or simply feel better – we create a plan that fits you, not the other way around.</p>
    </div>
""", unsafe_allow_html=True)

# --- Spacer ---
st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

# --- User Input Section ---
st.markdown("""
    <div style='background-color: #dceeff; padding: 25px; border-radius: 12px;'>
        <h3 style='color: #0F4C81;'>🔍 Enter Your Personal Details</h3>
""", unsafe_allow_html=True)

name = st.text_input("👤 Name")
age = st.number_input("🎂 Age", min_value=10, max_value=100, step=1)
gender = st.selectbox("🛋 Gender", ["Male", "Female", "Other"])
height = st.number_input("📏 Height (in cm)", min_value=100, max_value=250)
weight = st.number_input("⚖️ Weight (in kg)", min_value=30, max_value=200)
activity_level = st.selectbox("🏃 Activity Level", ["Sedentary", "Lightly Active", "Active", "Very Active"])
goal = st.selectbox("🎯 Fitness Goal", ["Lose Weight", "Gain Muscle", "Stay Fit"])
allergies = st.multiselect(
    "⚠️ Allergies (Select if any)",
    ["Lactose", "Gluten", "Nuts", "Soy", "None"]
)

st.markdown("</div>", unsafe_allow_html=True)

# --- Generate Plan Button ---
if st.button("💡 Generate My Plan"):
    st.header("📋 Your AI-Generated Fitness & Diet Plan")

    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    activity_multiplier = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Active": 1.55,
        "Very Active": 1.725
    }

    calorie_goal = int(bmr * activity_multiplier[activity_level])

    if goal == "Lose Weight":
        calorie_goal -= 500
    elif goal == "Gain Muscle":
        calorie_goal += 300

    diet = []
    if "Lactose" in allergies:
        diet.append("🚫 Avoid dairy. Use almond or oat milk.")
    if "Gluten" in allergies:
        diet.append("🚫 Avoid bread, pasta. Use gluten-free grains like quinoa or rice.")
    if "Nuts" in allergies:
        diet.append("🚫 Avoid peanut butter, almonds. Use sunflower seed butter.")
    if not diet:
        diet.append("✅ No major allergies. Eat a balanced diet with protein, carbs, and healthy fats.")

    if goal == "Lose Weight":
        meals = 3
        foods = ["Grilled chicken", "Steamed vegetables", "Boiled eggs", "Oats", "Fruits"]
        week_plan = ["Oats & banana", "Grilled chicken & veggies", "Boiled egg & salad", "Soup & toast", "Fruit bowl", "Rice & dal", "Yoghurt & seeds"]
        routine = "🏃 30 mins cardio + 💪 15 mins strength training + 🧘 stretching"
    elif goal == "Gain Muscle":
        meals = 5
        foods = ["Chicken breast", "Paneer", "Eggs", "Protein shakes", "Brown rice", "Sweet potato"]
        week_plan = ["Eggs & toast", "Protein shake & banana", "Chicken rice bowl", "Paneer curry & rice", "Sweet potato mash", "Oats & milk", "Cottage cheese salad"]
        routine = "🏋️ 45 mins weight training + 🔥 15 mins core workout"
    else:
        meals = 4
        foods = ["Whole grains", "Vegetables", "Fruits", "Lean meat", "Dairy", "Nuts (if not allergic)"]
        week_plan = ["Whole grain toast", "Fruit smoothie", "Mixed veg curry", "Dhalia & salad", "Egg sandwich", "Rice & veggies", "Milk & fruits"]
        routine = "🚶 30 mins walk/jog + 🤺 15 mins bodyweight exercises"

    water_intake_litres = round(weight * 0.033, 1)

    health_quotes = [
        "Every day is another chance to get stronger.",
        "Take care of your body. It's the only place you have to live.",
        "Small progress is still progress.",
        "Discipline is choosing between what you want now and what you want most."
    ]

    st.subheader(f"👤 Hello, {name}!")
    st.markdown(f"**🎯 Daily Calorie Goal:** <span style='color:#e67e22;font-size:20px;'>{calorie_goal} kcal</span>", unsafe_allow_html=True)

    st.subheader("🥗 Diet Suggestions:")
    for item in diet:
        st.markdown(f"- {item}")

    st.subheader("🍽️ Meals & Recommended Foods:")
    st.markdown(f"**Suggested Number of Meals:** <span style='color:#27ae60;'>{meals} per day</span>", unsafe_allow_html=True)
    st.markdown("**Recommended Foods:**")
    for food in foods:
        st.markdown(f"- 🍽️ {food}")

    # --- New Feature: Weekly Diet Plan ---
    st.subheader("🍜 Weekly Diet Plan (Sample)")
    for i, day in enumerate(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]):
        st.markdown(f"**{day}:** {week_plan[i]}")

    st.subheader("🚳 Water Intake Reminder")
    st.markdown(f"You should drink about **{water_intake_litres} litres** of water per day.")

    st.subheader("📚 Daily Health Motivation")
    st.info(random.choice(health_quotes))

    st.subheader("🏃 Exercise Routine:")
    st.markdown(f"{routine}")

    st.success("✅ This is a basic plan. You can enhance it further by training a model with real data.")

# --- Footer ---
st.markdown("""
    <hr style='margin-top: 50px;'>
    <div style='text-align: center; color: #6c757d; font-size: 14px;'>
        <p>© 2025 SmartFit AI | All rights reserved.</p>
        <p>Made with 💚 for your fitness journey</p>
        <p>📷 Follow Admin <a href='https://www.instagram.com/_wtfrav/' target='_blank' style='color:#0F4C81; text-decoration: none; font-weight: 600;'>Instagram</a></p>
    </div>
""", unsafe_allow_html=True)
