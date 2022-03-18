import { initPage } from "./master.js";
document.addEventListener("readystatechange", e => {
  initPage("topic");
});
