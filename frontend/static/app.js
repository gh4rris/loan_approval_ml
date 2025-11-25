import { API_BASE_URL } from "./config.js";

main();

function main() {
  const form = document.getElementById("loan-form");
  const popupBtn = document.getElementById("popup-btn");
  const clear = document.getElementById("clear");
  const random = document.getElementById("random");
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData.entries());
    data.loan_percent_income =
      Math.round((data.loan_amnt / data.person_income) * 100) / 100;
    const prediction = await predict(data);
    displayResults(prediction);
  });
  popupBtn.addEventListener("click", () => {
    const loanForm = document.getElementById("loan-form");
    const popupBox = document.getElementById("popup");
    loanForm.style.pointerEvents = "all";
    loanForm.style.opacity = 1;
    popupBox.style.display = "none";
  });
  clear.addEventListener("click", (e) => {
    e.preventDefault();
    clearInputs();
  });
  random.addEventListener("click", async (e) => {
    e.preventDefault();
    const randomInputs = await generateRandomInputs();
    displayRandomInputs(randomInputs);
  });
}

async function predict(data) {
  try {
    const response = await fetch(`${API_BASE_URL}/predict`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    if (!response.ok) {
      throw new Error("error making prediction");
    }
    return await response.json();
  } catch (error) {
    console.error(error);
  }
}

async function generateRandomInputs() {
  try {
    const response = await fetch(`${API_BASE_URL}/random`);
    if (!response.ok) {
      throw new Error("error generating random inputs");
    }
    return await response.json();
  } catch (error) {
    console.error(error);
  }
}

function displayResults(prediction) {
  const loanForm = document.getElementById("loan-form");
  const popupBox = document.getElementById("popup");
  const status = popupBox.children[0].firstElementChild;
  const proability = popupBox.children[1].firstElementChild;
  status.innerText = ` ${prediction.loan_status}`;
  proability.innerText = ` ${Math.round(prediction.probability * 100)}%`;
  if (prediction.loan_status === "Approved") {
    status.style.color = "forestgreen";
  } else {
    status.style.color = "firebrick";
  }
  loanForm.style.pointerEvents = "none";
  loanForm.style.opacity = 0.6;
  popupBox.style.display = "flex";
}

function clearInputs() {
  const ageInput = document.getElementById("age");
  const genderInput = document.getElementById("gender");
  const educationInput = document.getElementById("education");
  const incomeInput = document.getElementById("income");
  const employmentInput = document.getElementById("employment_exp");
  const homeInput = document.getElementById("home_ownership");
  const amountInput = document.getElementById("amount");
  const intentInput = document.getElementById("intent");
  const rateInput = document.getElementById("interest_rate");
  const creditHistInput = document.getElementById("credit_history");
  const scoreInput = document.getElementById("score");
  const defaultNoInput = document.getElementById("default-no");
  const defaultYesInput = document.getElementById("default-yes");
  ageInput.value = null;
  genderInput.value = "Select";
  educationInput.value = "Select";
  incomeInput.value = null;
  employmentInput.value = null;
  homeInput.value = "Select";
  amountInput.value = null;
  intentInput.value = "Select";
  rateInput.value = null;
  creditHistInput.value = null;
  scoreInput.value = null;
  defaultYesInput.checked = false;
  defaultNoInput.checked = false;
}

function displayRandomInputs(inputs) {
  const ageInput = document.getElementById("age");
  const genderInput = document.getElementById("gender");
  const educationInput = document.getElementById("education");
  const incomeInput = document.getElementById("income");
  const employmentInput = document.getElementById("employment_exp");
  const homeInput = document.getElementById("home_ownership");
  const amountInput = document.getElementById("amount");
  const intentInput = document.getElementById("intent");
  const rateInput = document.getElementById("interest_rate");
  const creditHistInput = document.getElementById("credit_history");
  const scoreInput = document.getElementById("score");
  const defaultNoInput = document.getElementById("default-no");
  ageInput.value = inputs.person_age;
  genderInput.value = inputs.person_gender;
  educationInput.value = inputs.person_education;
  incomeInput.value = inputs.person_income;
  employmentInput.value = inputs.person_emp_exp;
  homeInput.value = inputs.person_home_ownership;
  amountInput.value = inputs.loan_amnt;
  intentInput.value = inputs.loan_intent;
  rateInput.value = inputs.loan_int_rate;
  creditHistInput.value = inputs.cb_person_cred_hist_length;
  scoreInput.value = inputs.credit_score;
  defaultNoInput.checked = true;
}
