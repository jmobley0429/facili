import { initStdPages, initDiscussPage } from "./master.js";

document.addEventListener("readystatechange", e => {
  initDiscussPage("discuss");
});
