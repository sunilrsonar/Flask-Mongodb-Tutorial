# Flask MongoDB Assignment

This is a simple Flask web application that connects to a MongoDB database. It allows users to submit their name and password through a form and view the submitted data.

## Features

- Connects to MongoDB using `pymongo`.
- Loads environment variables securely using `python-dotenv`.
- Provides a simple form to submit data (name and password).
- Displays all stored data in JSON format.

## Tech Stack

- **Backend**: Python, Flask
- **Database**: MongoDB
- **Others**: dotenv for environment variable management

---

## Project Structure

```
.
├── app.py               # Main Flask application
├── .env                 # Environment variables (MongoDB connection URI)
├── requirement.txt      # Python dependencies
└── templates/
    └── index.html       # HTML form (not provided in this upload)
```

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirement.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root with the following content:
```
MONGODB_URI=mongodb+srv://<username>:<password>@<cluster-url>/?retryWrites=true&w=majority&appName=Cluster0
```
> sample `.env` file:
```
MONGODB_URI=mongodb+srv://dummy:1234@cluster0.o2qx5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
```
Replace `dummy` and `1234` with your actual MongoDB credentials.

### 5. Run the Application
```bash
python app.py
```

The application will be running on `http://127.0.0.1:5000/` by default.

---

## Endpoints

| Route      | Method | Description                      |
|------------|--------|----------------------------------|
| `/`        | GET    | Displays the index page (form).  |
| `/submit`  | POST   | Submits `name` and `password` to MongoDB. |
| `/view`    | GET    | Returns all submitted data in JSON (excluding `_id`). |

---

## Example Usage

### Submit Data
- Visit `http://127.0.0.1:5000/`
- Fill out the form and submit.

### View Data
- Go to `http://127.0.0.1:5000/view`
- You'll see a JSON response with all submitted entries.

---

## Dependencies

From `requirement.txt`:
- `flask`
- `pymongo`
- `dnspython`
- `python-dotenv`

Install them using:
```bash
pip install -r requirement.txt
```

---

## Notes
- The MongoDB connection uses a **ping** command to verify connectivity.
- Passwords are stored in plain text in the database for demonstration purposes. **This should not be used in production** without proper encryption and security practices.

---

## Author

Sunil Sonar
Email : sunil.r.sonar@gmail.com

## License

This project is for educational/demo purposes.
