Creating a Books Web Application
Overview
This project is a Flask-based web application designed to manage a collection of books. It demonstrates the use of modern web development practices, including JWT-based authentication and role-based access control, to build a secure and functional system. The application includes features for user management, book listing, and administrative functions such as adding new books and uploading cover images.

Features
User Authentication and Roles:

Supports user login and logout with JWT authentication stored in cookies.
Implements role-based access control to restrict specific functionalities to admin users only.
Book Management:

Displays a list of books with their authors, titles, publication years, and cover images.
Admin users can add new books and upload corresponding cover images.
Secure File Handling:

Ensures all uploaded images are securely stored in the static folder.
Dynamic Web Pages:

Uses Flask templates (Jinja2) to dynamically render HTML pages for user interaction.
Technology Stack
Backend: Python with Flask
Frontend: HTML, CSS (Bootstrap)
Authentication: JSON Web Tokens (JWT)
Database: In-memory lists for users and books
Hosting: Local development environment
How It Works
User Roles:

Admin: Can add books and upload cover images.
Reader: Can view books but has no permissions to modify content.
Key Routes:

/: Landing page for user login.
/login: Allows users to log in and sets JWT for authentication.
/logout: Logs out the user by clearing JWT cookies.
/books: Displays the list of books with their cover images.
/addbook: Admin-only route to add new books.
/addimage: Admin-only route to upload book cover images.
Error Handling:

Non-admin users attempting restricted actions receive a 403 Forbidden error.
Invalid credentials prompt a redirection to the login page.
Setup and Usage
Prerequisites
Python 3.8 or later
Flask and its dependencies installed
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/alanmossinger/Creating-a-Books-Web-Application.git
cd Creating-a-Books-Web-Application
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
python app.py
Open your browser and navigate to:

arduino
Copy code
http://127.0.0.1:5000/
Screenshots
Login Page
Users can log in with their credentials to access the application.

Books List
Displays a list of books with details and cover images.

Admin Features
Admin users can add books and upload cover images through dedicated forms.

Future Improvements
Persistent Storage:
Replace in-memory lists with a database (e.g., SQLite or PostgreSQL) for scalability.
Enhanced User Experience:
Add JavaScript for dynamic updates and improved interactivity.
Deployment:
Deploy the application using cloud platforms like AWS or Heroku.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request for review.

License
This project is licensed under the MIT License.

## Flask and Jinja Web Server

## jrw@mit.edu

Add Bootstrap Navigation and image upload
New routes addbook, addimage

