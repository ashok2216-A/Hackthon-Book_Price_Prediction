from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
     return "Hello World! My name is ashok kumar"
#      return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

