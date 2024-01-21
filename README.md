# Certibot Flask Application

## Overview
Certibot is a Flask application that facilitates the selection and examination of various certification exams, focusing on companies like Google, AWS, and Microsoft.

## API Endpoints

### Home Screen
- **Endpoint**: `'/'` (GET)
- **Description**: Provides a basic welcome message.
- **Output**: `"Welcome to Certibot!"`

### Get Companies
- **Endpoint**: `'/companies'` (GET)
- **Description**: Retrieves a list of certifying companies.
- **Output**: JSON list of companies.
  - **Example Output**: `["Google", "AWS", "Microsoft"]`

### Get Exams for Company
- **Endpoint**: `'/exams/<company>'` (GET)
- **Description**: Retrieves a list of exams offered by a specific company.
- **Parameters**: `company` (Company name as URL parameter)
- **Output**: JSON list of exams.
  - **Example Input**: `'/exams/Google'`
  - **Example Output**: `["Associate Cloud Engineer", "Professional Data Engineer", ...]`

### Exam Selection
- **Endpoint**: `'/exam_selection'` (POST)
- **Description**: Receives and stores the selected exam details.
- **Input**: JSON object with `certifier`, `exam_name`, and `exam_outline`.
  - **Example Input**:
    ```json
    {
      "certifier": "Google",
      "exam_name": "Professional Data Engineer",
      "exam_outline": "sections"
    }
    ```
- **Output**: Confirmation message with received data.
  - **Example Output**:
    ```json
    {
      "message": "Exam selection received",
      "data": {
        "certifier": "Google",
        "exam_name": "Professional Data Engineer",
        "exam_outline": "sections"
      }
    }
    ```

### Exam Outline Sections
- **Endpoint**: `'/exam_outline_sections'` (GET)
- **Description**: Retrieves the outline for the selected exam.
- **Output**: JSON object with the exam outline.
  - **Example Output**:
    ```json
    {
      "Section 1": "Designing Data Processing Systems ...",
      "Section 2": "Ingesting and Processing Data ...",
      ...
    }
    ```

### Generate Questions for Sections
- **Endpoint**: `'/generate_questions_for_sections'` (POST)
- **Description**: Generates exam questions for selected sections.
- **Input**: JSON object with selected section names.
  - **Example Input**:
    ```json
    {
      "1": "Section 1",
      "2": "Section 2"
    }
    ```
- **Output**: JSON object with generated questions for each section.
  - **Example Output**:
    ```json
    {
      "Section 1": "Generated questions for Section 1 ...",
      "Section 2": "Generated questions for Section 2 ..."
    }
    ```

## Usage Flow
1. Access the root URL to receive a welcome message.
2. Retrieve the list of certifying companies via `'/companies'`.
3. Select a company and fetch available exams using `'/exams/<company>'`.
4. Submit the chosen exam details to `'/exam_selection'`.
5. Retrieve the outline of the selected exam from `'/exam_outline_sections'`.
6. Generate questions for specific sections using `'/generate_questions_for_sections'`.
