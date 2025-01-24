from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Contact

bp = Blueprint('contacts', __name__, url_prefix='/contacts')

@bp.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('contacts.html', contacts=contacts)

@bp.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        contact = Contact(name=name, email=email, phone=phone)
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('contacts.index'))
    return render_template('add_contact.html')
