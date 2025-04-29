from flask import Blueprint, render_template, request
from datetime import datetime
from config import SITE_TITLE

search_bp = Blueprint('search', __name__)

page_title = "Search"
page_title = " - " + page_title if page_title else ""

@search_bp.route("/search")
def search():
    page_title = "Search"
    return render_template('search.html', title=page_title)

@search_bp.route("/search/results", methods=["GET"])
def search_results():
    query = request.args.get('q', '')
    
    results = []
    if query:
        # Add your search implementation here
        pass

    return render_template(
        'search.html',
        title=page_title,
        query=query,
        results=results,
        year=datetime.now().year
    )