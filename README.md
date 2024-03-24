# Sherpa-AI-Learning-Management-System
# Django LMS (Learning Management System)

Django LMS is a Learning Management System built with Django and Django REST Framework. It provides a platform for managing users, classes, assignments, questions, and more.

## Installation

1. Clone the repository:

    ```
    git clone <repository_url>
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```
    python manage.py migrate
    ```

4. Run the development server:

    ```
    python manage.py runserver
    ```

## Usage

### API Endpoints

- **Authentication**: `/authenticate/` (POST)
- **Users**: `/api/users/` (GET, POST), `/api/users/<id>/` (GET, PUT, PATCH, DELETE)
- **Assignments**: `/api/assignments/` (GET, POST), `/api/assignments/<id>/` (GET, PUT, PATCH, DELETE)
- **Questions**: `/api/questions/` (GET, POST), `/api/questions/<id>/` (GET, PUT, PATCH, DELETE)
- **Classes**: `/api/classes/` (GET, POST), `/api/classes/<id>/` (GET, PUT, PATCH, DELETE)

### API Documentation

- Access the API documentation at `/`

## Contributing

Contributions are welcome! If you'd like to contribute to Django LMS, please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -am 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project was inspired by [Django](https://www.djangoproject.com/) and [Django REST Framework](https://www.django-rest-framework.org/).
- Special thanks to all contributors and the open-source community.
