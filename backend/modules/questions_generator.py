import openai

class ExamQuestionGenerator:
    def __init__(self, model='gpt-4-1106-preview', exam_outline=''):
        self.model = model
        # will have to scrape this
        self.exam_outline = exam_outline

    def retrieve_keywords(self):
        """
        Generate a list of keywords for the exam.
        """      
        return self._call_openai_api(f'Return only a list, comma separated, of important keywords from this exam outline {self.exam_outline}')

    def based_on_outline(self, section):
        """
        Generate questions for a specific section of the exam.
        """
        # if section not in self.exam_outline:
        #     raise ValueError(f"Invalid section: {section}")

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
