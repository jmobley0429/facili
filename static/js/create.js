import { initPage } from "./master.js";

document.addEventListener("readystatechange", function(e) {
  initEditPages("discussion");
});
