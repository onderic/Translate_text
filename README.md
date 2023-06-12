# Vue.js and Django Rest Framework Translation App

This is a translation application built using Vue.js and Django Rest Framework. It allows users to enter text and select a target language for translation. The application makes API calls to the backend server, which utilizes machine translation to provide the translated text.

## Features

- Translate text from one language to another.
- Support for multiple target languages.
- Real-time translation using the Django Rest Framework backend.

## Installation

To run this application locally, follow these steps:

## Clone the repository:
    git clone https://github.com/onderic/Translate_text.git


## Install the dependencies for the frontend (Vue.js):

    cd translation-app/frontend
    npm install
## Install the dependencies for the backend (Django Rest Framework):

    cd ../backend
    pip install -r requirements.txt

## Start the frontend development server:

    cd ../frontend

    npm run serve

## Start the backend server:

    cd ../backend
    python manage.py runserver

## Access the application in your web browser:

    http://localhost:8080

Configuration
    To configure the backend server and API endpoints, update the settings in backend/settings.py file. You might need to modify the database settings, CORS configuration, and any other relevant settings as per your requirements.

API Endpoints
The following API endpoints are available:

POST /api/v1/translate/: Translates the given text to the target language.
Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.


Feel free to customize the content based on your project's specific details and requirements.
