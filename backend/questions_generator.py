import openai

class GCPExamQuestionGenerator:
    def __init__(self, model='gpt-4-1106-preview'):
        self.model = model
        # will have to scrape this
        self.exam_outline = {
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

    def retrieve_keywords(self):
        """
        Generate a list of keywords for the exam.
        """      
        return self._call_openai_api(f'Return only a list, comma separated, of important keywords from this exam outline {self.exam_outline}')

    def based_on_outline(self, section):
        """
        Generate questions for a specific section of the exam.
        """
        if section not in self.exam_outline:
            raise ValueError(f"Invalid section: {section}")

        section = self.exam_outline[section]
        return self._call_openai_api(f'Generate 5 complex, scenario-based multiple-choice questions about {section} for the GCP Professional Data Engineer Exam. Include answers and explanations for each question. Return the response as a json object. Structure your JSON object as follows: include a "question" key for the exam question, an "options" key with choices labeled "A" to "D," and a "solution" key containing the "answer" (correct option) and an "explanation" for why it\'s correct.')
    
    def based_on_keywords(self, keywords):
        """
        Generate questions based on keywords for the exam.
        """
        return self._call_openai_api(f'Generate 5 complex, scenario-based multiple-choice questions based on these {keywords} for the GCP Professional Data Engineer Exam. Include answers and explanations for each question. Return the response as a json object. Structure your JSON object as follows: include a "keyword" key for the keyword, "question" key for the exam question, an "options" key with choices labeled "A" to "D," and a "solution" key containing the "answer" (correct option) and an "explanation" for why it\'s correct.')


    def _call_openai_api(self, content):
            """
            Call the OpenAI API to generate questions based on the provided content.
            """
            openai.api_key = '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' # will need to be hidden
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {
                        'role': 'user',
                        'content': f'{content}'
                    }
                ]
            )
            return response.choices[0].message.content    

# Example usage
generator = GCPExamQuestionGenerator()
try:
    #questions = generator.based_on_outline('Section 1')
    #print(questions)
    questions = generator.retrieve_keywords()
    print(questions)     
except ValueError as e:
    print(e)