import os
import django

# Configurer Django pour accéder aux modèles
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'superfamilytree.settings')
django.setup()

from superhero.models import SuperHero

def populate():
    # Créer des super-héros sans parent (racine de l'arbre)
    spiderman = SuperHero.objects.create(
        name="Spiderman", 
        description="A teenage superhero with spider-like abilities", 
        skill1="Wall-Crawling", 
        skill2="Spider-Sense", 
        skill3="Superhuman Agility", 
        image="spiderman.jpg",
    )

    blackpanther = SuperHero.objects.create(
        name="Black Panther", 
        description="The king of Wakanda, using his enhanced abilities and vibranium suit to protect his people and the world.",
        skill1="Enhanced Agility", 
        skill2="Vibranium Suit", 
        skill3="Master Combatant", 
        image="blackpanther.jpg",
    )

    john = SuperHero.objects.create(
        name="John 'BouclierMan'", 
        description="Initially unaware of his abilities, John discovers that he has the power to neutralize other superpowers.",
        skill1="Power Neutralization", 
        skill2="Enhanced Reflexes", 
        skill3="Strategic Thinking", 
        image="bouclier-man.jpg"
    )

    doctor_strange = SuperHero.objects.create(
        name="Doctor Strange", 
        description="A former neurosurgeon who becomes the Sorcerer Supreme, protecting Earth from magical and mystical threats. He is known for his mastery of the mystic arts and his ability to traverse different dimensions.",
        skill1="Mastery of Magic", 
        skill2="Dimensional Manipulation", 
        skill3="Astral Projection", 
        image="doctor-strange.jpg"
    )

    print("Database populated successfully!")

if __name__ == '__main__':
    print("Populating the database...")
    populate()
    print("Done!")
