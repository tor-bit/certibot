import Head from "next/head";
import Footer from "../components/footer";
import React, {useEffect, useState} from 'react';
import Sparkles from 'react-sparkle'
import Container from "../components/container";
import { useContext } from "react";
import { AppContext } from "./_app";
import { getGenerateQuestionsForSections, getGenerateQuestionsForTopics } from "./api/api";
import { ModuleQuestion, ProgressBar, Control, Results } from "../components/quizComponents";
import { quizData } from "../components/quizData";
import { topics_questions } from "../components/check";
import { Button } from "antd";

const Quiz = () => {

  const {quiz_details} = useContext(AppContext);

  console.log("QUIZ DETAILS: ", quiz_details);

  const handleGenerateQuestions = async () => {

    if (quiz_details['exam_outline'] === 'topics') {
      let topicss = quiz_details['selected_outlines'].map((x) => {
        return x.label
      })
      console.log("Topics are: ", topicss)
      let res = await getGenerateQuestionsForTopics({topics:topicss});
      console.log("RESPONSE IS tOPICS : ", res)
      return res;
    } else {
      console.log("We reach here?")
      let sections = {}

      const iterator =  quiz_details['selected_outlines'].keys();

          for (const key of iterator) {
            console.log(key);
            sections = {...sections,
               [key]:quiz_details['selected_outlines'][key].label};
          }



      console.log("Sections are: ", sections)
      let res = await getGenerateQuestionsForSections(sections);
      console.log("RESPONSE IS sections : ", res)
      
      return res;
    }
  }

  useEffect(() => {
    handleGenerateQuestions();    
  }, []);


  const [title, setTitle] = useState("Quiz Demo");
  const [quizModalVisible, setQuizModalVisible] = useState(false);
  const [selectedModule, setSelectedModule] = useState(1);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [userAnswers, setUserAnswers] = useState([]);
  const [showResults, setShowResults] = useState(false);
  const [answered, setAnswered] = useState(false);


  const updateQuestion = (type) => {
    const value = type === "dec" ? -1 : 1;
    const len = topics_questions["BigQuery"].questions.length;
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

  console.log("TOPICS: ", topics_questions);


  return (
    <>
      <Head>
        <title>Certibot</title>
        <meta
          name="description"
          content="Certibot is an AI driven application created to give you a personalized study experience."
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Sparkles flicker={false}
        count={10}
        minSize={2}
        maxSize={4}
        overflowPx={80}
        fadeOutSpeed={1}
      />
      <Container className={`flex w-full flex-col mt-4 items-center justify-center text-center`}>
        <h2 className="max-w-2xl mt-3 text-3xl font-bold leading-snug tracking-tight text-blue-200 lg:leading-tight lg:text-4xl dark:text-white">
          Quiz
        </h2>

        {!showResults && (
          <>
          <p style={{color:'whitesmoke'}}>
            Topic: Big Query
          </p>
          {topics_questions["BigQuery"].questions.map((moduleQuestions, index) => {
console.log("here : ", moduleQuestions)
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
              percent={(currentQuestion / topics_questions["BigQuery"].questions.length) * 100}
            />
            <Control
              disableBack={currentQuestion === 0}
              disableNext={userAnswers.length < currentQuestion + 1}
              updateQuestion={updateQuestion}
              lastQuestion={currentQuestion === topics_questions["BigQuery"].questions.length - 1}
            />


          </>
        )}




{showResults && (
          <>
            <Results
              questions={topics_questions["BigQuery"].questions}
              userAnswers={userAnswers}
              quiz_topic_section={'Big Query'}
              is_topic={true}
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

      </Container>
      <Footer />
    </>
  );
}

export default Quiz;