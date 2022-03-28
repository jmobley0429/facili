import { initPage } from "./master.js";

document.addEventListener("readystatechange", function(e) {
  initPage("discussion");
});
