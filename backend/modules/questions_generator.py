import openai

class ExamQuestionGenerator:
    def __init__(self, model='gpt-4-1106-preview', exam_outline=''):
        self.model = model
        # will have to scrape this
        self.exam_outline = exam_outline

    def retrieve_keytopics(self):
        """
        Generate a list of keywords for the exam.
        """      
        return self._call_openai_api(f'Return only a list of 5, comma separated, of the top core products or topics that will be tested based on this exam outline {self.exam_outline}')

    def based_on_outline(self, section, exam_name):
        """
        Generate questions for a specific section of the exam.
        """

        section = self.exam_outline[section]
        return self._call_openai_api(
                    f'Generate five scenario-based multiple-choice questions on "{section}" for the "{exam_name}" exam. '
                    'Each question should include four options (A-D) and a solution with a detailed explanation as to why it is correct and why the other options are not a good fit. '
                    'Format the response as JSON, with each question as an object in an array. '
                    'Include a "question" text, "options" as a dictionary, and a "solution" object with the correct option and an explanation. '
                    'Example structure: '
                    '"Section 1": {"questions": ['
                    '{"question": "Example question text for Section 1?", "options": {"A": "Option A", "B": "Option B", "C": "Option C", "D": "Option D"}, '
                    '"solution": {"correct": "A", "explanation": "Explanation why A is correct for Section 1."}}, ...'
                    ']}, '
                    '"Section 2": {"questions": ['
                    '{"question": "Example question text for Section 2?", "options": {"A": "Option A", "B": "Option B", "C": "Option C", "D": "Option D"}, '
                    '"solution": {"correct": "B", "explanation": "Explanation why B is correct for Section 2."}}, ...'
                    ']}, ...'
                    '}')    
    
    def based_on_topics(self, keywords, exam_name):
        """
        Generate questions based on a list of keywords for the exam.
        """
        return self._call_openai_api(
                   f'Generate 5 complex, scenario-based multiple-choice questions for each of these topics {keywords} for the {exam_name} Exam. Include answers and explanations for each question in JSON format. Return only a json object as response. Structure the JSON object with topic, question, options, and solution keys. Remove any markdown or contextual characters.')    


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
    
