import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase Admin SDK with service account credentials and project ID
cred = credentials.Certificate("path/to/serviceAccountKey.json")  # Provide the path to your service account key JSON file
firebase_admin.initialize_app(cred, {
    'projectId': 'your-project-id'
})

# Initialize Firestore client
db = firestore.client()

# JSON object to be saved into Firestore
data = {
    "GCP": [
        {"exam_code": "ACE", "exam_name": "Associate Cloud Engineer"},
        {"exam_code": "PCA", "exam_name": "Professional Cloud Architect"},
        # Include other GCP exams here...
    ],
    "AWS": [
        {"exam_code": "AWS CCP", "exam_name": "AWS Certified Cloud Practitioner"},
        {"exam_code": "AWS SAA", "exam_name": "AWS Certified Solutions Architect – Associate"},
        # Include other AWS exams here...
    ],
    "Microsoft": [
        {"exam_code": "AZ-900", "exam_name": "Microsoft Certified: Azure Fundamentals"},
        {"exam_code": "DP-900", "exam_name": "Microsoft Certified: Azure Data Fundamentals"},
        # Include other Microsoft exams here...
    ]
}

# Save JSON object into Firestore
def save_json_to_firestore(data):
    for category, exams in data.items():
        category_ref = db.collection("exams").document(category)
        for exam in exams:
            exam_ref = category_ref.collection("exams").document()
            exam_ref.set(exam)

# Call the function to save the JSON object into Firestore
save_json_to_firestore(data)
