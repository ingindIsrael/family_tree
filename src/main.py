"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
#from models import Person

from familia import Losperez

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

perez_family = Losperez("Perez")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code



@app.route('/members/all')
def get_members():
    members = perez_family.getAllMembers()
    return jsonify(members), 200

@app.route('/member/<int:id>')
def get_single_member(id):
    member = perez_family.getSingleMember(id)
    return jsonify(member), 200

@app.route('/members/create')
def create_member():
    members = perez_family.getAllMembers()
    grandparent = members[0]
    first_parent = perez_family.createFamilyMember("Elena", "30", grandparent['id'])
    second_parent = perez_family.createFamilyMember("Jose", "27", grandparent['id'])
    first_child = perez_family.createFamilyMember("Juan", "4", first_parent["id"])
    second_child = perez_family.createFamilyMember("Patricia", "2", first_parent['id'])
    family_tree = perez_family.getAllMembers()
    return jsonify(family_tree), 200

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)