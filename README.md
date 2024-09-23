# Flask Test Project

This is a simple Flask project with the following functionalities:
- Get user info via query parameters
- Post user info and return interpolated strings
- Upload a file and return its content

## Project Structure
```
bash
.
├── app.py              # Main Flask application file
├── static/             # Folder for static uploads
└── templates/
    └── index.html      # HTML file for the upload interface
```

## Routes

### 1. `/users` (GET)
This route takes two query parameters (`name` and `appName`) and returns a greeting message.

#### Example request:
```
GET /users?name=John&appName=FlaskApp
```

#### Example response:
```
Hello John, welcome to FlaskApp!
```

### 2. `/users` (POST)
This route also takes two query parameters (`name` and `appName`), and returns a personalized thank you message.

#### Example request:
```
POST /users?name=John&appName=FlaskApp
```

#### Example response:
```
Thank you for posting on FlaskApp, John!
```

### 3. `/` (GET/POST)
- **GET**: Renders an `index.html` page that allows file uploads.
- **POST**: Accepts a file upload, reads its content, and returns the file content in plain text.

#### Example request:
- Upload a file using the form on `index.html`.

#### Example response:
- Returns the content of the uploaded file as plain text.

## Setup Instructions

### 1. Clone the repository:
```bash
git clone <repository-url>
```

### 2. Install dependencies:
```bash
pip install Flask
```

### 3. Run the app:
```bash
flask run
```

### 4. Access the app:
Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Project Configuration

- **UPLOAD_FOLDER**: The folder where files are uploaded and stored (`static/uploads/`).

## Notes

- Ensure you have a file named `index.html` under the `templates/` directory for the file upload form.
- Use tools like Postman or Curl to test the GET and POST routes on `/users`.


This file provides an overview of the project, its functionality, and instructions on how to run and interact with it.

