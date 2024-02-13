import Head from "next/head";
import Hero from "../components/hero";
import Navbar from "../components/navbar";
import SectionTitle from "../components/sectionTitle";
import Footer from "../components/footer";
import React, {useState, useEffect} from 'react'
import Sparkles from 'react-sparkle'
import Container from "../components/container";
import { NormalSelect } from "../components/dataEntry";
import Link from "next/link";
import { getCompanies, getExamsCompany, getExamSelection, getGenerateQuestionsForSections } from "./api/api";

const exam_types = [
  { value: 'GCP', label: 'Google Cloud Platform' },
  { value: 'AWS', label: 'Amazon Web Services' },
  { value: 'Microsoft', label: 'Microsoft' }
]


const GenerateQuestions = ({companies}) => {


  
  const [exam_outline, setExamOutline] = useState('topics');

  const [exams, setExams] = useState([{value:'', label:''}]);

  const [exam_type, setExamType] = useState('GCP');

  const [exam_specific, setExamSpecfic] = useState({});

  const [sections, setSections] = useState({});

  const [topics, setTopics] = useState({});



  const handleGenerateQuestionsForSections = async (val) => {
    let res = await getGenerateQuestionsForSections(val);
    console.log("Questions: ", res);
  }

  const handleGetExamsCompany = async (val) => {
    let res = await getExamsCompany(val);
    console.log("READ: ", res);
    let dict = [];
    for (var x = 0; x < res.length; x++) {
      let neww = {value:x, label:res[x]};
      dict.push(neww);
    }
    console.log("Dictionary is: ", dict)
    setExams(dict);
    setExamSpecfic(dict[0])
    return res;
}

  const handleExamTypeChange = (value) => {
    console.log("Handle Exam Type change")
    setExamType(value);
    let neww = handleGetExamsCompany(value);
    console.log("NNN: ", neww)
  }

  const handleExamOutlineChange = (value) => {
    console.log("E: ", value)
    setExamOutline(value)
  }

  const handleExamSpecificChange = (value) => {
    console.log("VAL: ", value)
    setExamSpecfic(value);
  }

  const handleExamSelection = async () => {
    let neww = getExamSelection(exam_type, exam_specific.label??'', exam_outline);
    console.log("NWWW: ", neww)
    // set the sections or exams from here
    // NEED TO CATER FOR 404. and when the sections and topics are not there

    
  }
  
  useEffect(() => {
    handleGetExamsCompany(exam_type);    
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
          Exam Selection
        </h2>

        <div className="text-md font-bold tracking-wider text-indigo-600 uppercase">
          Exam Type
        </div>
        <NormalSelect value={exam_type} defaultValue={exam_type} handleChange={handleExamTypeChange} options={exam_types}/>

        <div className="text-md font-bold tracking-wider text-indigo-600 uppercase">
          Exam Specification
        </div>
        <NormalSelect value={exam_specific} defaultValue={exam_specific} handleChange={handleExamSpecificChange} 
        options={exams} labelInValue={true}/>

        <div className="text-md font-bold tracking-wider text-indigo-600 uppercase">
          Exam Outline
        </div>
        <NormalSelect value={exam_outline} defaultValue={exam_outline} handleChange={handleExamOutlineChange} 
         options={[
          { value: 'topics', label: 'Topics' },
          { value: 'sections', label: 'Sections' },
        ]}/>

        <button href={exam_outline === 'topics' ? "/topics_outline":"/sections_outline"} 
        onClick={handleExamSelection}
        className="w-full px-6 py-2 mt-3 text-center text-white bg-blue-800 rounded-xl lg:ml-5">         
          Let's do it!
        </button>

        {exam_outline === 'topics' ?
          <>div</> 
          : 
          <>sigh</>
        }
      </Container>
      <Footer />
    </>
  );
}

export default GenerateQuestions;


export async function getServerSideProps() {
  const companies = await getCompanies();
  
  return {
    props: {
      companies
    },
  };
}