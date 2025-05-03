# AppDjango

This is a simple Django project that models products, categories, and tags.

## Requirements

Make sure you have the following installed:

- **Python**
- **Django**
- **pip**
- **Git**

## Setup

### 1. Clone the Repository

1) First, clone the project from GitHub:

   ```bash
   git clone https://github.com/otarovvak/django_task.git
   cd django_task

2) Then, create and activate a Virtual Environment:

On Windows:
    python -m venv env
    .\env\Scripts\activate


On macOS/Linux:
    python3 -m venv env
    source env/bin/activate


3) Install dependencies:

    ```bash
    pip install django

4) Create an admin/superuser by running this command:

    ```bash
    python manage.py createsuperuser

5) Run the server:

By running the following command:

python manage.py runserver

6) Access the application:

Once the server is running, you can access the following links:

http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/products/

On this page, you will be able to search products by description, filter products by category, and filter products by tags.