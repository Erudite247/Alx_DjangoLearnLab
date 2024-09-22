# Django Blog Authentication System

## Features
- User registration
- User login/logout
- Profile management

## Setup Instructions
1. Clone the repository.
2. Install requirements with `pip install -r requirements.txt`.
3. Run migrations: `python manage.py migrate`.
4. Create a superuser: `python manage.py createsuperuser`.
5. Start the server: `python manage.py runserver`.
6. Visit `/register`, `/login`, `/profile` to interact with the authentication system.

## Testing Instructions
- Register a new user.
- Log in using the registered credentials.
- Edit the user profile.
- Log out and confirm that the session is terminated.
