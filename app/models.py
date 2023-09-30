from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    super_name = db.Column(db.String(255), nullable=False)

    powers = db.relationship('Power', secondary='hero_power', backref='heroes')

    def __repr__(self):
        return f'<Hero {self.id}: {self.name} ({self.super_name})>'

class Power(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Power {self.id}: {self.name}>'

class HeroPower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'), nullable=False)
    strength = db.Column(db.String(255), nullable=False)
    

    def __repr__(self):
        return f'<HeroPower {self.id}: Hero ID {self.hero_id}, Power ID {self.power_id}, Strength: {self.strength}>'
