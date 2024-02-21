import React, { useState, useEffect } from "react";
import { Modal, Button, Divider, Radio, Progress } from "antd";
import { quizData } from "./quizData";
import classnames from "classnames";

export function Results({ questions, userAnswers, quiz_topic_section, is_topic }) {
  return (
    <div>
         <p style={{color:'whitesmoke'}}>
            {is_topic ? 'Topic' : 'Section'} : {quiz_topic_section}
          </p>
      {questions.map((moduleQuestions, index) => {
        console.log("MODD: ", moduleQuestions['solution'])
        return (
          <>
            <ModuleQuestion
              question={moduleQuestions["question"]}
              options={moduleQuestions["options"]}
              index={index}
              key={index}
              answer={moduleQuestions["solution"].correct}
              selectedOption={userAnswers[index]}
              isResult={true}
            />
            <p style={{color:'blue', margin:'4px'}}>
                Explanation:
                {moduleQuestions["solution"].explanation}
            </p>
          </>
        );
      })}
    </div>
  );
}

export function Control({ updateQuestion, lastQuestion, disableBack, disableNext }) {
  return (
    <div
      style={{
        marginTop: "0.5rem",
        display: "flex",
        justifyContent: "space-between",
        color:'white'
      }}
    >
      <div />
      <div>
        <Button
          onClick={() => updateQuestion("dec")}
          style={{ marginRight: "0.25rem" , color:'white'}}
          disabled={disableBack}
        >
          Back
        </Button>
        <Button
          onClick={() => updateQuestion("inc")}
          type="primary"
          disabled={disableNext}
          style={{ color:'white'}}
        >
          {lastQuestion ? "Submit" : "Next"}
        </Button>
      </div>
    </div>
  );
}

export function ProgressBar({ percent }) {
  return <Progress percent={percent} showInfo={false} strokeLinecap="square" />;
}

export function ModuleQuestion({
  question,
  options,
  index,
  currentQuestion,
  updateSelection = () => {},
  selectedOption,
  answer,
  visible = true,
  isResult = false
}) {
  const onChange = (e) => {
    updateSelection(currentQuestion, e.target.value);
  };

  if (!visible) {
    return null;
  }

  const radioStyle = {
    display: "block",
    height: "45px",
    lineHeight: "30px",
    width: "100%",
    
  };

  return (
    <div>
      <div className="quiz-question" style={{color:'whitesmoke'}}>{`${index + 1}. ${question}`}</div>
      <div>
        <Radio.Group
          onChange={onChange}
          value={selectedOption}
          style={{ width: "100%" , color:'white'}}
        >
          {Object.keys(options).map((key) => {

            console.log("REsult : ", isResult)
            console.log("Key: ", key)
            console.log("answwer: ", answer)

            const quizClasses = classnames({
              "quiz-option": true,
              correct: isResult && key === answer,
              wrong:
                isResult && selectedOption === key && selectedOption !== answer
            });
            return (
          
              <Radio.Button
               


                checked={key === selectedOption}
                value={key}

                style= {{
                    color: (isResult && key === answer) ? 'green' :  (isResult && selectedOption === key && selectedOption !== answer) ? 'red' :  (key === selectedOption) ? 'blue': 'whitesmoke',
                    border:`2px solid`,
                    borderColor: (isResult && key === answer) ? 'green' :  (isResult && selectedOption === key && selectedOption !== answer) ? 'red' :  (key === selectedOption) ? 'blue' : 'whitesmoke',
                    borderRadius:'10px',
                    width: '100%',
                    display: 'block',
                    padding: '0.5rem',
                    marginBottom: '1rem',
                    cursor: 'pointer',
                    background:'none',
                    height:'fit-content ',
                    
                }}
              >
                
                {options[key]}
                
               
              </Radio.Button>
            
            );
          })}
        </Radio.Group>
      </div>
      {isResult && <Divider />}
    </div>
  );
}

function Quiz() {
  const [title, setTitle] = useState("Quiz Demo");
  const [quizModalVisible, setQuizModalVisible] = useState(false);
  const [selectedModule, setSelectedModule] = useState(1);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [userAnswers, setUserAnswers] = useState([]);
  const [showResults, setShowResults] = useState(false);
  const [answered, setAnswered] = useState(false);

  const showModal = () => {
    setQuizModalVisible(true);
  };

  const handleOk = (e) => {
    setQuizModalVisible(false);
  };

  const handleCancel = (e) => {
    setQuizModalVisible(false);
  };

  const updateQuestion = (type) => {
    const value = type === "dec" ? -1 : 1;
    const len = quizData["module1"].length;
    const newQuestionNumber = currentQuestion + value;
    if (newQuestionNumber >= len) {
      let count = 0;

      for (let i = 0; i < quizData["module1"].length; i++) {
        if (quizData["module1"][i]["answer"] === userAnswers[i]) {
          count++;
        }
      }
      setShowResults(true);

      setTitle(`Result - You got ${count}/${len} correct answers`);
      updateSelection(false);
    } else {
      setCurrentQuestion(newQuestionNumber);
      updateSelection(false);
    }
  };

  const updateSelection = (questionNumber, answer) => {
    const answers = [...userAnswers];
    answers[questionNumber] = answer;
    setUserAnswers(answers);
  };

  return (
    <div>
      <Button type="primary" onClick={showModal}>
        Start Quiz
      </Button>
      <Modal
        maskClosable={false}
        title={title}
        visible={quizModalVisible}
        onOk={handleOk}
        onCancel={handleCancel}
        footer={[]}
        closable={false}
      >
        {showResults && (
          <>
            <Results
              questions={quizData["module1"]}
              userAnswers={userAnswers}
            />
            <div
              style={{
                marginTop: "0.5rem",
                display: "flex",
                justifyContent: "space-between"
              }}
            >
              <div />
              <div>
                <Button
                  onClick={() => setQuizModalVisible(false)}
                  type="primary"
                >
                  Close
                </Button>
              </div>
            </div>
          </>
        )}
        {!showResults && (
          <>
            {quizData["module1"].map((moduleQuestions, index) => {
              return (
                <>
                  <ModuleQuestion
                    selectedOption={userAnswers[currentQuestion]}
                    question={moduleQuestions["question"]}
                    options={moduleQuestions["options"]}
                    key={index}
                    index={index}
                    currentQuestion={currentQuestion}
                    visible={index === currentQuestion}
                    updateSelection={updateSelection}
                  />
                </>
              );
            })}
            <ProgressBar
              percent={(currentQuestion / quizData["module1"].length) * 100}
            />
            <Control
              disableBack={currentQuestion === 0}
              disableNext={userAnswers.length < currentQuestion + 1}
              updateQuestion={updateQuestion}
              lastQuestion={currentQuestion === quizData["module1"].length - 1}
            />
          </>
        )}
      </Modal>
    </div>
  );
}

export default Quiz;
