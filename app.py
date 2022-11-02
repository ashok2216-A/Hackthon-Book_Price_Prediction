# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route("/")
# def home():
#      return "Hello World! My name is ashok"
#      # return render_template('templates\index.html')

# if __name__ == "__main__":
#     app.run(debug=True)

import streamlit as st



age1 = st.slider('How old are you?', 0, 5, 0)
st.write("You Selected", age1, 'Star')

age2 = st.slider('How old are you?', 0, 1000, 0)
st.write("I'm ", age2, 'years old')

age3 = st.slider('How old are you?', 0, 1302, 2500)
st.write("I'm ", age3, 'years old')

age4 = st.slider('How old are you?', 0, 2130, 215)
st.write("I'm ", age4, 'years old')

age5 = st.slider('How old are you?', 0, 6030, 2025)
st.write("I'm ", age5, 'years old')

