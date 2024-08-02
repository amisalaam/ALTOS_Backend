

# Event Management System

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
   git clone https://github.com/yourusername/event-management-system.git
   cd event-management-system
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
   SECRET_KEY=your_secret_key
   DEBUG=True
   EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
   DEFAULT_FROM_EMAIL=webmaster@localhost
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

## Contributing

Contributions are welcome! Please create a pull request with your changes or open an issue to discuss a new feature or bug.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Developed with ❤️ by [Your Name](https://github.com/yourusername).*
```

You can copy and paste the entire content above into your `README.md` file. Be sure to replace placeholders like `yourusername` and `your_secret_key` with your actual details.
