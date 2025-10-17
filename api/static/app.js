import { API_BASE_URL } from "./config.js";

main();

function main() {
  const form = document.getElementById("loan-form");
  const popupBtn = document.getElementById("popup-btn");
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

function displayResults(prediction) {
  const loanForm = document.getElementById("loan-form");
  const popupBox = document.getElementById("popup");
  popupBox.children[0].firstElementChild.innerText = ` ${prediction.loan_status}`;
  popupBox.children[1].firstElementChild.innerText = ` ${prediction.probability}`;
  loanForm.style.pointerEvents = "none";
  loanForm.style.opacity = 0.6;
  popupBox.style.display = "block";
}
