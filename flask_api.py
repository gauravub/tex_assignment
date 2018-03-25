from alchemy import app, Location, db
from flask import render_template, redirect, url_for, request, jsonify
from sqlalchemy import exc


@app.route('/add_location', methods=["POST"])
def add_location():
    json_dict = request.get_json()
    # print(json_dict)
    new_id = int(json_dict['id'])
    description = json_dict['description']
    datetime = json_dict['datetime']
    longitude = float(json_dict['longitude'])
    latitude = float(json_dict['latitude'])
    elevation = int(json_dict['elevation'])

    new_loc = Location(new_id, description, datetime, longitude, latitude, elevation)
    try:
        db.session.add(new_loc)
        db.session.commit()

    except exc.IntegrityError as e:
        db.session().rollback()
        raise ValueError("Integrity error:" + e.__str__())

    return jsonify({"status":"Success", "message": "1 row inserted"})


@app.route('/update_location', methods=["POST"])
def update_location():
    json_dict = request.get_json()
    print(json_dict)
    new_id = int(json_dict['id'])
    description = json_dict['description']
    datetime = json_dict['datetime']
    longitude = float(json_dict['longitude']) if json_dict.get('longitude') else None
    latitude = float(json_dict['latitude']) if json_dict.get('latitude') else None
    elevation = int(json_dict['elevation']) if json_dict.get('elevation') else None

    update_location = db.session.query(Location).get((new_id, description, datetime))

    if longitude:
        update_location.longitude = longitude
    if latitude:
        update_location.latitude = latitude
    if elevation:
        update_location.elevation = elevation
    db.session.commit()
    return jsonify({"status":"Success", "message": "1 row updated"})


@app.route('/delete_location', methods=["POST"])
def delete_location():
    json_dict = request.get_json()
    print(json_dict)
    new_id = int(json_dict['id'])
    description = json_dict['description']
    datetime = json_dict['datetime']

    delete_location = db.session.query(Location).get((new_id, description, datetime))
    db.session.delete(delete_location)
    db.session.commit()
    return jsonify({"status":"Success", "message": "1 row deleted"})


@app.route('/')
def hello():
    return redirect(url_for('thread', page_num=1))


@app.route('/location/<int:page_num>')
def thread(page_num):
    threads = Location.query.paginate(per_page=5, page=page_num, error_out=True)
    return render_template('results.html', threads=threads)


if __name__ == '__main__':
    app.run(debug=True)