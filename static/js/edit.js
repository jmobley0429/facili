import { initPage } from "./master.js";

const sel = document.querySelector("select");
const options = sel.options;

document.addEventListener("readystatechange", e => {
  initPage("topic");
});
