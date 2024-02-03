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
        return self._call_openai_api(f'Return only a list of 5, comma separated, of the top core topics based on this exam outline {self.exam_outline}')

    def based_on_outline(self, section, exam_name):
        """
        Generate questions for a specific section of the exam.
        """

        section = self.exam_outline[section]
        return self._call_openai_api(f'Generate 5 complex, scenario-based multiple-choice questions about {section} for the {exam_name} Exam. Include answers and explanations for each question in JSON format. Return the response as a json object. Structure the JSON object with question, options, and solution keys. Remove any markdown or contextual characters.')
    
    def based_on_topics(self, keywords, exam_name):
        """
        Generate questions based on a list of keywords for the exam.
        """
        prompt = f'Generate 5 complex, scenario-based multiple-choice questions for each of these topics {keywords} for the {exam_name} Exam. Include answers and explanations for each question in JSON format. Return only a json object as response. Structure the JSON object with topic, question, options, and solution keys. Remove any markdown or contextual characters.'
        response = self._call_openai_api(prompt)
        
        # Assume the response is structured with one block per topic
        # This parsing will depend on how you format the prompt and the expected response structure
        return response


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
    
