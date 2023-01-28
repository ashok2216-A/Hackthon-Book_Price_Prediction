# # from flask import Flask, render_template
# # app = Flask(__name__)

# # @app.route("/")
# # def home():
# #      return "Hello World! My name is ashok"
# #      # return render_template('templates\index.html')

# # if __name__ == "__main__":
# #     app.run(debug=True)

# import streamlit as st
# import pickle

# st.title("Book Price Prediction 🚀")
# #Reviews
# Reviews = st.slider('Select Reviews', 0, 5, 0)
# st.write("You Selected", Reviews, 'Star')

# #Edition Name
# EditionName = st.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone'))

# st.write('You selected:', EditionName)

# #Ratings
# Ratings = st.slider('Select Ratings', 0, 1000, 0)
# st.write("You Selected", Ratings, 'Ratings')

# #Genre
# Genre = st.selectbox(
#     'How would you like to be contacted?',
#     ('Ema5il', 'Hom5e phone', 'Mob5ile phone'))

# st.write('You selected:', Genre)


# #BookCategory
# Bookcategory = st.radio(
#     "What's your favorite movie genre",
#     (
# 'Action & Adventure',                     
# 'Arts, Film & Photography',                 
# 'Biographies, Diaries & True Accounts',   
# 'Comics & Mangas',                    
# 'Computing, Internet & Digital Media',     
# 'Crime, Thriller & Mystery',                
# 'Humour',                                   
# 'Language, Linguistics & Writing',          
# 'Politics',                                 
# 'Romance',                                  
# 'Sports'))

# if Bookcategory == 'Action & Adventure':
#     st.write('You selected Action & Adventure.')
# elif Bookcategory == 'Arts, Film & Photography':
#     st.write('You selected Arts, Film & Photography.')
# elif Bookcategory == 'Biographies, Diaries & True Accounts':
#     st.write('You selected Biographies, Diaries & True Accounts.')
# elif Bookcategory == 'Comics & Mangas':
#     st.write('You selected Comics & Mangas.')
# elif Bookcategory == 'Computing, Internet & Digital Media':
#     st.write('You selected Computing, Internet & Digital Media.')
# elif Bookcategory == 'Crime, Thriller & Mystery':
#     st.write('You selected Crime, Thriller & Mystery.')
# elif Bookcategory == 'Humour':
#     st.write('You selected Humour.')
# elif Bookcategory == 'Language, Linguistics & Writing':
#     st.write('You selected Language, Linguistics & Writing.')
# elif Bookcategory == 'Politics':
#     st.write('You selected Politics.')
# elif Bookcategory == 'Romance':
#     st.write('You selected Romance.')
# elif Bookcategory == 'Sports':
#     st.write('You selected Sports.')

# else:
#     st.write("You didn't select any items.")

# with open("pickle_model.pkl", "wb") as file:
#     pickle.dump(treereg_pred, file)


# pickling the model
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

# pickle_out = open("pickle_model.pkl", "wb")
# pickle.dump(treereg_pred, pickle_out)
# pickle_out.close()




# loading in the model to predict on the data
pickle_in = open('pickle_model.pkl', 'rb')
classifier = pickle.load(pickle_in)

def welcome():
	return 'welcome all'

# defining the function which will make the prediction using
# the data which the user inputs
def prediction(Reviews, Ratings, Genre, BookCategory, Edition_Name):

	prediction = classifier.predict(
		[[Reviews, Ratings, Genre, BookCategory, Edition_Name]])
	print(prediction)
	return prediction
	

# this is the main function in which we define our webpage
def main():
	# giving the webpage a title
	st.title("Book Price Prediction")
	
	# here we define some of the front end elements of the web page like
	# the font and background color, the padding and the text to be displayed
	html_temp = """
	<div style ="background-color:yellow;padding:13px">
	<h1 style ="color:black;text-align:center;">Streamlit Iris Flower Classifier ML App </h1>
	</div>
	"""
	
	# this line allows us to display the front end aspects we have
	# defined in the above code
	st.markdown(html_temp, unsafe_allow_html = True)
    
    Reviews = st.slider('Select Reviews', 0, 5, 0)
    st.write("You Selected", Reviews, 'Star')
	EditionName = st.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))
	petal_length = st.text_input("Petal Length", "Type Here")
	petal_width = st.text_input("Petal Width", "Type Here")
	result =""
	
	# the below line ensures that when the button called 'Predict' is clicked,
	# the prediction function defined above is called to make the prediction
	# and store it in the variable result
	if st.button("Predict"):
		result = prediction(sepal_length, sepal_width, petal_length, petal_width)
	st.success('The output is {}'.format(result))
	
if __name__=='__main__':
	main()
