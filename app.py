# Leon Magbanua
# HCI Project: Butcher Sanity
# CS 420 - Human Computer Interaction

#app.py
#Primary application management performed here
#Routes are listed, and most non-static, interactivity is coded here

from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

#Routes for interactive pages
@app.route("/", methods = ['GET', 'POST'])
def homepage(): #The homepage
    return render_template('homepage.html')

@app.route("/home", methods = ['GET', 'POST'])
def home(): #The homepage
    return render_template('homepage.html')

@app.route("/searchPage")
def search_page():  #Search function
    return render_template('searchPage.html')

@app.route("/loginPage")
def login_page():   #Potential login
    return render_template('meatCatalog.html')

@app.route("/meatCatalog")
def meat_catalog():
    return render_template('meatCatalog.html')

@app.route("/shoppingCart")
def chopping_cart():
    return render_template('shoppingCart.html')

@app.route("/sirloinPage")
def sirloinPage():
    return render_template('sirloinInfo.html')

#Routes for information pages



app.run(debug=True, port=8090)