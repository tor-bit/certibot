import Head from "next/head";
import Hero from "../components/hero";
import Navbar from "../components/navbar";
import SectionTitle from "../components/sectionTitle";

import { benefitOne, benefitTwo } from "../components/data";
import Video from "../components/video";
import Benefits from "../components/benefits";
import Footer from "../components/footer";
import Testimonials from "../components/testimonials";
import Cta from "../components/cta";
import Faq from "../components/faq";
import PopupWidget from "../components/popupWidget";

const Home = () => {
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

      <Navbar />
      <Hero />
      <SectionTitle
        title="Welcome">
        Many learners preparing for certification exams struggle to find personalized, effective study materials
        that adapt to their unique learning styles and the dynamic nature of exam content. 
      </SectionTitle>
      
      <SectionTitle
        pretitle="Certibot"
        title={`" Thou Shall Pass "`}>
        This leads to inadequate preparation, increased anxiety, and lower success rates in certification exams,
        which are crucial for professional advancement.
      </SectionTitle>

      <SectionTitle
        pretitle=""
        title="Preparation Selection Page">
        <div className="flex flex-col items-start space-y-3 sm:space-x-4 sm:space-y-0 sm:items-center sm:flex-row">
          <a
            href="https://web3templates.com/templates/nextly-landing-page-template-for-startups"
            target="_blank"
            rel="noopener"
            className="px-8 py-4 text-lg font-medium text-center text-white bg-indigo-600 rounded-md ">
            Try it Now
          </a>
        </div>
      </SectionTitle>

      <Footer />
    </>
  );
}

export default Home;