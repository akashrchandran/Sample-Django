# Sample Django Rest Framework API

This is a sample Django Rest Framework API that allows users to register, login, upload files, and download files. The API is secured with JWT authentication. The API is hosted on Heroku and can be accessed via the following link: [https://sample-django-7lfj.onrender.com/](https://sample-django-7lfj.onrender.com/)


## API Documentation

The API documentation is available at the following link: 
1. Swagger UI: [https://sample-django-7lfj.onrender.com/docs/](https://sample-django-7lfj.onrender.com/docs/)
2. Redoc: [https://sample-django-7lfj.onrender.com/redoc/](https://sample-django-7lfj.onrender.com/redoc)

## API Endpoints

| Endpoint              | Method | Description          | Authentication Required | Request Body Parameters |
|-----------------------|--------|----------------------|-------------------------|--------------------|
| `/api/register/`      | POST   | Register User        | No                      | `username`, `password`, `email` |
| `/api/login/`         | POST   | Login User           | No                      | `username`, `password` |
| `/api/upload/`        | POST   | Upload File          | Yes                     | `file` |
| `/api/download/{id}`      | GET    | Download File        | Yes                     | `None` |
| `/api/add/`           | POST   | Add Number           | Yes                     | `num1`, `num2` |
| `/api/subtract/`      | POST   | Subtract Number      | Yes                     | `num1`, `num2` |
| `/api/multiply/`      | POST   | Multiply Number      | Yes                     | `num1`, `num2` |
| `/api/divide/`        | POST   | Divide Number        | Yes                     | `num1`, `num2` |

## Authentication

The API uses JWT authentication. To access the protected endpoints, you need to include the JWT token in the request headers. The token is generated when you login. The token should be included in the `Authorization` header as follows:

```json
{
    "Authorization": "Bearer  <token>"
}
```

## Running the API Locally

To run the API locally, follow the steps below:

1. Clone the repository:

```bash
git clone https://github.com/akashrchandran/sample-django
```

2. Change into the project directory:

```bash
cd sample-django
```

3. Create a virtual environment:

```bash
python3 -m venv env
```

4. Activate the virtual environment:

```bash
source env/bin/activate
```

5. Install the dependencies:

```bash
pip install -r requirements.txt
```

6. Run the migrations:

```bash
python manage.py migrate
```

7. Run the development server:

```bash
python manage.py runserver
```

The API will be accessible at `http://localhost:8000/`.