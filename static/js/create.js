import { initEditPages, addDivSelect, generateTooltips } from "./master.js";

document.addEventListener("readystatechange", function(e) {
  let pageType = "discussion";
  addDivSelect(pageType);
  initEditPages(pageType);
  generateTooltips(pageType);
});
