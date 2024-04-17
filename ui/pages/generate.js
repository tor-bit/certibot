import Head from "next/head";
import { Spin } from "antd";
import Footer from "../components/footer";
import React, {useState, useEffect} from 'react'
import Sparkles from 'react-sparkle'
import Container from "../components/container";
import { MultipleSelect, NormalSelect } from "../components/dataEntry";
import { useContext } from "react";
import { AppContext } from "./_app";
import Navbar from "../components/navbar";
import { useRouter } from 'next/navigation';
import { getCompanies, getExamsCompany, getExamSelection, getGenerateQuestionsForSections } from "./api/api";

const exam_types = [
  { value: 'GCP', label: 'Google Cloud Platform' },
  { value: 'AWS', label: 'Amazon Web Services' },
  { value: 'Microsoft', label: 'Microsoft' }
]


const GenerateQuestions = ({companies}) => {


  const {setQuizDetails} = useContext(AppContext);
  
  const [exam_outline, setExamOutline] = useState('topics');

  const [exams, setExams] = useState([{value:'', label:''}]);

  const [exam_type, setExamType] = useState('GCP');

  const [exam_specific, setExamSpecfic] = useState({});

  const [sections, setSections] = useState({});

  const [topics, setTopics] = useState({});

  const [selected_topics, setSelectedTopic] = useState([]);

  const [selected_sections, setSelectedSection] = useState([]);

  const router = useRouter();

 
  const handleGenerateQuestions = () => {
    if (exam_outline === 'topics') {
      setQuizDetails({exam_outline, selected_outlines: selected_topics});
    } else {
      setQuizDetails({exam_outline, selected_outlines: selected_sections});
    }
    router.push('/quiz');
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

  const handleSelectTopics = (value) => {
    console.log("Current selected topics: ", value)
    setSelectedTopic(value);
  }

  const handleSelectSections = (value) => {
    console.log("Current selected sections: ", value)
    setSelectedSection(value);
  }

  const [loading, setLoading] = useState(true);
  
  const [showSelection, setShowSelection] = useState(false);

  const handleExamSelection = async () => {
    let neww = await getExamSelection(exam_type, exam_specific.label??'', exam_outline);
    console.log("NWWW: ", neww)
    // set the sections or exams from here
    // NEED TO CATER FOR 404. and when the sections and topics are not there
    console.log("READ: ", neww);
    setShowSelection(true);
    setLoading(true);
   


    let received_topics_sections = exam_outline === 'topics' ? neww['key_topics'] : neww;
    console.log('Recevied topics: .', received_topics_sections)

    if (exam_outline === 'topics') {
      let dict = [];
      for (var x = 0; x < received_topics_sections.length; x++) {
        let neww = {value:x, label:received_topics_sections[x]};
        dict.push(neww);
      }
      console.log("Dictionary is: ", dict)
      setTopics(dict);
    } else {

      let dict = [];
      for (const [key, value] of Object.entries(received_topics_sections)) {
        let neww = {value:key, label:value};
        dict.push(neww);
      }
      console.log("Dictionary is: ", dict)

      setSections(dict);
    }

    setLoading(false);

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
      <Navbar />
      <Container className={`flex w-full flex-col mt-4 items-center justify-center text-center`}>
        <h2 className="max-w-2xl mt-3 text-3xl font-bold leading-snug tracking-tight text-blue-200 lg:leading-tight lg:text-4xl dark:text-white">
          Exam Selection
        </h2>

        <div className="text-md mt-4 font-bold tracking-wider text-cyan-500 uppercase">
          Exam Type
        </div>
        <NormalSelect value={exam_type} defaultValue={exam_type} handleChange={handleExamTypeChange} options={exam_types}/>

        <div className="text-md mt-4 font-bold tracking-wider text-cyan-500 uppercase">
          Exam Specification
        </div>
        <NormalSelect value={exam_specific} defaultValue={exam_specific} handleChange={handleExamSpecificChange} 
        options={exams} labelInValue={true}/>

        <div className="text-md mt-4 font-bold tracking-wider text-cyan-500 uppercase">
          Exam Outline
        </div>
        <NormalSelect value={exam_outline} defaultValue={exam_outline} handleChange={handleExamOutlineChange} 
         options={[
          { value: 'topics', label: 'Topics' },
          { value: 'sections', label: 'Sections' },
        ]}/>

        <button 
        onClick={handleExamSelection}
        className="w-full px-6 py-2 mt-4 text-center text-white bg-cyan-700 rounded-xl lg:ml-5">         
          Let's do it!
        </button>

        {!showSelection ? <></>
        :
        loading ?



<Spin spinning={loading}/>
:

exam_outline === 'topics' ?
<>

<div className="text-md  mt-4 font-bold tracking-wider text-cyan-500 uppercase">
  Select Topics
</div>
<MultipleSelect value={selected_topics} options={topics} 
handleChange={handleSelectTopics} labelInValue={true} />
</> 
: 
<>

<div className="text-md mt-4 font-bold tracking-wider text-cyan-500 uppercase">
  Select Sections
</div>
<MultipleSelect value={selected_sections} options={sections}
 handleChange={handleSelectSections} labelInValue={true} />
</>


        }

        {showSelection ? 
        
        <button 
        onClick={handleGenerateQuestions}
        className="w-full px-6 py-2 mt-4 text-center text-white bg-cyan-700 rounded-xl lg:ml-5">         
          Generate Questions
        </button>
      
        :
<></>
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