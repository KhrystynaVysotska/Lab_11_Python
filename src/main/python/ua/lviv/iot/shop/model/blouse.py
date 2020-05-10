from src.main.python.ua.lviv.iot.shop.model.abstract_clothes import AbstractClothes
from src.main.python.ua.lviv.iot.shop.model.gender import Gender
from src.main.python.ua.lviv.iot.shop.model.season import Season
from flask import Flask, request, abort, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
import json
import copy

with open('../../../../../../../../secret.json') as f:
    SECRET = json.load(f)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}?auth_plugin=mysql_native_password".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Blouse(AbstractClothes, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    season_name = db.Column(db.Enum(Season), nullable=False)
    country_of_manufacture = db.Column(db.String(32), nullable=False)
    brand_name = db.Column(db.String(32), nullable=False)
    price_in_uah = db.Column(db.Float, nullable=False)
    gender_category = db.Column(db.Enum(Gender), nullable=False)
    material = db.Column(db.String(32), nullable=False)
    color = db.Column(db.String(32), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    item_id = db.Column(db.Integer, nullable=False)
    age_group_in_years = db.Column(db.Integer, nullable=False)
    height_in_centimetres = db.Column(db.Integer, nullable=False)
    clothes_style = db.Column(db.String(32), nullable=False)
    print_type = db.Column(db.String(32), nullable=False)
    neckline_type = db.Column(db.String(32), nullable=False)
    sleeve_length_in_centimetres = db.Column(db.Float, nullable=False)

    def __init__(self, season_name: Season, country_of_manufacture: str, brand_name: str, price_in_uah: float,
                 gender_category: Gender, material: str, color: str, size: int, item_id: int, age_group_in_years: int,
                 height_in_centimetres: int, clothes_style: str, print_type: str, neckline_type: str,
                 sleeve_length_in_centimetres: float) -> None:
        AbstractClothes.__init__(self, season_name, country_of_manufacture, brand_name, price_in_uah, gender_category,
                                 material, color, size, item_id, age_group_in_years, height_in_centimetres,
                                 clothes_style, print_type)
        self.neckline_type = neckline_type
        self.sleeve_length_in_centimetres = sleeve_length_in_centimetres


class BlouseSchema(ma.Schema):
    class Meta:
        fields = ('season_name', 'country_of_manufacture',
                  'brand_name', 'price_in_uah', 'gender_category',
                  'material', 'color', 'size', 'item_id', 'age_group_in_years',
                  'height_in_centimetres', 'clothes_style', 'print_type',
                  'neckline_type', 'sleeve_length_in_centimetres', 'id')


blouse_schema = BlouseSchema()
blouses_schema = BlouseSchema(many=True)


@app.route("/blouses", methods=["POST"])
def add_blouse():
    body = request.get_json()
    blouse = Blouse(**body)

    db.session.add(blouse)
    db.session.commit()
    return blouse_schema.jsonify(blouse)


@app.route("/blouses", methods=["GET"])
def get_blouses():
    all_blouses = Blouse.query.all()
    return jsonify({'blouses': blouses_schema.dump(all_blouses)})


@app.route("/blouses/<blouse_id>", methods=["GET"])
def get_blouse(blouse_id):
    blouse = Blouse.query.get(blouse_id)
    if not blouse:
        abort(404)
    return blouse_schema.jsonify(blouse)


@app.route("/blouses/<blouse_id>", methods=["PUT"])
def update_blouse(blouse_id):
    blouse = Blouse.query.get(blouse_id)
    if not blouse:
        abort(404)
    old_blouse = copy.deepcopy(blouse)
    blouse.season_name = request.json['season_name']
    blouse.country_of_manufacture = request.json['country_of_manufacture']
    blouse.brand_name = request.json['brand_name']
    blouse.price_in_uah = request.json['price_in_uah']
    blouse.gender_category = request.json['gender_category']
    blouse.material = request.json['material']
    blouse.color = request.json['color']
    blouse.size = request.json['size']
    blouse.item_id = request.json['item_id']
    blouse.age_group_in_years = request.json['age_group_in_years']
    blouse.height_in_centimetres = request.json['height_in_centimetres']
    blouse.clothes_style = request.json['clothes_style']
    blouse.print_type = request.json['print_type']
    blouse.neckline_type = request.json['neckline_type']
    blouse.sleeve_length_in_centimetres = request.json['sleeve_length_in_centimetres']
    db.session.commit()
    return blouse_schema.jsonify(old_blouse)


@app.route("/blouses/<blouse_id>", methods=["DELETE"])
def delete_blouse(blouse_id):
    blouse = Blouse.query.get(blouse_id)
    if not blouse:
        abort(404)
    db.session.delete(blouse)
    db.session.commit()
    return blouse_schema.jsonify(blouse)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='localhost')