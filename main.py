from flask import Flask, redirect, url_for, send_from_directory, render_template
from config import SITE_TITLE

from controllers.search import search_bp

app = Flask(__name__)
app.register_blueprint(search_bp)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/public/<filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/')
def home():
    # return render_template('index.html', title=SITE_TITLE)
    return redirect(url_for('search.search'))

@app.route("/admin")
def admin():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()
