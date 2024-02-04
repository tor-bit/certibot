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

const exam_types = [
  { value: 'google', label: 'Google' },
  { value: 'aws', label: 'AWS' },
  { value: 'microsoft', label: 'Microsoft' }
]


const GenerateQuestions = () => {


  
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
          Exam Type
        </div>
        <NormalSelect value={exam_type} defaultValue={exam_type} handleChange={handleExamTypeChange} options={exam_types}/>

        <div className="text-md font-bold tracking-wider text-indigo-600 uppercase">
          Exam Specification
        </div>
        <NormalSelect value={exam_type} defaultValue={exam_type} handleChange={handleExamTypeChange} options={exam_types}/>

        <div className="text-md font-bold tracking-wider text-indigo-600 uppercase">
          Exam Outline
        </div>
        <NormalSelect value={exam_outline} defaultValue={exam_outline} handleChange={handleExamOutlineChange}
         options={[
          { value: 'topics', label: 'Topics' },
          { value: 'sections', label: 'Sections' },
        ]}/>

        <Link href={exam_outline === 'topics' ? "/topics_outline":"/sections_outline"} className="w-full px-6 py-2 mt-3 text-center text-white bg-blue-800 rounded-xl lg:ml-5">         
          Let's do it!
        </Link>
      </Container>
      <Footer />
    </>
  );
}

export default GenerateQuestions;