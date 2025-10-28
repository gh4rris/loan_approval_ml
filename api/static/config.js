let API_BASE_URL;
const host = window.location.hostname;
if (host === "localhost" || /^\d+\.\d+\.\d+\.\d+$/.test(host)) {
  API_BASE_URL = `http://${host}:8000`;
} else {
  API_BASE_URL = `http://${host}`;
}
export { API_BASE_URL };
