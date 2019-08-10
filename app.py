import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'mygigscene'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

# Homepage routing
@app.route('/')
@app.route('/gig_listing')
def gig_listing():
    return render_template('gig_listing.html', 
                            gig = mongo.db.gig_listing.find(),
                            venue = mongo.db.venue.find(),
                            artist = mongo.db.artist.find())

# Form for adding a new gig to the database
@app.route('/add_gig')
def add_gig():
    return render_template('add_gig.html')
    

# Function to insert the details of the new gig into the database   
@app.route('/insert_gig')
def insert_gig():
    gig = mongo.db.gig_listing
    gig.insert({
        'venue_name': request.form.get('venue.name'),
        'town_name': request.form.get('town_name'),
        'artist_name': request.form.get('artist_name'),
        'genre_category': request.form.getlist('genre_category'),
        'gig_date': request.form.get('gig_date'),
        'gig_time': request.form.get('gig_time'),
        'gig_info': request.form.get('gig_info')
    })


# Routing for Artists page    
@app.route('/get_artists')
def get_artists():
    return render_template('artists.html', artists=mongo.db.artist.find())


# Form for adding a new Artist    
@app.route('/add_artist')
def add_artist():
    return render_template('add_artist.html', 
    price_range=mongo.db.budget.find(),
    genre=mongo.db.genre.find())


# Function to insert new Artist details into the database    
@app.route('/insert_artist', methods=['POST'])
def insert_artist():
    artists = mongo.db.artist
    artists.insert_one({
        'artist_name': request.form.get('artist_name'),
        'genre_category': request.form.getlist('genre_category'),
        'budget_range': request.form.get('budget_range'),
        'profile_description': request.form.get('profile_description'),
        'profile_image': request.form.get('profile_image'),
        'active': request.form.get('active')
     })
    return redirect(url_for('get_artists'))


# Routing to show gig listings for selected artist    
@app.route('/gig_listing_artist')
def gig_listing_artist():
    return render_template('gig_listing_artist.html')


# Routing to Venues page    
@app.route('/get_venues')
def get_venues():
    return render_template('venues.html', venues=mongo.db.venue.find())


# Form for adding a new Venue
@app.route('/add_venue')
def add_venue():
    return render_template('add_venue.html', 
    town_name=mongo.db.town_name.find(),
    price_range=mongo.db.budget.find(),
    genre=mongo.db.genre.find())
    

# Function to insert the new Venue details into the database    
@app.route('/insert_venue', methods=['POST'])
def insert_venue():
    venues = mongo.db.venue
    venues.insert({
        'venue_name': request.form.get('venue_name'),
        'town_name': request.form.get('town_name'),
        'profile_description': request.form.get('profile_description'),
        'genre_category': request.form.getlist('genre_category'),
        'budget_range': request.form.get('budget_range'),
        'profile_image': request.form.get('profile_image'),
        'active': request.form.get('active')
    } )
    return redirect(url_for('get_venues'))


# Routing for About Us Page    
@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


# Routing for contact us page    
@app.route('/contact_us')
def contact_us():
    return render_template('contact.html')
    
    
#Filter Section Functions

@app.route('/select_budget',methods=['POST'])
def select_budget():
    return render_template('artists.html')
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

