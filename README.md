# Plant Collector 🌿

[Plant Collector](https://plant-collections.herokuapp.com/) is a Django app designed to provide users a central web application to showcase, track and maintain their plants.

## Usage 👩‍💻

To get started, clone this repo. Change your directory to where you'd like to host the app (I use my Desktop for simplicity's sake) and enter the commands below in your terminal:

```bash
git clone https://github.com/mikezalik/plantcollector.git
cd plantcollector
pip3 install -r requirements.txt
```

To set up a local environment you'll need to change this field in plantcollector/settings.py

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'plantcollector',
    }
}
```

Save the file and run these commands to set up your local db. Make sure you install PostgreSQL before proceeding!

```
createdb plantcollector
python3 manage.py makemigrations
python3 manage.py migrate

```

- **Development**: to run the app locally use `python3 manage.py runserver` in your terminal.

This web app is hosted on Heroku at [Plant Collector](https://plant-collections.herokuapp.com/)

## Project Summary 👍

Plant Collector is a Django app designed to help organize plant information and care instructions for your favorite plants. It was inspired by the fact that I've had a hard time keeping SOME individual plants alive.

## Screenshot 📸

| <img alt="Landing Page" src="public/login.png" width="400"> |
| :---------------------------------------------------------: |
|                         Login Page                          |

| <img alt="Landing Page" src="public/view_all.png" width="400"> |
| :------------------------------------------------------------: |
|                        All Plants Page                         |

| <img alt="Landing Page" src="public/plant_details.png" width="400"> |
| :-----------------------------------------------------------------: |
|                          Plant Detail Page                          |

## Design Process 📐

In the design phase of this application, I started by imagining the user journey of a plant lover. Users will need a space to add plants, read info on them, update them, and get rid of them in case they sold the plant or it died... I reasoned Django's CRUD-like backend would work well for its ability to provide the create, update, read and delete features needed to complete the user journey. I also reasoned that the Django templating engine would be perfect for a straightforward user interface that promotes ease-of-use.

## Development Process 🛠

I started the development process by completing a PostgreSQL setup. I then created the user-facing templates, worked my way through each request and response cycle from template through model to complete each leg in the CRUD journey. I started with the home, index, base, plant and plant detail templates and created the plant model and its respective view actions. From there I added the options for care instructions and incorporated the ability to upload photos and store in an S3 bucket. Once I completed the user journey, I roped in Django auth, user creation and made modifications to the models so users can see only their plants.

## Tech Used 💻

### Front-End

- JavaScript
- HTML5
- CSS3
- Materialize

### Back-End

- Python
- Django
- PostgreSQL
- Amazon Web Services S3 Storage

### Deployment

- [Heroku](https://heroku.com) - PaaS cloud host

## Future Improvements 🚀

I'd like to implement the ability for users to review each other's plants and see other collections.
