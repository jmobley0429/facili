import { initEditPages } from "./master.js";

document.addEventListener("readystatechange", e => {
  initEditPages("topic");
});
