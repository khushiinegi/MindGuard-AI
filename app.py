from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, redirect, url_for, request, make_response
import datetime

# Create the Flask application instance
app = Flask(__name__)

# These global variables are provided by the Canvas environment.
# For local development, you might need to define them or remove the checks.
# They are typically injected into the global scope.

@app.route('/')
def index():
    """
    Renders the main Digital Wellbeing Guardian page.
    Authentication and content display are now handled client-side in index.html.
    """
    return render_template("index.html")

# The /login route is no longer strictly necessary as index.html handles it,
# but keeping it might be useful for direct navigation or future expansion.
# For now, it will just redirect to the main app as index.html handles login.
@app.route('/login')
def login():
    """
    Redirects to the main application, as login is handled client-side in index.html.
    """
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    """
    Logs out the user by clearing the Firebase ID token cookie.
    """
    response = make_response(redirect(url_for('index'))) # Redirect to index, which will show login form
    response.set_cookie('firebase_id_token', '', expires=0) # Clear the cookie
    return response

# This block is for direct execution (python app.py)
# When using 'flask run', this block is typically not executed.
if __name__ == '__main__':
    # Correctly access global variables provided by the Canvas environment in Python
    # Use globals().get() to safely retrieve the variable or a default value
    app.config['APP_ID'] = globals().get('__app_id', 'default-app-id')
    # You might also need to access __firebase_config and __initial_auth_token
    # if they were intended for use in the Python backend, but typically
    # they are consumed directly by the JavaScript frontend.
    # Example for other globals if needed in Python:
    # firebase_config = globals().get('__firebase_config', '{}')
    # initial_auth_token = globals().get('__initial_auth_token', None)

    # Run the Flask application in debug mode.
    # This is suitable for development; for production, use a WSGI server.
    app.run(debug=True)
