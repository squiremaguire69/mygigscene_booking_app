import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'mygigscene'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/')
@app.route('/gig_listing')
def gig_listing():
    return render_template('gig_listing.html', gig=mongo.db.gig_listing.find())
    
@app.route('/get_artists')
def get_artists():
    return render_template('artists.html', artists=mongo.db.artist.find())
    
@app.route('/add_artist')
def add_artist():
    return render_template('add_artist.html', 
    price_range=mongo.db.budget.find(),
    genre=mongo.db.genre.find())
    
@app.route('/insert_artist', methods=['POST'])
def insert_artist():
    artists = mongo.db.artist
    artists.insert_one(request.form.to_dict())
    return redirect(url_for('get_artists'))
    
@app.route('/get_venues')
def get_venues():
    return render_template('venues.html', venues=mongo.db.venue.find())

@app.route('/add_venue')
def add_venue():
    return render_template('add_venue.html', 
    town_name=mongo.db.town_name.find(),
    price_range=mongo.db.budget.find(),
    genre=mongo.db.genre.find())
    
    
@app.route('/insert_venue', methods=['POST'])
def insert_venue():
    venues = mongo.db.venue
    venues.insert_one(request.form.to_dict())
    return redirect(url_for('get_venues'))
    
@app.route('/about_us')
def about_us():
    return render_template('about_us')
    
@app.route('/contact_us')
def contact_us():
    return render_template('contact.html')
    
#Filter Methods

@app.route('/select_budget',methods=['POST'])
def select_budget():
    return render_template('artists.html')
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

