import { initEditPages, addDivSelect } from "./master.js";

document.addEventListener("readystatechange", function(e) {
  let pageType = "topic";
  addDivSelect(pageType);
  initEditPages(pageType);
});
