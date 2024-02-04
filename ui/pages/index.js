import Head from "next/head";
import Hero from "../components/hero";
import Navbar from "../components/navbar";
import SectionTitle from "../components/sectionTitle";
import Footer from "../components/footer";
import React from 'react'
import Sparkles from 'react-sparkle'
import { getHomeScreen } from "./api/api";


// home page
export default function Home () {


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
        count={30}
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
            href="/generate"
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


export async function getServerSideProps() {
  const photos = await getHomeScreen();
  console.log("PPP", photos)
  return {
    props: {
      photos
    },
  };
}