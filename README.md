# Certibot Flask Application

## Overview
Certibot is a Flask-based application designed to assist users in preparing for various certification exams, with a focus on tech giants like Google, AWS, and Microsoft. It provides functionalities to select exams, review exam outlines, and generate practice questions.

## API Endpoints

### Home Screen
- **Endpoint:** `/`
- **Method:** GET
- **Description:** Displays a welcome message.
- **Example Request:** `curl http://localhost:5000/`
- **Response:** "Welcome to Certibot!"

### Get Companies
- **Endpoint:** `/companies`
- **Method:** GET
- **Description:** Lists all certifying companies.
- **Example Request:** `curl http://localhost:5000/companies`
- **Response:** `["Google", "AWS", "Microsoft"]`

### Get Exams for Company
- **Endpoint:** `/exams/<company>`
- **Method:** GET
- **Description:** Lists available exams for the selected company.
- **Example Request:** `curl http://localhost:5000/exams/Google`
- **Response:** `["Associate Cloud Engineer", "Professional Data Engineer", ...]`

### Exam Selection
- **Endpoint:** `/exam_selection`
- **Method:** POST
- **Description:** Selects an exam for generating questions.
- **Input:** `{"certifier": "Google", "exam_name": "Professional Data Engineer", "exam_outline": "sections"}`
- **Example Request:**

curl -X POST http://localhost:5000/exam_selection
-H "Content-Type: application/json"
-d '{"certifier": "Google", "exam_name": "Professional Data Engineer", "exam_outline": "sections"}'

- **Response:** `{"message": "Exam selection received", "data": ...}`

### Exam Outline Sections
- **Endpoint:** `/exam_outline_sections`
- **Method:** GET
- **Description:** Retrieves the outline of the selected exam.
- **Example Request:** `curl http://localhost:5000/exam_outline_sections`
- **Response:** `{ "Section 1": "Designing Data Processing Systems ...", ... }`

### Generate Questions for Sections
- **Endpoint:** `/generate_questions_for_sections`
- **Method:** POST
- **Description:** Generates questions for the selected exam sections.
- **Input:** `{"1": "Section 1", "2": "Section 2"}`
- **Example Request:**

curl -X POST http://localhost:5000/generate_questions_for_sections
-H "Content-Type: application/json"
-d '{"1": "Section 1", "2": "Section 2"}'

- **Response:** `{ "Section 1": "...questions...", "Section 2": "...questions..." }`

### Exam Outline Key Topics
- **Endpoint:** `/exam_outline_key_topics`
- **Method:** GET
- **Description:** Retrieves key topics for the selected exam outline.
- **Example Request:** `curl http://localhost:5000/exam_outline_key_topics`
- **Response:** Returns key topics relevant to the selected exam, formatted as a JSON array.
- **Example Response:** `{"key_topics": ["IAM", "Data Lakes", "BigQuery"]}`

### Generate Questions for Topics
- **Endpoint:** `/generate_questions_for_topics`
- **Method:** POST
- **Description:** Generates questions based on provided topics for the selected exam.
- **Input:** JSON object with a list of topics under the key `"topics"`.
- **Example Request:**

## Running the Application

Ensure you have Python 3 and Flask installed. Navigate to the application directory and activate the virtual environment:

- **Unix/MacOS:**
source myenv/bin/activate

- **Windows:**
myenv\Scripts\activate

Run the application:
python app.py

You can then use `curl` or any HTTP client to interact with the API endpoints as demonstrated.

## Testing Endpoints

Use the `curl` commands provided under each endpoint section to test the functionality of the Certibot application. Replace `localhost:5000` with your server's address if you're hosting the application elsewhere.
