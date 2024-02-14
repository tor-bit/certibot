import Head from "next/head";
import Hero from "../components/hero";
import Navbar from "../components/navbar";
import SectionTitle from "../components/sectionTitle";
import Footer from "../components/footer";
import React, {useState} from 'react'
import Sparkles from 'react-sparkle'
import Container from "../components/container";
import { NormalSelect } from "../components/dataEntry";
import Link from "next/link";




const Quiz = () => {


  
  const [exam_outline, setExamOutline] = useState('topics');


  const [exam_type, setExamType] = useState('google');

  const handleExamTypeChange = () => {
    console.log("Handle Exam Type change")
  }

  const handleExamOutlineChange = (value) => {
    console.log("E: ", value)
    setExamOutline(value)
  }
  

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
          Exam Selection
        </h2>

        <div className="text-md font-bold tracking-wider text-indigo-600 uppercase">
          Sections
        </div>

      </Container>
      <Footer />
    </>
  );
}

export default Quiz;