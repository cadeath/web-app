from flask import Flask, redirect, url_for, send_from_directory, render_template

app = Flask(__name__)

title = "Web Application"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/public/<filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/')
def home():
    return render_template('index.html', title=title)

@app.route("/search")
def search():
    return render_template('search.html', title=title)

@app.route("/admin")
def admin():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()
