from flask import Flask, redirect, url_for, send_from_directory, render_template
from controllers.search import search_bp
from config import SITE_TITLE

app = Flask(__name__)
app.register_blueprint(search_bp, url_prefix='/search')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/public/<filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/')
def home():
    return render_template('index.html', title=SITE_TITLE)

@app.route("/search")
def search():
    return render_template('search.html', title=SITE_TITLE)

@app.route("/admin")
def admin():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()
