
# ALTOS Event Management System

Welcome to the Event Management System! This project is a Django-based application that allows users to view, register, and manage events. Admin users can create, edit, and delete events, while regular users can register for events and view their registered events.

## Features

- **User Authentication**: Secure authentication for users.
- **Event Management**: Admins can create, update, and delete events.
- **Event Registration**: Users can register for events.
- **Email Notifications**: Sends confirmation emails upon registration.
- **Responsive Design**: Mobile-friendly user interface.



## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/amisalaam/ALTOS_Backend.git
   cd ALTOS_Backend
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add the following:
   ```
    EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
    EMAIL_HOST=smtp.gmail.com
    EMAIL_PORT=587
    EMAIL_USE_TLS=True
    EMAIL_HOST_USER=example@gmail.com
    EMAIL_HOST_PASSWORD=password

    SECRET_KEY='djangoSeceret Key'

   ```

5. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

6. **Create a superuser:**
   ```sh
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

## Setup

### Django Settings

Update the `settings.py` file with the necessary configurations, such as database settings, installed apps, and middleware.

### Static and Media Files

Make sure to configure static and media file settings for serving these files in production.

## Usage

### Running the Server

To start the server, run:
```sh
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view the application.

### Admin Panel

Access the Django admin panel at `http://127.0.0.1:8000/admin` to manage events and users.

### API Endpoints

| Endpoint | Description | Method |
| -------- | ----------- | ------ |
| `/api/token/` | Obtain JWT token | POST |
| `/api/token/refresh/` | Refresh JWT token | POST |
| `/api/register/` | Register a new user | POST |
| `/api/otp/verify/` | Verify OTP for user registration | POST |
| `/api/login/` | Login a user | POST |
| `/api/events/` | List and create events | GET, POST |
| `/api/events/<id>/` | Retrieve, update, and delete an event | GET, PUT, DELETE |
| `/api/register/event/` | Register for an event | POST |
| `/api/register/event/` | List registered events for a user | GET |


### Example Request

**Register for an Event:**
```sh
curl -X POST http://127.0.0.1:8000/api/register/event/ -H "Content-Type: application/json" -d '{
    "email": "user@example.com",
    "event_id": 1
}'
```

**Obtain JWT Token:**
```sh
curl -X POST http://127.0.0.1:8000/api/token/ -H "Content-Type: application/json" -d '{
    "username": "yourusername",
    "password": "yourpassword"
}'
```

## Project Structure

```
event-management-system/
├── manage.py
├── README.md
├── requirements.txt
├── .env
├── users/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── events/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
└── ...
```


