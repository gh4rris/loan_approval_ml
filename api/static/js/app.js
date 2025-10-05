import { API_BASE_URL } from "./config.js";

main();

function main() {
  const form = document.getElementById("loan-form");
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData.entries());
    console.log(JSON.stringify(data));
    const prediction = await predict(data);
    console.log(prediction);
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
