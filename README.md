# Flask Code Challenge - Superheroes

This is a Superheroes Database and API that offers a comprehensive solution for managing and retrieving information about superheroes and their superpowers. It provides a RESTful API for creating, reading, and updating superheroes, their powers, and their power levels.

# Table of Contents
1. Prerequisites
2. Getting started
3. Database Models
4. API endpoints
5. Usage
6. License
7. Author

# Prerequisites
Before getting started, make sure you have the following prerequisites installed:

- Python 3.x
- Pipenv (for managing Python dependencies)
- Node.js and npm (for the provided React frontend,optional)

# Getting started
1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install Python dependencies using Pipenv:

       pipenv install

4. Install frontend dependencies (Note: The frontend is provided for testing purposes and does not require modification):       

       npm install --prefix client

5. Apply migrations 

       flask db upgrade

6. Seed the database:  

       python seed.py

#  Models and Database
This code challenge includes three database models:
- **Hero**: Represents a superhero with properties like `name` and `super_name`.
- **Power**: Represents a superpower with properties like `name` and `description`.
- **HeroPower**: Represents the association between a hero and  power, with an additional `strength` property.

These models have relationships that allow heroes to possess multiple powers, and powers to be possessed by multiple heroes. 

# API endpoints
The API provides the following routes to interact with the models:

- **GET /heroes**: Retrieves a list of all superheroes.
           
             [
              { "id": 1, "name": "Kamala Khan", "super_name": 
              "Ms.  Marvel" },
              { "id": 2, "name": "Doreen Green", "super_name":  
              "Squirrel Girl" },
             { "id": 3, "name": "Gwen Stacy", "super_name": "Spider-Gwen" 
             }
           ]

- **GET /heroes/:id**: Retrieves information about a specific superhero by ID.

  **Response**: if hero exist

       {
             "id": 1,
             "name": "Kamala Khan",
             "super_name": "Ms. Marvel",
             "powers": [
           {
             "id": 1,
             "name": "super strength",
             "description": "gives the wielder super-human strengths"
           },
          {
             "id": 2,
             "name": "flight",
             "description": "gives the wielder the ability to fly  through the skies at supersonic speed"
          }
        ]
      }
    **Response**: if hero does not exist

      {
        "error": "Hero not found"
      }

- **GET /powers**: Retrieves a list of all superpowers.

      [
        {
         "id": 1,
         "name": "super strength",
         "description": "gives the wielder super-human strengths"
        },
        {
         "id": 2,
         "name": "flight",
         "description": "gives the wielder  the ability to fly through the skies at supersonic speed"
        }
      ]


- **GET /powers/:id**: Retrieves information about a specific superpower by ID.

  **Response**: if power exist

      {
        "id": 1,
        "name": "super strength",
        "description": "gives the wielder super-human strengths"
      }

   **Response**: if power does not exist

      {
        "error": "Power not found"
      }

- **PATCH /powers/:id**: Updates an existing power's description.

  **Request Body** :

      {
        "description": "Updated description"
      }

  **Response**: if power exists and is updated successfully 

      {
        "id": 1,
        "name": "super strength",
        "description": "Updated description"
      }

   **Response**: if power updates fails validation

      {
        "errors": ["validation errors"]
      }

- **POST /hero_powers**: Creates a new association between a hero and a power.

  **Request Body** :

       {
        "strength": "Average",
        "power_id": 1,
        "hero_id": 3
      }
    

   **Response**: if HeroPower is created successfully:

         {
             "id": 1,
             "name": "Kamala Khan",
             "super_name": "Ms. Marvel",
             "powers": [
               {
                 "id": 1,
                 "name": "super strength",
                 "description": "gives the wielder super-human strengths"
                },
                {
                 "id": 2,
                 "name": "flight",
                 "description": "gives the wielder the ability to fly through the skies at supersonic speed"
                }
              ]
            }

  **Response**: if HeroPower creation fails validation:

       {
         "errors": ["validation errors"]
       }

Each route returns JSON data in the specified format and handles error cases appropriately.

# Usage
To run the Flask server, use the following command:

    python app.py

The API will be available at http://localhost:5555    

# License
This project is licensed under the MIT License.

# Author
Wanjira Faith(Software Engineer)