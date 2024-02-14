import Head from "next/head";
import Footer from "../components/footer";
import React, {useEffect} from 'react';
import Sparkles from 'react-sparkle'
import Container from "../components/container";
import { useContext } from "react";
import { AppContext } from "./_app";
import { getGenerateQuestionsForSections, getGenerateQuestionsForTopics } from "./api/api";


const Quiz = () => {

  const {quiz_details} = useContext(AppContext);

  console.log("QUIZ DETAILS: ", quiz_details);

  const handleGenerateQuestions = async () => {

    if (quiz_details['exam_outline'] === 'topics') {
      let res = await getGenerateQuestionsForSections();
    } else {
      let res = await getGenerateQuestionsForTopics();
    }


    let dict = [];
    for (var x = 0; x < res.length; x++) {
      let neww = {value:x, label:res[x]};
      dict.push(neww);
    }
    

 
    return res;
  }

  useEffect(() => {
    handleGenerateQuestions();    
  }, []);

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


      </Container>
      <Footer />
    </>
  );
}

export default Quiz;