from flask import Flask, request, jsonify
from flask_cors import CORS 
from modules.questions_generator import ExamQuestionGenerator

app = Flask('Certibot')
CORS(app)

exams_by_company = {
    'Google': ["Associate Cloud Engineer", 
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
    'Professional Data Engineer' : 45
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
    exam_name = selected_exam_details.get('exam_name')

    # Check if the selected exam is in the outlines
    if exam_name in exam_outlines:
        question_generator = ExamQuestionGenerator(exam_outline=exam_outlines[exam_name])
    else:
        return jsonify({"error": "Exam outline not found"}), 404

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

@app.route('/exam_outline_key_topics', methods=['GET'])
def exam_outline_key_topics():
    global selected_exam_details
    exam_name = selected_exam_details.get('exam_name')

    # Check if the exam name is set and valid
    if exam_name in exam_outlines:
        # Initialize the question generator with the exam outline
        question_generator = ExamQuestionGenerator(exam_outline=exam_outlines[exam_name])

        # Retrieve key topics
        key_topics = question_generator.retrieve_keywords()

        # Return the key topics as a JSON response
        key_topics = key_topics.split(",")
        return jsonify({"key_topics": key_topics})
    else:
        # Return an error if the exam name is not set or invalid
        return jsonify({"error": "Invalid or unspecified exam name"}), 400


@app.route('/generate_questions_for_topics', methods=['POST'])
def generate_questions_for_topics():
    data = request.get_json()
    custom_topics = data.get('custom', [])
    chosen_topics = data.get('chosen', [])
    global selected_exam_details
    exam_name = selected_exam_details.get('exam_name')

    # Initialize your question generator
    question_generator = ExamQuestionGenerator(exam_outline=exam_outlines[exam_name])

    # Structure to hold the questions for each topic
    topics_questions = {}

    # Generate questions for custom topics
    for topic in custom_topics:
        try:
            generated_questions = question_generator.based_on_keywords(chosen_topics)
        except ValueError as e:
            print(e)

    # Return the structured response as JSON
    return jsonify(generated_questions)


if __name__ == '__main__':
    app.run(debug=True)
