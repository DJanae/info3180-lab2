from app import app
from flask import render_template
from datetime import datetime

# Sample data for the user profile
user_profile = {
    'photo': 'https://via.placeholder.com/150',
    'full_name': 'D\'Janae Patterson',
    'username': 'djanaepat',
    'location': 'Kingston, Jamaica',
    'join_date': datetime(2024, 2, 19),  # Using datetime object for join date
    'bio': 'I am smart and intelligent and I love web design.',
    'num_posts': 10,
    'num_followers': 100,
    'num_following': 50,
}

def format_date_joined(date):
    """Format the date as Month, Year (e.g. Feb, 2021)."""
    return date.strftime('%b, %Y')

# New route and view function for the profile page
@app.route('/profile/')
def profile():
    """Render the user's profile page."""
    user_profile['join_date'] = format_date_joined(user_profile['join_date'])
    return render_template('profile.html', user=user_profile)

# Existing routes and view functions
@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
