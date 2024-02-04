
export const getHomeScreen = async () => {
  const res = await fetch(
    `https://cert-bot-dev.ew.r.appspot.com/`
  );
  const responseJson = await res.json();
  console.log("REs ", responseJson)
  return responseJson;
}


export const getCompanies = async () => {
  const res = await fetch(
    `https://cert-bot-dev.ew.r.appspot.com/companies`
  );
  const responseJson = await res.json();
  return responseJson;
}


export const getExamsCompany = async (company) => {
  const res = await fetch(
    `https://cert-bot-dev.ew.r.appspot.com/exams/${company}`
  );
  const responseJson = await res.json();
  return responseJson;
}

export const getExamSelection = async (certifier, exam_name, exam_outline) => {
  const body_data = JSON.stringify({certifier, exam_name, exam_outline})
  const res = await fetch(
    `https://cert-bot-dev.ew.r.appspot.com/exam_selection`,
    {
      headers: {
        "Content-Type": "application/json",
      },
      method: "POST", 
      body: body_data
    }
  );
  const responseJson = await res.json();
  return responseJson;
}