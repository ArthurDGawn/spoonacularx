import os
x = os.getenv("GEMINI")
import google.generativeai as genai
genai.configure(api_key=x)
model = genai.GenerativeModel('models/gemini-pro')
import streamlit as st
st.title("Recipe and Meal Plan Assistant")

    # Radio button for selecting functionality
choice = st.radio("Choose an option:", ("Generate Recipe", "Create Meal Plan"))

if choice == "Generate Recipe":
        goal = st.selectbox("What is your dietary goal?", ("Muscle Building", "Fitness", "Weight Loss", "General Health"))
        allergies = st.multiselect("Select any allergies (if none, leave blank):", ["Peanuts", "Dairy", "Gluten", "Soy", "Shellfish", "None"])
        restrictions = st.multiselect("Select any dietary restrictions (if none, leave blank):", ["Vegan", "Vegetarian", "Pescatarian", "Keto", "Paleo", "None"])
        if st.button("Generate Recipe"):
            prompt = f"""
            Create a healthy recipe that is suitable for {goal}.
            Avoid ingredients that cause {','.join(allergies) if allergies else 'no'} allergies.
            Follow {','.join(restrictions) if restrictions else 'no'} dietary restrictions.
            """

            response = model.generate_content(prompt)
            st.success("Your recipe is ready!")
            st.write(response.text)
else:
        goal = st.selectbox("What is your dietary goal?", ("Muscle Building", "Fitness", "Weight Loss", "General Health"))
        allergies = st.multiselect("Select any allergies (if none, leave blank):", ["Peanuts", "Dairy", "Gluten", "Soy", "Shellfish", "None"])
        restrictions = st.multiselect("Select any dietary restrictions (if none, leave blank):", ["Vegan", "Vegetarian", "Pescatarian", "Keto", "Paleo", "None"])
        num_meals = st.number_input("Enter the number of meals (default: 3):", min_value=1, max_value=7, value=3)
        if st.button("Create Meal Plan"):
            prompt = f"""
            Create a {num_meals}-meal meal plan that is suitable for {goal}.
            Avoid ingredients that cause {','.join(allergies) if allergies else 'no'} allergies.
            Follow {','.join(restrictions) if restrictions else 'no'} dietary restrictions.
            Include a variety of nutrients and ensure balanced portions.
            """

            response = model.generate_content(prompt)
            st.success("Your meal plan is ready!")
            st.write(response.text)



