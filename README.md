# Certibot Flask Application

## Overview
Certibot is a Flask-based application designed to assist users in preparing for various certification exams, with a focus on tech giants like Google, AWS, and Microsoft. It provides functionalities to select exams, review exam outlines, and generate practice questions.

## API Endpoints

### Home Screen
- **Endpoint:** `/`
- **Method:** GET
- **Description:** Displays a welcome message.
- **Example Request:**
  `curl http://localhost:5000/`
- **Response:** "Welcome to Certibot!"

### Get Companies
- **Endpoint:** `/companies`
- **Method:** GET
- **Description:** Lists all certifying companies.
- **Example Request:**
  `curl http://localhost:5000/companies`
- **Response:** `["Google", "AWS", "Microsoft"]`

### Get Exams for Company
- **Endpoint:** `/exams/<company>`
- **Method:** GET
- **Description:** Lists available exams for the selected company.
- **Example Request:**
  `curl http://localhost:5000/exams/Google`
- **Response:**
  `["Associate Cloud Engineer", "Professional Data Engineer", ...]`

### Exam Selection
- **Endpoint:** `/exam_selection`
- **Method:** POST
- **Description:** Selects an exam for generating questions.
- **Input:**
  `{"certifier": "Google",
  "exam_name": "Professional Data Engineer",
  "exam_outline": "sections"}`
- **Example Request:**
  `curl -X POST http://localhost:5000/exam_selection
-H "Content-Type: application/json"
-d '{"certifier": "Google", "exam_name": "Professional Data Engineer", "exam_outline": "sections"}'`
- **Response:**
  `{
  "data": {
    "certifier": "GCP",
    "exam_name": "Professional Data Engineer",
    "exam_outline": "topics"
  },
  "message": "Exam selection received"
}`

### Exam Outline Sections
- **Endpoint:** `/exam_outline_sections`
- **Method:** GET
- **Description:** Retrieves the outline of the selected exam.
- **Example Request:**
  `curl http://localhost:5000/exam_outline_sections`
- **Response:**
  `{ "Section 1": "Designing Data Processing Systems ...", ... }`

### Generate Questions for Sections
- **Endpoint:** `/generate_questions_for_sections`
- **Method:** POST
- **Description:** Generates 5 questions for each selected exam sections.
- **Input:**
  `{"1": "Section 1", "2": "Section 2"}`
- **Example Request:**
  `curl -X POST http://localhost:5000/generate_questions_for_sections
-H "Content-Type: application/json"
-d '{"1": "Section 1", "2": "Section 2"}'`
- **Response:**
  `{
  "Section 1": [
    {
      "options": {
        "a": "Google Cloud Storage with IAM policies.",
        "b": "Cloud Data Loss Prevention (DLP) API.",
        "c": "Cloud Identity-Aware Proxy (IAP).",
        "d": "Cloud Healthcare API with proper IAM configurations."
      },
      "question": "A healthcare company needs to ensure strict adherence to HIPAA regulations and compliance with regional data privacy laws for their global patient information system. They want to avoid hefty fines and legal issues associated with data breaches. Which GCP service should they prioritize for handling IAM and access control to their healthcare data?",
      "solution": {
        "correct_answer": "d",
        "explanation": "The Cloud Healthcare API enables healthcare data solutions with integration that provides support for compliance with HIPAA and other regulations. Configuring IAM correctly would allow the company to control access to sensitive data efficiently while addressing both security and compliance concerns."
      }
    }, ... << 4 more >>
  ],
  "Section 2": {
    "questions": [
      {
        "options": {
          "a": "Use Cloud Storage as a data sink, with Compute Engine instances running Apache NiFi to ingest and transfer logs.",
          "b": "Utilize Pub/Sub for log ingestion, Dataflow for stream processing, and BigQuery for analysis.",
          "c": "Set up a managed instance group of Compute Engine VMs that run custom-built log ingestion services to Bigtable.",
          "d": "Employ Cloud Dataprep to collect logs and Cloud SQL to store the logs for the analysis."
        },
        "question": "A company wants to build a data pipeline that collects logs from hundreds of servers in multiple global data centers and centralizes the logs for analysis. Which combination of services would best facilitate a scalable and secure solution within the Google Cloud Platform?",
        "solution": {
          "answer": "b",
          "explanation": "Option B offers a scalable and secure method that is fully managed in GCP. Pub/Sub allows for global ingestion of messages, Dataflow can process the streams in a scalable manner, and BigQuery provides a powerful analytics engine that scales automatically."
        }
      }, ... << 4 more >>]`

### Exam Outline Key Topics
- **Endpoint:** `/exam_outline_key_topics`
- **Method:** GET
- **Description:** Retrieves key topics for the selected exam outline.
- **Example Request:** `curl http://localhost:5000/exam_outline_key_topics`
- **Response:** Returns key topics relevant to the selected exam, formatted as a JSON array.
- **Example Response:**
  `{
  "key_topics": [
    "Security and Compliance",
    " Data Migrations",
    " Data Lake Management",
    " Data Preparation for Visualization",
    " Optimizing Resources"
  ]
}`

### Generate Questions for Topics
- **Endpoint:** `/generate_questions_for_topics`
- **Method:** POST
- **Description:** Generates 5 questions for each of the provided topics for the selected exam.
- **Input:** JSON object with a list of topics under the key `"topics"`.
- **Example Request:** `curl -X POST http://localhost:5000/generate_questions_for_topics
-H "Content-Type: application/json"
-d '{"topics": ["IAM", "Data Lakes", "BigQuery"]}'`
- **Response:** JSON object containing generated questions for each topic provided.
- **Example Response:** `{
"{
  "BigQuery": [
    {
      "options": {
        "A": "Use BigQuery's Data Loss Prevention (DLP) API to automatically detect and redact PII while data is being inserted into BigQuery.",
        "B": "Create authorized views in BigQuery that exclude PII columns from the analysts' view and grant analysts access to these views instead of the base tables.,
        "C": "Leverage Cloud Dataflow to preprocess the data, mask PII, and then store the results in a separate BigQuery dataset for analysts.",
        "D": "Implement row-level security in BigQuery to filter out any rows that contain PII from the results that analysts can see."
      },
      "question": "A financial institution uses BigQuery as their data warehouse and needs to ensure that personally identifiable information (PII) within their datases is masked before analysts can query the data. What should they implement to meet this requirement while ensuring analysts can still perform their tasks?",
      "solution": {
        "answer": "B",
        "explanation": "Authorized views in BigQuery allow administrators to create views that exclude sensitive PII, which can then be shared with analysts. This ensues that the underlying data is protected while still allowing analysts to query non-sensitive data."
      }, ... << 4 more >>
  ],
  "Data Lakes": [
    {
      "options": {
        "A": "Use BigQuery for storage, Dataflow for stream processing, and Cloud Dataproc for batch processing.",
        "B": "Utilize Cloud Storage as the data lake storage, Pub/Sub for real-time streams, Cloud Dataflow for both stream and batch processing, and BigQuery for analytics.",
        "C": "Deploy Cloud Spanner for real-time data storage, Cloud Dataprep for data cleaning, and Cloud ML Engine for analytics.",
        "D": "Implement Cloud Bigtable for batch processing storage, Cloud Composer for workflow management, and Data Studio for visualization and analytics."
      },
      "question": "A company is building a data lake in GCP to handle various types of data, including real-time streams and batch processing for analytics purposes. They require the data lake to be highly scalable and cost-effective. They want to ensure that the data remains secure and that access is properly managed according to company policies. Which GCP services should be combined to meet these requirements?",
      "solution": {
        "answer": "B",
        "explanation": "Cloud Storage is an excellent fit for scalable and cost-effective data lake storage. Pub/Sub can handle real-time data streams effectively, and Dataflow can process both streams and batch data. BigQuery is a powerful tool for analytics queries on large datasets. Together, these services fulfill the scalability, cost-effectiveness, security, and access management requirements for the data lake."
      }
    }, ... << 4 more >>
  ],
  "IAM": [
    {
      "options": {
        "A": "Create a custom Role with permissions specific to each department and assign it at the organization level.",
        "B": "Create a custom IAM policy and apply it at the project level for each department.",
        "C": "Use predefined roles and assign them to individual users based on their department.",
        "D": "Set up IAM Conditional Role Binding with conditions that match the department attribute in users' profiles."
      },
      "question": "A company has a requirement to enhance security by ensuring that their cloud resources are only accessible by team members within a specific department. The company's organizational structure comprises various departments such as Sales, Marketing, and Engineering, and they use Google Cloud Platform for their infrastructure. As the GCP Data Engineer, you are tasked with designing an IAM policy that aligns with this requirement. Which of the following approaches best satisfies this requirement?",
      "solution": {
        "answer": "D",
        "explanation": "Using IAM Conditional Role Binding allows binding roles to users or groups with conditions that can be set to match custom attributes like department fields within the user's profile. This approach will ensure that only users from specific departments can access the cloud resources, satisfying the requirement or enhanced security."
      }
    }, ... << 4 more >>
  ]
}`

## Running the Application

Ensure you have Python 3 and Flask installed. Navigate to the application directory and activate the virtual environment:

- **Unix/MacOS:**
`source myenv/bin/activate`

- **Windows:**
`source myenv\Scripts\activate`

Run the application:
`python app.py`

You can then use `curl` or any HTTP client to interact with the API endpoints as demonstrated.

## Testing Endpoints

Use the `curl` commands provided under each endpoint section to test the functionality of the Certibot application. Replace `localhost:5000` with the `https://cert-bot-dev.ew.r.appspot.com/` address to access the hosted application. Running the hosted address eliminates the need to run the python script locally. 

