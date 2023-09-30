from faker import Faker
from random import randint, choice
from app import app 
from models import db, Hero, Power, HeroPower 

# Initialize the Faker library
fake = Faker()
Faker.seed(0)

# Create a Flask app context
with app.app_context():
    # Clear existing data
    HeroPower.query.delete()
    Power.query.delete()
    Hero.query.delete()

    # Seeding heroes
    heroes = []
    for _ in range(20):
        hero = Hero(
            name=fake.name(),
            super_name=fake.unique.user_name(),
        )
        heroes.append(hero)

    db.session.add_all(heroes)
    db.session.commit()

    # Seeding powers
    powers = []
    power_names = ['Super Strength', 'Flight', 'Telekinesis', 'Invisibility', 'X-ray Vision', 'Fire Manipulation', 'Ice Control', 'Time Travel', 'Teleportation', 'Mind Reading']
    for name in power_names:
        power = Power(
            name=name,
            description=fake.sentence(nb_words=10),
        )
        powers.append(power)

    db.session.add_all(powers)
    db.session.commit()

    # Seeding hero powers
    hero_powers = []
    for hero in heroes:
        for _ in range(randint(1, 3)):  # Random number of powers per hero
            power = choice(powers)
            hero_power = HeroPower(
                hero=hero,
                power=power,
                strength=choice(['Strong', 'Weak', 'Average']),
            )
            hero_powers.append(hero_power)

    db.session.add_all(hero_powers)
    db.session.commit()
