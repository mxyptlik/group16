README
Employee and Project Management System
Overview
The Employee and Project Management System is a web-based application with the following functionalities:

Employees can join projects.
Managers can create and manage projects.
Users can register to become employees and add dependents.
This system emphasizes database design and normalization, ensuring data integrity, efficiency, and scalability.

Key Features
Employee Functionality:

Register as an employee.
Join availct based on project ID.
Manage dependents.
Manager Functionality:

Create new projects.
employees can join projects.
Database Design:

Fully normalized database using MySQL to prevent redundancy and maintain data consistency.
Key relationships include:
Employees ↔ Projects (Many-to-Many)
Employees ↔ Dependents (One-to-Many)
Technology Stack
Frontend:
HTML, CSS
Backend:
Django (Python)
Database:
MySQL
Installation Guide
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/employee-project-management
cd employee-project-management
Set up a virtual environment and install dependencies:

bash
Copy code
python -m venv env
source env/bin/activate  # For Linux/Mac
env\Scripts\activate     # For Windows
pip install -r requirements.txt
Configure the MySQL database:

Create a new database in MySQL.
Update settings.py with your database credentials:
python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Run database migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Start the development server:

bash
Copy code
python manage.py runserver
Access the application at http://127.0.0.1:8000.

Usage
Managers:

Sign up and log in.
Navigate to the Projects section to create and manage projects.
Employees:

Register as an employee.
View available projects and join them.
Add dependents via the Dependents section.
Database Schema Highlights
Tables:

Users: Stores general user data.
Employees: Extends user data with employee-specific details.
Dependents: Links to employees for dependent information.
Projects: Contains project details.
EmployeeProjects: Many-to-Many relationship between employees and projects.
Normalization:

Ensures no redundant data.
Relationships designed to follow 3rd Normal Form (3NF).
Future Enhancements
Add task-level management within projects.
Integrate REST APIs for external system compatibility.
Implement role-based access control for enhanced security.
Contributing
Contributions are welcome! Submit a pull request or raise an issue for any feature requests or bugs.

License
This project is licensed under the MIT License. See LICENSE for details.

