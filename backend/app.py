from questions_generator import generator
from flask import Flask
from flask_cors import CORS

app = Flask('Certibot')
CORS(app)

#cloud tasks
@app.route('/') 
def get_hello():
    return "hello, world. it's me certibot! yeehaw!"    

@app.route('/api/sectionquestions')   
def get_data():
    questions = generator.based_on_outline()
    return questions             

if __name__ == '__main__':
    app.run(debug=True)