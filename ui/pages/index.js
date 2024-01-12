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
import React from 'react'
import Sparkles from 'react-sparkle'


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
      <Sparkles flicker={false}
        count={20}
        minSize={7}
        maxSize={12}
        overflowPx={80}
        fadeOutSpeed={10}
      />
      <Navbar />
      <Hero />



    
      <SectionTitle
        title="Preparation Selection Page" noparagraph={true}>
        <div className="mt-6 flex flex-col items-start space-y-3 sm:space-x-4 sm:space-y-0 sm:items-center sm:flex-row">
          <a
            href="https://web3templates.com/templates/nextly-landing-page-template-for-startups"
            target="_blank"
            rel="noopener"
            className="px-8 py-4 text-lg font-medium text-center text-white bg-blue-800 rounded-xl ">
            Try it Now
          </a>
        </div>
      </SectionTitle>

      <Footer />
    </>
  );
}

export default Home;