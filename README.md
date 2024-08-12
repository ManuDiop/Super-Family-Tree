# Super Family Tree

***Superhero Family Tree*** is a web application that allows you to create, modify, display, and delete superheroes while visualizing their family relationships. The project focuses on managing parent-child relationships among superheroes, enabling users to view the ancestry and descendants of each character dynamically and visually.

## Features 

- **Add a superhero** : \
Create a new superhero by defining their name, skills (up to three), a description, its image url and their parent, if they have one.

- **Edit a superhero** : \
Modify the details of an existing superhero. 

- **Delete a superhero** : \
Delete a superhero and, if applicable, all their descendants.

- **Display relationships** : \
View the ancestry and descendants of a superhero, with a tree structure showing parents and children.

- **Search** : \
Search for superheroes by their name and directly access their detailed profile.


## Technologies used 

- **Django** : \
The main framework for the backend

- **SQlite** : \
Database used to store superhero information 

- **HTML/CSS** : \
For creating the user interface

- **JavaScript** : \
Just a few to handle dynamic interactions like toggling between parent and child views. 

- **FontAwesome** : 
Used for icons on the website


## Installation and setup 

1. Clone the project 
``` git clone git@github.com:ManuDiop/Super-Family-Tree.git ```

2. Place yourself in the project in order to be able to use manage.py file\
``` cd superfamilytree ```

3. Create a virtual environnement\
``` python -m venv .env ```\
``` source .env/bin/activate ```

4. Install all dependencies\
``` pip install -r requirements.txt ```

5. Apply migrations\
``` python manage.py migrate ```

6. Run de development server\
``` python manage.py runserver ```

7. Access the app\
Open your browser and go to ``` http://127.0.0.1:8000 ``` as instructed in your terminal


## Project structure 

- **authuser**\
Manages user authentication, including signup, login, logout and also the homepage app.

- **superhero**\
The main application for managing superheroes, including models, views, and templates.

- **static/styles**\
CSS files for layout and application styling and assets like images. There is also a main.css file containing global styling used across all pages.

- **templates**\
Contains HTML templates organized by application.


## Development choices 

- **Recursive Model**\
The relationship between superheroes is managed through a recursive relationship in the superHero model, making it easy to link a hero to a parent.
First I thought about creating a another table named ``` relations ``` with a ``` parent_id ```and a ``` child_id ``` but, as each superhero could only have one parent (as requested) I chose recursivity. It was also a nod to the previous evaluation test. 

- **Frontend**\
I chose not to use a frontend framework since the user interface was limited to just a few pages. The goal here was to reduce the number of dependencies and keep the project lightweight.


## Possible future improvements 
- Implement advanced search filters to find superheroes by skills or relationships.
- Enhance the style and responsiveness of the user interface for a better mobile interface.
- Find a way for the user to add his superhero image (not only the url) maybe with an image storage API. For now only a developper can upload an image by storing it in the assets folder and inserting its path in the DB. 
- I have created a personnalized 404 page but, as I am still in dev mode (Debug=True), I cannot display it without modifying my ```settings.py```

