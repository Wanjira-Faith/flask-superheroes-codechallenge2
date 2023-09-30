from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    super_name = db.Column(db.String(255), nullable=False)

   # Define a many-to-many relationship with the Power model using the HeroPower association table
    powers = db.relationship('Power', secondary='hero_power', backref='heroes')

    @validates('name')
    def validate_name(self, key, value):
        if not value:
            raise ValueError("Name cannot be empty")
        return value

    @validates('super_name')
    def validate_super_name(self, key, value):
        if not value:
            raise ValueError("Super name cannot be empty")
        return value

    def __repr__(self):
        return f'<Hero {self.id}: {self.name} ({self.super_name})>'

class Power(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)

    @validates('name')
    def validate_name(self, key, value):
        if not value:
            raise ValueError("Power name cannot be empty")
        return value

    @validates('description')
    def validate_description(self, key, value):
        if not value:
            raise ValueError("Description cannot be empty")
        if len(value) < 20:
            raise ValueError("Description must be at least 20 characters long")
        return value

    def __repr__(self):
        return f'<Power {self.id}: {self.name}>'

class HeroPower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'), nullable=False)
    strength = db.Column(db.String(255), nullable=False)
    
    @validates('strength')
    def validate_strength(self, key, value):
        if value not in ['Strong', 'Weak', 'Average']:
            raise ValueError("Strength must be one of the following values: 'Strong', 'Weak', 'Average'")
        return value
    
    def __repr__(self):
        return f'<HeroPower {self.id}: Hero ID {self.hero_id}, Power ID {self.power_id}, Strength: {self.strength}>'
    
