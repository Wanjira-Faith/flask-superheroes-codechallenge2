from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, Hero, Power, HeroPower

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
CORS(app)

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

# Route to get powers by id
@app.route('/powers/<int:power_id>', methods=['GET'])
def get_power(power_id):
    power = Power.query.get(power_id)
    
    if power is None:
        return jsonify({"error": "Power not found"}), 404
    
    power_data = {
        "id": power.id,
        "name": power.name,
        "description": power.description
    }
    
    return jsonify(power_data)

# Route to update powers description by id
@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)

   # Check if the power exists
    if not power:
        return jsonify({
            "error": "Power not found"
        }), 404

    # Validate request body
    power_data = request.get_json()
    if "description" not in power_data:
        return jsonify({
            "errors": ["description is required"]
        }), 400

    if len(power_data["description"]) < 20:
        return jsonify({
            "errors": ["description must be at least 20 characters long"]
        }), 400

    # Try to update power
    try:
        power.description = power_data["description"]
        db.session.commit()
    except Exception as e:
        # If the power is not updated successfully, return error response
        return jsonify({
            "errors": ["validation errors"]
        }), 400

    # Return the updated power
    updated_power_data = {
        "id": power.id,
        "name": power.name,
        "description": power.description
    }

    return jsonify(updated_power_data), 200

# Route to create new hero powers
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    
    # Parse JSON data from the request body
    data = request.json

    # Check if the requested Power exists
    power = Power.query.get(data['power_id'])
    if power is None:
        return jsonify({"errors": ["Power not found"]}), 404

    # Check if the requested Hero exists
    hero = Hero.query.get(data['hero_id'])
    if hero is None:
        return jsonify({"errors": ["Hero not found"]}), 404
    
    if data['strength'] not in['Strong', 'Weak', 'Average'] :
        return jsonify({"errors": ["Invalid strength"]}), 400

    # Create new HeroPower 
    hero_power = HeroPower(
        strength=data['strength'],
        power_id=data['power_id'],
        hero_id=data['hero_id']
    )

    # Add the HeroPower to the db
    db.session.add(hero_power)
    db.session.commit()

    # Fetch related Hero with their powers
    hero = Hero.query.get(data['hero_id'])
    if hero is not None:
        # Convert Hero object and associated Powers to JSON
        hero_data = {
            'id': hero.id,
            'name': hero.name,
            'super_name': hero.super_name,
            'powers': [{'id': power.id, 'name': power.name, 'description': power.description} for power in hero.powers]
        }
        return jsonify(hero_data), 201  
    
    return jsonify({"errors": ["validation errors"]}), 400

if __name__ == '__main__':
    app.run(port=5555, debug=True)