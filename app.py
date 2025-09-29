from flask import Flask, render_template

# Create an instance of the Flask class.
app = Flask(__name__)

# __name__ is a special variable that gets the name of the current Python module.
@app.route('/')
def home():
    """Serves the home page."""
    # Render the home.html template
    return render_template('home.html')

# Define a route for an 'about' page.
@app.route('/about')
def about():
    """Serves the about page."""
    # Render the about.html template
    return render_template('about.html')

# This block allows you to run the app directly from the command line.
if __name__ == '__main__':
    # debug=True will auto-reload the server on code changes and show detailed errors.
    # For production, consider using a production-ready WSGI server like Gunicorn.
    # host='0.0.0.0' makes the app accessible from any IP, which is necessary for containerized deployments like Cloud Run.
    app.run(debug=True, host='0.0.0.0', port=8080) # Using port 8080 as a common port for containerized apps.

