from flask import render_template, request, Blueprint
from datetime import datetime
from config import SITE_TITLE, db_connection

search_bp = Blueprint('search', __name__)

page_title = "Search"
page_title = " - " + page_title if page_title else ""
page_title = SITE_TITLE + page_title if SITE_TITLE else page_title

@search_bp.route("/search", methods=["GET"])
# @bp.route("/search", methods=["GET"])
def search():
    return render_template('search.html', title=page_title)

@search_bp.route("/search/results", methods=["GET"])
def search_results():
    query = request.args.get('q', '')
    
    results = ()
    if query:
        conn = db_connection()
        cur = conn.cursor()
        
        cur.execute(f"SELECT title, description FROM tblSearches WHERE title LIKE \"%{query}%\" or description LIKE \"%{query}%\"")
        results = cur.fetchall()
        cur.close()

    return render_template(
        'results.html',
        title=page_title,
        query=query,
        results=results,
        year=datetime.now().year,
    )