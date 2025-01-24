from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Lead

bp = Blueprint('leads', __name__, url_prefix='/leads')

@bp.route('/')
def index():
    leads = Lead.query.all()
    return render_template('leads.html', leads=leads)

@bp.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        name = request.form['name']
        source = request.form['source']
        status = request.form['status']
        lead = Lead(name=name, source=source, status=status)
        db.session.add(lead)
        db.session.commit()
        return redirect(url_for('leads.index'))
    return render_template('add_lead.html')
