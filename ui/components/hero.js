import Image from "next/image";
import Container from "./container";
import heroImg from "../public/img/try.png";

const Hero = () => {
  return (
    <>
      <Container className="flex flex-wrap ">
        <div className="flex items-center w-full lg:w-1/2">
          <div className="max-w-2xl mb-8">
            <h1 className="text-4xl font-bold leading-snug tracking-tight text-gray-100 lg:text-4xl lg:leading-tight xl:text-6xl xl:leading-tight dark:text-white">
              Welcome
            </h1>

            <h2 className="max-w-2xl mt-3 text-3xl font-bold leading-snug tracking-tight text-blue-200 lg:leading-tight lg:text-4xl dark:text-white">
              Many learners preparing for certification exams struggle to find personalized, effective study materials
              that adapt to their unique learning styles and the dynamic nature of exam content. 
            </h2>
          </div>
        </div>
        <div className="flex items-center justify-center w-full lg:w-1/2">
          <div className="bot-animate">
            <Image priority
              src={heroImg}
              width="616"
              height="617"
              className={"object-cover"}
              alt="Hero Illustration"
              loading="eager"
            />
          </div>
        </div>


        <div className=" flex w-full flex-col mt-4 items-center justify-center text-center">
          <p className="max-w-4xl mt-3 text-3xl font-bold leading-snug tracking-tight text-blue-200 lg:leading-tight lg:text-4xl dark:text-white">
          This leads to inadequate preparation, increased anxiety, and lower success rates in certification exams,
          which are crucial for professional advancement.
          </p>

          <div className="mt-8 text-sm font-bold tracking-wider text-cyan-500 uppercase">
            INTRODUCING
          </div>

          <h1 className="mt-4 font-bold leading-snug tracking-tight text-gray-100 lg:text-4xl lg:leading-tight xl:text-6xl xl:leading-tight dark:text-white" style={{fontSize:'130px'}}>
            Certibot
          </h1>

          <div className="text-3xl mt-3 font-bold tracking-wider text-cyan-500 uppercase">
            {`"THOU SHALL PASS"`}
          </div>
      </div>

      </Container>

    </>
  );
}


export default Hero;