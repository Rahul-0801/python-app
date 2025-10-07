from flask import Flask, render_template


# Create an instance of the Flask class.
app = Flask(__name__)


@app.route('/')
def home():
    """Serves the home page."""
    return render_template('home.html')


@app.route('/about')
def about():
    """Serves the about page."""
    return render_template('about.html')


if __name__ == '__main__':
    # debug=True will auto-reload the server on code changes and show detailed errors.
    # For production, consider using a production-ready WSGI server like Gunicorn.
    # host='0.0.0.0' makes the app accessible from any IP, which is necessary for containerized deployments like Cloud Run.
    app.run(
        debug=True,
        host='0.0.0.0',
        port=8080
    )