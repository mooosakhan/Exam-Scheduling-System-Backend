# 📚 Exam Scheduling System 🎓

## Description
The **Exam Scheduling System** is a powerful web application designed to simplify and automate the process of scheduling exams for universities. Built with Flask, this backend application provides seamless management of teachers, exams, subjects, departments, and classrooms, ensuring efficient and conflict-free scheduling. 🌟

## Features 🚀
- **🔐 User Authentication**: Secure login for administrators and teachers using token-based authentication.
- **📝 CRUD Operations**: Manage teachers, exams, subjects, departments, and classrooms effortlessly.
- **🗓️ Scheduling**: Create timetables, assign teachers, and allocate classrooms with ease.
- **⚠️ Conflict Management**: Automatic detection and resolution of scheduling conflicts.
- **📱 Responsive Design**: User-friendly across all devices.

## Technologies Used 🛠️
- **Flask**: A lightweight Python web framework.
- **SQLAlchemy**: Powerful SQL toolkit and ORM.
- **MySQL**: Reliable relational database management system.
- **JWT**: Secure JSON Web Tokens for authentication.
- **Flask-RESTful**: Quickly build REST APIs.

## Installation 🛠️
1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/exam-scheduling-system.git
   cd exam-scheduling-system
   ```

2. **Create a virtual environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   - Ensure MySQL is installed and running.
   - Create a new database for the project.
   - Update the database URI in `config.py` with your database credentials.

5. **Run the application**:
   ```sh
   flask run
   ```

## Usage 🖥️
- **Admin Dashboard**: Manage teachers, exams, subjects, departments, and classrooms.
- **Schedule Creation**: Assign teachers to exams, allocate classrooms, and set exam times.
- **Conflict Management**: System automatically handles conflicts and ensures no overlaps.

## API Endpoints 🌐
- **🔑 Authentication**: `/auth/login`, `/auth/register`
- **👩‍🏫 Teachers**: `/teachers`, `/teachers/<id>`
- **📅 Exams**: `/exams`, `/exams/<id>`
- **📚 Subjects**: `/subjects`, `/subjects/<id>`
- **🏢 Departments**: `/departments`, `/departments/<id>`
- **🏫 Classrooms**: `/classrooms`, `/classrooms/<id>`
- **📋 Scheduling**: `/schedule`

## Contact 📧
For any inquiries or feedback, please contact:
- **Name**: Moosa 
- **Email**: moosakhan3856902@gmail.com

## Screenshots 📸
![Dashboard](screenshots/dashboard.png)
![Scheduling](screenshots/scheduling.png)

---
