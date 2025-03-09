# FastAPI Blog App 📝

A simple blog application built using **FastAPI** that demonstrates basic **CRUD (Create, Read, Update, Delete)** operations with authentication and SQLite as the database.

## 📋 Overview

This app allows users to:

-   **Create** a new user account and log in to receive a JWT token.
-   **Create** new blog posts if authenticated.
-   **Read** all blog posts or a specific post by ID.
-   **Update** blog posts if authenticated as the author.
-   **Delete** blog posts if authenticated as the author.

----------

## 🛠 Setup and Installation

### 1. Clone the Repository

```
git clone <your-repository-url>
cd BlogApp
``` 

### 2. Create a Virtual Environment

```
python3 -m venv venv
``` 

### 3. Activate the Virtual Environment

-   **On macOS/Linux:**
    
    ```
    source venv/bin/activate
    ``` 

### 4. Install the Requirements

```
pip install -r requirements.txt
``` 

### 5. Run the Server

```
uvicorn main:app --reload
``` 

-   The app will be available at: http://127.0.0.1:8000

----------

## 🔒 Authentication

-   Uses JWT (JSON Web Tokens) for secure authentication.
-   Token is required for creating, updating, and deleting blog posts.
-   Include the token in the header as:
    
    ```
    Authorization: Bearer <your_jwt_token>
    ``` 

----------

## 🗄 Database

-   Uses **SQLite** for storing users and blog posts.
-   Database file: `blog.db`

----------

## 🛠️ Future Improvements

-   Add more advanced filtering and searching for blog posts.
-   Implement role-based access control.
-   Enhance error handling and validation.

----------

## 🤝 Contributing

Feel free to fork the repo and submit pull requests. Contributions are always welcome!

----------
