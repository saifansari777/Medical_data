from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from bson import ObjectId
from werkzeug.exceptions import abort

from .auth import login_required
from .db import init_db

bp = Blueprint('med', __name__)

@bp.route('/')
def index():
    db = init_db()
    records = db.med_record.find({})
    return render_template('med_record/index.html', records=records)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        patient_name = request.form['patient_name']
        doctor_name = request.form['doctor_name']
        diagnoses = request.form['diagnoses']
        registration_date = request.form['registration_date']
        last_checkup_date = request.form['last_checkup_date']
        comment = request.form["comment"]
        error = None

        if not patient_name and doctor_name and diagonses:
            error = 'fields are required.'

        if error is not None:
            flash(error)
        else:
            db = init_db()
            db.med_record.insert_one({"patient_name":patient_name, "doctor_name":doctor_name, "diagnoses":diagnoses,"registration_date":registration_date,"last_checkup_date":last_checkup_date,
            "comment":comment,})
            return redirect(url_for('med.index'))

    return render_template('med_record/create.html')



def get_record(id):
    record = init_db().med_record.find_one({"_id":ObjectId(id)})

    if record is None:
        abort(404, "record id {0} doesn't exist.".format(id))

    
    return record



@bp.route('/id/update', methods=('GET', 'POST'))
@login_required
def update():
    id = request.args.get("id")
    record = get_record(id)
    
    if request.method == 'POST':
        patient_name = request.form['patient_name']
        doctor_name = request.form['doctor_name']
        diagnoses = request.form['diagnoses']
        registration_date = request.form['registration_date']
        last_checkup_date = request.form['last_checkup_date']
        comment = request.form["comment"]
        error = None

        if not patient_name:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = init_db()
            db.med_record.update_one({"_id":ObjectId(id)}, {"$set" : {"patient_name":patient_name, "doctor_name":doctor_name, "diagnoses":diagnoses,"registration_date":registration_date,"last_checkup_date":last_checkup_date,
            "comment":comment,} })
            
            return redirect(url_for('med.index'))

    return render_template('med_record/update.html', record=record)


@bp.route('/id/delete', methods=('POST',))
@login_required
def delete():
    id = request.args.get("id")
    get_record(id)
    db = init_db()
    db.med_record.delete_one({"_id":ObjectId(id)})
    return redirect(url_for('med.index'))