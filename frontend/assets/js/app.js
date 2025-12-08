// Main entrypoint for frontend
// import { initStudentController } from "./controllers/studentcontroller.js";
import { router } from "./router/viewrouter.js";

// Initialize app on page load
window.addEventListener("DOMContentLoaded", () => {
  router();
  // initStudentController();
});