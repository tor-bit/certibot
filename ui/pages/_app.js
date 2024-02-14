import { ThemeProvider } from "next-themes";
import "../css/tailwind.css";
import { createContext,  useState } from "react";

export const AppContext = createContext(null);

function MyApp({ Component, pageProps }) {
  const [quiz_details, setQuizDetails] = useState({exam_outline:'', selected_outlines:[]});
  return (
    <AppContext.Provider value={{quiz_details, setQuizDetails}}>
      <ThemeProvider attribute="class">
        <Component {...pageProps} />
      </ThemeProvider>
    </AppContext.Provider>
  );
}

export default MyApp;
