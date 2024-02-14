from flask import Flask, request, jsonify
from flask_cors import CORS 
from modules.questions_generator import ExamQuestionGenerator
import json

app = Flask('Certibot')
CORS(app)

exams_by_company = {
    'GCP': ["Associate Cloud Engineer", 
               "Professional Cloud Architect", 
               "Professional Data Engineer",
               "Professional Cloud Developer",
               "Professional Cloud Network Engineer",
               "Professional Cloud Security Engineer",
               "Professional Collaboration Engineer",
               "Professional Machine Learning Engineer",
               "Professional Cloud Database Engineer",
               "Looker Business Analyst",
               "Looker Developer",
               "Looker LookML Developer",
               "G Suite Certification"],
    'AWS': ["AWS Certified Cloud Practitioner",
            "AWS Certified Solutions Architect – Associate",
            "AWS Certified Developer – Associate",
            "AWS Certified SysOps Administrator – Associate",
            "AWS Certified Solutions Architect – Professional",
            "AWS Certified DevOps Engineer – Professional",
            "AWS Certified Security – Specialty",
            "AWS Certified Big Data – Specialty",
            "AWS Certified Advanced Networking – Specialty",
            "AWS Certified Machine Learning – Specialty",
            "AWS Certified Database – Specialty",
            "AWS Certified Data Analytics – Specialty"],
    'Microsoft': ["Microsoft Certified: Azure Fundamentals",
                  "Microsoft Certified: Azure Data Fundamentals",
                  "Microsoft Certified: Azure AI Fundamentals",
                  "Microsoft Certified: Azure Administrator Associate",
                  "Microsoft Certified: Azure Developer Associate",
                  "Microsoft Certified: Azure Security Engineer Associate",
                  "Microsoft Certified: Azure AI Engineer Associate",
                  "Microsoft Certified: Azure Data Scientist Associate",
                  "Microsoft Certified: Azure Data Engineer Associate",
                  "Microsoft Certified: Azure Database Administrator Associate",
                  "Microsoft Certified: Azure Solutions Architect Expert",
                  "Microsoft Certified: Azure DevOps Engineer Expert",
                  "Microsoft Certified: Security, Compliance, and Identity Fundamentals",
                  "Microsoft Certified: Security Operations Analyst Associate",
                  "Microsoft Certified: Identity and Access Administrator Associate",
                  "Microsoft Certified: Information Protection Administrator Associate",
                  "Microsoft Certified: Windows Server Hybrid Administrator Associate"]
}

# Mock data for exam outlines
exam_outlines = {
    'GCP': {'Professional Data Engineer': {
        'Section 1': "Designing Data Processing Systems:- Security and Compliance: IAM, Data Security, Privacy, Regional Data Considerations, Compliance. Reliability and Fidelity: Data Cleaning, Monitoring Data Pipelines, Disaster Recovery, ACID Compliance, Data Validation. Flexibility and Portability: Mapping Business Requirements, Data/Application Portability, Data Staging/Cataloging. Data Migrations: Analyzing Stakeholder Needs, Migration Planning, Validation Strategy, Project/Dataset/Table Architecture.",
        'Section 2': "Ingesting and Processing Data:- Planning Data Pipelines: Data Sources/Sinks, Transformation Logic, Networking, Encryption. Building Pipelines: Data Cleansing, Service Identification, Transformations (Batch/Streaming), Data Acquisition. Deploying Pipelines: Job Automation, CI/CD.",
        'Section 3': "Storing Data:- Selecting Storage Systems: Data Access Patterns, Managed Services, Storage Costs/Performance, Data Lifecycle. Data Warehouse Usage: Data Model Design, Data Normalization, Business Requirements, Architecture for Data Access. Data Lakes: Management, Processing, Monitoring. Data Mesh: Building Data Mesh, Segmenting Data, Federated Governance Model.",
        'Section 4': "Preparing and Using Data for Analysis:- Data Preparation for Visualization: Tool Connections, Field Pre-calculation, BigQuery Materialized Views, Granularity of Time Data. Sharing Data: Data Sharing Rules, Publishing Datasets/Reports, Analytics Hub. Data Exploration and Analysis: Data Preparation for Feature Engineering, Data Discovery.",
        'Section 5': "Maintaining and Automating Data Workloads:- Optimizing Resources: Minimizing Costs, Resource Availability, Persistent/Job-based Data Clusters. Designing Automation: Creating DAGs, Scheduling Jobs. Organizing Workloads: Pricing Models, Job Types. Monitoring and Troubleshooting: Observability, Usage Monitoring, Troubleshooting, Workload Management. Failure Awareness: Fault Tolerance, Multi-region Job Runs, Data Corruption Handling, Replication/Failover."
    },
        "Associate Cloud Engineer": {
        "Section 1": "Setting up cloud projects and accounts. Managing billing configuration. Installing and configuring the command line interface (CLI).",
        "Section 2": "Planning and estimating GCP product use using the Pricing Calculator. Planning and configuring compute resources, data storage options, and network resources.",
        "Section 3": "Deploying and implementing Compute Engine resources, Google Kubernetes Engine resources, App Engine, Cloud Run, and Cloud Functions resources. Deploying and implementing data solutions and networking resources.",
        "Section 4": "Managing Compute Engine resources. Managing Google Kubernetes Engine resources. Managing App Engine and Cloud Run resources. Managing storage and database solutions. Managing networking resources. Monitoring and logging.",
        "Section 5": "Managing identity and access management (IAM). Managing service accounts. Viewing audit logs for project and managed services."
    },
        "Professional Cloud Architect": {
        "Section 1": "Designing and planning a cloud solution architecture includes designing a solution infrastructure that meets business requirements with considerations for business use cases, product strategy, cost optimization, supporting application design, integration with external systems, movement of data, design decision trade-offs, success measurements, compliance, and observability.",
        "Section 2": "Managing and provisioning a solution infrastructure involves configuring network topologies, extending to on-premises or multicloud environments, security protection, configuring individual storage systems, data storage allocation, compute provisioning, security and access management, network configuration for data transfer and latency, data retention, life cycle management, data growth management, and configuring compute systems.",
        "Section 3": "Designing for security and compliance focuses on identity and access management, resource hierarchy, data security, separation of duties, security controls, managing customer-managed encryption keys with Cloud KMS, and designing for compliance with legislation, commercial requirements, industry certifications, and audits.",
        "Section 4": "Analyzing and optimizing technology and business processes includes analyzing and defining technical processes like SDLC, CI/CD, troubleshooting, testing and validation of software and infrastructure, service catalogue and provisioning, business continuity, and disaster recovery, and analyzing and defining business processes including stakeholder management, change management, team assessment, decision-making process, customer success management, cost/resource optimization.",
        "Section 5": "Managing implementation entails advising development/operation teams for successful deployment, application development, API best practices, testing frameworks, data and system migration tooling, interacting with Google Cloud programmatically using Google Cloud Shell, Google Cloud SDK, and Cloud Emulators.",
        "Section 6": "Ensuring solution and operations reliability covers monitoring/logging/profiling/alerting solution, deployment and release management, and assisting with the support of solutions in operation."
        },
        "Professional Cloud Developer": {
        "Section 1": "Designing highly scalable, available, and reliable cloud-native applications. Covering microservices architectures, the use of Google recommended practices and patterns for application development.",
        "Section 2": "Building and testing applications. Understanding of best practices for building secure applications, using Google Cloud managed services for application storage, and deploying applications in containerized environments.",
        "Section 3": "Deploying applications. Skills in using Google Cloud services for application deployment, monitoring, management, and scaling. Understanding of continuous integration and continuous delivery (CI/CD) pipelines.",
        "Section 4": "Integrating Google Cloud services. Ability to integrate Google Cloud services with applications in ways that optimize performance and cost and create seamless user experiences.",
        "Section 5": "Managing application performance monitoring. Use of Google Cloud tools and technologies to monitor, troubleshoot, and optimize application performance."
        },
        "Professional Cloud Network Engineer": {
        "Section 1": "Designing, planning, and prototyping a Google Cloud network. Including considerations for high availability, failover, disaster recovery, DNS strategy, security, data exfiltration requirements, load balancing, quotas, hybrid connectivity, container networking, IAM roles, SaaS/PaaS/IaaS services, and microsegmentation.",
        "Section 2": "Implementing a Virtual Private Cloud (VPC). Covering IP address management, standalone vs. shared VPC, single vs. multi VPC, regional vs. multi-regional considerations, VPC Network Peering, firewall configurations, custom routes, managed services integration, and third-party device insertion.",
        "Section 3": "Configuring network services. Focusing on load balancing configurations, Google Cloud Armor policies, Cloud CDN settings, and Cloud DNS management.",
        "Section 4": "Implementing hybrid Interconnectivity. Discussing configurations for Cloud Interconnect, site-to-site IPsec VPNs, and Cloud Router setup.",
        "Section 5": "Managing, monitoring, and optimizing network operations. Including logging and monitoring with Google Cloud’s operations suite, managing security, troubleshooting connectivity issues, and monitoring for latency and traffic flow."
        },
        "Professional Cloud Security Engineer": {
        "Section 1": "Configuring Access Within a Cloud Solution Environment: Understanding how to manage access to cloud resources effectively.",
        "Section 2": "Configuring Network Security: Knowledge of securing network architectures, including the use of firewalls, VPCs, and private access.",
        "Section 3": "Ensuring Data Protection: Implementing mechanisms to protect data at rest and in transit, including encryption and data lifecycle management.",
        "Section 4": "Managing Operations Within a Cloud Solution Environment: Overseeing the operational aspects of cloud solutions to ensure security and compliance.",
        "Section 5": "Ensuring Compliance: Ensuring cloud solutions adhere to legal, regulatory, and compliance requirements."
        }
    }
}

# Temporary storage for selected exam details
selected_exam_details = {}

@app.route('/', methods=['GET'])
def home_screen():
    return "Welcome to Certibot!"

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

    if certifier in exam_outlines and exam_name in exam_outlines[certifier]:
        exam_scope = exam_outlines[certifier][exam_name]
        # Assuming you want to return the sections and their content
        if exam_outline.lower() == 'sections':
            exam_scope = json.dumps(exam_scope).replace("/n","")
            return exam_scope
        elif exam_outline.lower() == 'topics':
            question_generator = ExamQuestionGenerator(exam_outline=exam_outlines[certifier][exam_name])
            # Retrieve key topics
            key_topics = question_generator.retrieve_keytopics()
            # Return the key topics as a JSON response
            key_topics = key_topics.split(",")
            return jsonify({"key_topics": key_topics})
        else:
            return jsonify({"error": "Selection Unknown"}), 404
    else:
        return jsonify({"error": "Exam outline not found"}), 404

@app.route('/generate_questions_for_sections', methods=['POST'])
def generate_questions_for_sections():
    selected_sections = request.get_json()

    certifier = selected_exam_details.get('certifier')
    exam_name = selected_exam_details.get('exam_name')

    # Navigate the nested structure to get the specific exam's outline
    if certifier in exam_outlines and exam_name in exam_outlines[certifier]:
        exam_outline = exam_outlines[certifier][exam_name]
    else:
        return jsonify({"error": "Exam outline not found"}), 404

    question_generator = ExamQuestionGenerator(exam_outline=exam_outline)

    # Structure to hold the questions for each section
    section_questions = {}

    for section_key in selected_sections.values():
        # Ensure the section exists in the exam outline
        if section_key in exam_outline:
            try:
                # Generate questions for the selected section
                generated_questions = question_generator.based_on_outline(section_key, f"{certifier} {exam_name}")
                # Assuming generated_questions returns clean JSON or a dictionary
                clean_text = generated_questions.replace("```json\n", "").replace("\n```", "").strip()
                clean_text.replace("\\n", "")
                section_questions[section_key] = json.loads(clean_text)
            except ValueError as e:
                # Handle the error appropriately, maybe log it or return an error message
                section_questions[section_key] = "Error generating questions for this section"
        else:
            section_questions[section_key] = "Section not found in the exam outline"

    # Return the structured response as JSON
    return jsonify(section_questions)

@app.route('/generate_questions_for_topics', methods=['POST'])
def generate_questions_for_topics():
    data = request.get_json()
    topics = data.get('topics', [])
    
    exam_name = selected_exam_details.get('exam_name')
    certifier = selected_exam_details.get('certifier')

    question_generator = ExamQuestionGenerator(exam_outline=exam_outlines[certifier][exam_name])
    
    topics_questions = {}

    for topic in topics:
        try:
            # Generate questions for each topic
            generated_questions_str = question_generator.based_on_topics([topic], f"{certifier} {exam_name}")
            generated_questions_json = json.loads(generated_questions_str)
            # Add the generated questions to the topics_questions dict
            topics_questions[topic] = generated_questions_json
        except json.JSONDecodeError as e:
            # Log the error or handle it as needed
            topics_questions[topic] = {"error": f"{e}"}

    # Return the compiled topics and their questions as JSON
    return jsonify(topics_questions)

if __name__ == '__main__':
    app.run(debug=True)
