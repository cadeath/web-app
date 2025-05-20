from flask import render_template, request, Blueprint
from datetime import datetime
from config import SITE_TITLE, db_connection

dashboard_bp = Blueprint('dashboard', __name__)