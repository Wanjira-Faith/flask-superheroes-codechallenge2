from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# Route to get all heroes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    hero_list = []
    for hero in heroes:
        hero_data = {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name
        }
        hero_list.append(hero_data)
    return jsonify(hero_list)

# Route to get heroes by id
@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)

    if not hero:
        return jsonify({
            "error": "Hero not found"
        }), 404

    hero_data = {
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "powers": []
    }

    for power in hero.powers:
        power_data = {
            "id": power.id,
            "name": power.name,
            "description": power.description
        }

        hero_data["powers"].append(power_data)

    return jsonify(hero_data)

# Route to get all powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    
    power_list = []
    for power in powers:
        power_data = {
            "id": power.id,
            "name": power.name,
            "description": power.description
        }
        power_list.append(power_data)
    
    # Return list of powers as JSON
    return jsonify(power_list)

if __name__ == '__main__':
    app.run(debug=True)