from flask import Flask, request, jsonify
from flask_cors import CORS 
from questions_generator import GCPExamQuestionGenerator

app = Flask('Certibot')
CORS(app)

exams_by_company = {
    'Google': ['Professional Data Engineer', 'Cloud Architect', 'Associate Cloud Engineer'],
    'AWS': ['Solutions Architect', 'Developer Associate', 'SysOps Administrator'],
    'Microsoft': ['Azure Fundamentals', 'Azure Administrator', 'Azure Developer']
}

# Mock data for exam outlines
exam_outlines = {
    'Professional Data Engineer' : {
            'Section 1': """Designing Data Processing Systems
            - Security and Compliance: IAM, Data Security, Privacy, Regional Data Considerations, Compliance
            - Reliability and Fidelity: Data Cleaning, Monitoring Data Pipelines, Disaster Recovery, ACID Compliance, Data Validation
            - Flexibility and Portability: Mapping Business Requirements, Data/Application Portability, Data Staging/Cataloging
            - Data Migrations: Analyzing Stakeholder Needs, Migration Planning, Validation Strategy, Project/Dataset/Table Architecture""",

            'Section 2': """Ingesting and Processing Data
            - Planning Data Pipelines: Data Sources/Sinks, Transformation Logic, Networking, Encryption
            - Building Pipelines: Data Cleansing, Service Identification, Transformations (Batch/Streaming), Data Acquisition
            - Deploying Pipelines: Job Automation, CI/CD""",

            'Section 3': """Storing Data
            - Selecting Storage Systems: Data Access Patterns, Managed Services, Storage Costs/Performance, Data Lifecycle
            - Data Warehouse Usage: Data Model Design, Data Normalization, Business Requirements, Architecture for Data Access
            - Data Lakes: Management, Processing, Monitoring
            - Data Mesh: Building Data Mesh, Segmenting Data, Federated Governance Model""",

            'Section 4': """Preparing and Using Data for Analysis
            - Data Preparation for Visualization: Tool Connections, Field Pre-calculation, BigQuery Materialized Views, Granularity of Time Data
            - Sharing Data: Data Sharing Rules, Publishing Datasets/Reports, Analytics Hub
            - Data Exploration and Analysis: Data Preparation for Feature Engineering, Data Discovery""",

            'Section 5': """Maintaining and Automating Data Workloads
            - Optimizing Resources: Minimizing Costs, Resource Availability, Persistent/Job-based Data Clusters
            - Designing Automation: Creating DAGs, Scheduling Jobs
            - Organizing Workloads: Pricing Models, Job Types
            - Monitoring and Troubleshooting: Observability, Usage Monitoring, Troubleshooting, Workload Management
            - Failure Awareness: Fault Tolerance, Multi-region Job Runs, Data Corruption Handling, Replication/Failover"""
    }
}
# Temporary storage for selected exam details
selected_exam_details = {}

@app.route('/companies', methods=['GET'])
def get_companies():
    companies = list(exams_by_company.keys())
    return jsonify(companies)

@app.route('/exams/<company>', methods=['GET'])
def get_exams_for_company(company):
    if company in exams_by_company:
        exams = exams_by_company[company]
        return jsonify(exams)
    else:
        return jsonify({"error": "Company not found"}), 404


@app.route('/exam_selection', methods=['POST'])
def exam_selection():
    global selected_exam_details
    data = request.get_json()
    certifier = data.get('certifier')
    exam_name = data.get('exam_name')
    exam_outline = data.get('exam_outline')

    # Store the selected exam details
    selected_exam_details = {
        "certifier": certifier,
        "exam_name": exam_name,
        "exam_outline": exam_outline
    }

    return jsonify({"message": "Exam selection received", "data": data})

@app.route('/exam_outline_sections', methods=['GET'])
def exam_outline_sections():
    global selected_exam_details
    exam_name = selected_exam_details.get('exam_name')
    
    # Fetch the outline for the selected exam
    outline = exam_outlines.get(exam_name, {})
    return jsonify(outline)


@app.route('/generate_questions_for_sections', methods=['POST'])
def generate_questions_for_sections():
    selected_sections = request.get_json()

    question_generator = GCPExamQuestionGenerator(exam_outline=exam_outlines["Professional Data Engineer"])

    # Structure to hold the questions for each section
    section_questions = {}

    for section in selected_sections.values():
        try:
            # Generate questions for the selected section
            generated_questions = question_generator.based_on_outline(section)
            # Add the generated questions to the corresponding section
            section_questions[section] = generated_questions
        except ValueError as e:
            section_questions[section] = str(e)

    # Return the structured response as JSON
    return jsonify(section_questions)

if __name__ == '__main__':
    app.run(debug=True)
