# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route("/")
# def home():
#      return "Hello World! My name is ashok"
#      # return render_template('templates\index.html')

# if __name__ == "__main__":
#     app.run(debug=True)

import streamlit as st

st.title("Book Price Prediction 🚀")
#Reviews
Reviews = st.slider('Select Reviews', 0, 5, 0)
st.write("You Selected", Reviews, 'Star')

#Edition Name
EditionName = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', EditionName)

#Ratings
Ratings = st.slider('Select Ratings', 0, 1000, 0)
st.write("You Selected", Ratings, 'Ratings')

#Genre
Genre = st.selectbox(
    'How would you like to be contacted?',
    ('Ema5il', 'Hom5e phone', 'Mob5ile phone'))

st.write('You selected:', Genre)


#BookCategory
Bookcategory = st.radio(
    "What's your favorite movie genre",
    (
'Action & Adventure',                     
'Arts, Film & Photography',                 
'Biographies, Diaries & True Accounts',   
'Comics & Mangas',                    
'Computing, Internet & Digital Media',     
'Crime, Thriller & Mystery',                
'Humour',                                   
'Language, Linguistics & Writing',          
'Politics',                                 
'Romance',                                  
'Sports'))

if Bookcategory == 'Action & Adventure':
    st.write('You selected Action & Adventure.')
elif Bookcategory == 'Arts, Film & Photography':
    st.write('You selected Arts, Film & Photography.')
elif Bookcategory == 'Biographies, Diaries & True Accounts':
    st.write('You selected Biographies, Diaries & True Accounts.')
elif Bookcategory == 'Comics & Mangas':
    st.write('You selected Comics & Mangas.')
elif Bookcategory == 'Computing, Internet & Digital Media':
    st.write('You selected Computing, Internet & Digital Media.')
elif Bookcategory == 'Crime, Thriller & Mystery':
    st.write('You selected Crime, Thriller & Mystery.')
elif Bookcategory == 'Humour':
    st.write('You selected Humour.')
elif Bookcategory == 'Language, Linguistics & Writing':
    st.write('You selected Language, Linguistics & Writing.')
elif Bookcategory == 'Politics':
    st.write('You selected Politics.')
elif Bookcategory == 'Romance':
    st.write('You selected Romance.')
elif Bookcategory == 'Sports':
    st.write('You selected Sports.')

else:
    st.write("You didn't select any items.")

