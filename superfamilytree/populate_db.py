import os
import django

# Configurer Django pour accéder aux modèles
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'superfamilytree.settings')
django.setup()

from superhero.models import SuperHero

def populate():
    # Créer des super-héros sans parent (racine de l'arbre)
    frozone = SuperHero.objects.create(
        name="Frozone", 
        description="Master of ice and cold", 
        skill1="Ice manipulation", 
        skill2="Cold resistance", 
        skill3="Skating", 
        image="frozone.jpg",
    )

    batman = SuperHero.objects.create(
        name="Batman", 
        description="Dark Knight of Gotham", 
        skill1="Martial Arts", 
        skill2="Detective Skills", 
        skill3="Stealth", 
        image="batman.jpg"
    )

    thor = SuperHero.objects.create(
        name="Thor", 
        description="God of Thunder", 
        skill1="Lightning control", 
        skill2="Super Strength", 
        skill3="Immortality", 
        image="thor.jpg"
    )

    rocket = SuperHero.objects.create(
        name="Rocket", 
        description="Expert marksman and tactician", 
        skill1="Expert Marksman", 
        skill2="Engineering", 
        skill3="Tactics", 
        image="rocket.jpg"
    )
    
    groot = SuperHero.objects.create(
        name="Groot", 
        description="Living tree with regenerative abilities", 
        skill1="Regeneration", 
        skill2="Super Strength", 
        skill3="Size manipulation", 
        image="groot.jpg",
        parent=rocket
    )


    daredevil = SuperHero.objects.create(
        name="Daredevil", 
        description="The Man Without Fear", 
        skill1="Enhanced senses", 
        skill2="Martial Arts", 
        skill3="Acrobatics", 
        image="daredevil.jpg",
    )

    black_widow = SuperHero.objects.create(
        name="Black Widow", 
        description="Elite spy and combatant", 
        skill1="Espionage", 
        skill2="Martial Arts", 
        skill3="Tactics", 
        image="black_widow.jpg"
    )

    catwoman = SuperHero.objects.create(
        name="Catwoman", 
        description="Master thief and skilled fighter", 
        skill1="Stealth", 
        skill2="Acrobatics", 
        skill3="Martial Arts", 
        image="catwoman.jpg",
        parent=black_widow
    )

    gamorra = SuperHero.objects.create(
        name="Gamorra", 
        description="Deadliest woman in the galaxy", 
        skill1="Swordsmanship", 
        skill2="Martial Arts", 
        skill3="Tactics", 
        image="gamorra.jpg",
        parent=catwoman
    )

    wolverine = SuperHero.objects.create(
        name="Wolverine", 
        description="The best there is at what he does", 
        skill1="Regeneration", 
        skill2="Adamantium skeleton", 
        skill3="Enhanced senses", 
        image="wolverine.jpg"
    )

    tornade = SuperHero.objects.create(
        name="Tornado", 
        description="Weather-controlling mutant", 
        skill1="Weather manipulation", 
        skill2="Flight", 
        skill3="Energy projection", 
        image="tornade.jpg",
        parent=wolverine
    )

    professor_xavier = SuperHero.objects.create(
        name="Professor X", 
        description="Leader of the X-Men with powerful telepathy", 
        skill1="Telepathy", 
        skill2="Mind control", 
        skill3="Genius-level intellect", 
        image="professor_x.jpg"
    )

    print("Database populated successfully!")

if __name__ == '__main__':
    print("Populating the database...")
    populate()
    print("Done!")
