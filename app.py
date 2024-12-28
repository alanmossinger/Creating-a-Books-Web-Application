from flask import Flask, request, render_template, make_response, jsonify
from functools import wraps
import os
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
    JWTManager,
    set_access_cookies,
)

# Initialize Flask app
app = Flask(__name__)

# Flask configuration for JWT and file uploads
app.config["JWT_SECRET_KEY"] = "secretkey"  # Secret key for JWT
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]  # Store JWT in cookies
app.config["JWT_COOKIE_SECURE"] = False  # Secure cookies only for HTTPS
app.config["JWT_COOKIE_CSRF_PROTECT"] = False  # Disable CSRF for simplicity
app.config["UPLOADED_PHOTOS_DEST"] = "static"  # Directory for uploaded images
jwt = JWTManager(app)

# Book collection with two additional books
books = [
    {
        "id": 1,
        "author": "Eric Reis",
        "country": "USA",
        "language": "English",
        "title": "Lean Startup",
        "year": 2011,
        "cover": "static/image1.png",
    },
    {
        "id": 2,
        "author": "Mark Schwartz",
        "country": "USA",
        "language": "English",
        "title": "A Seat at the Table",
        "year": 2017,
        "cover": "static/image2.png",
    },
    {
        "id": 3,
        "author": "James Womak",
        "country": "USA",
        "language": "English",
        "title": "Lean Thinking",
        "year": 1996,
        "cover": "static/image3.png",
    },
    {
        "id": 4,
        "author": "F. Scott Fitzgerald",
        "country": "USA",
        "language": "English",
        "title": "The Great Gatsby",
        "year": 1925,
        "cover": "static/image4.png",
    },
    {
        "id": 5,
        "author": "Herman Melville",
        "country": "USA",
        "language": "English",
        "title": "Moby Dick",
        "year": 1851,
        "cover": "static/image5.png",
    },
]

# User collection with additional users
users = [
    {"username": "testuser", "password": "testuser", "role": "admin"},
    {"username": "John", "password": "John", "role": "reader"},
    {"username": "Anne", "password": "Anne", "role": "admin"},
    {"username": "Sam", "password": "Sam123", "role": "reader"},
    {"username": "Lisa", "password": "Lisa456", "role": "admin"},
]

# Helper function to check user credentials
def check_user(username, password):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return {"username": user["username"], "role": user["role"]}
    return None

# Decorator to restrict access to admin users
def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        user = get_jwt_identity()
        for u in users:
            if u["username"] == user and u["role"] == "admin":
                return fn(*args, **kwargs)
        return jsonify(msg="Admins only!"), 403
    return wrapper

# Landing page
@app.route("/", methods=["GET"])
def home():
    return render_template("register.html")

# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        valid_user = check_user(username, password)
        if valid_user:
            access_token = create_access_token(identity=username)
            response = make_response(render_template("index.html", username=username, books=books))
            set_access_cookies(response, access_token)  # Set JWT as a cookie
            return response
    return render_template("register.html")

# Logout route
@app.route("/logout", methods=["GET"])
def logout():
    response = make_response("Logged Out")  # Simple logout response
    response.delete_cookie("access_token_cookie")  # Remove JWT cookie
    return response

# View books
@app.route("/books", methods=["GET"])
@jwt_required()
def get_books():
    username = get_jwt_identity()
    return render_template("books.html", username=username, books=books)

# Add a book (admin only)
@app.route("/addbook", methods=["GET", "POST"])
@jwt_required()
@admin_required
def add_book():
    username = get_jwt_identity()
    if request.method == "GET":
        return render_template("addBook.html", username=username)
    if request.method == "POST":
        author = request.form.get("author")
        title = request.form.get("title")
        new_book = {
            "id": len(books) + 1,
            "author": author,
            "title": title,
            "cover": f"static/image{len(books) + 1}.png",
        }
        books.append(new_book)
        return render_template("books.html", books=books, username=username)

# Add an image (admin only)
@app.route("/addimage", methods=["GET", "POST"])
@jwt_required()
@admin_required
def add_image():
    if request.method == "GET":
        return render_template("addImage.html")
    if request.method == "POST":
        image = request.files["image"]
        book_id = request.form.get("number")
        image_path = f"static/image{book_id}.png"
        image.save(os.path.join(app.config["UPLOADED_PHOTOS_DEST"], image_path))
        return "Image uploaded successfully!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

