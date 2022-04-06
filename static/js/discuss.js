import { initStdPages, initDiscussPage } from "./master.js";

document.addEventListener("readystatechange", e => {
  initDiscussPage("discuss");
});

const facilitatorDiv = document.querySelector("div#facilitatorList");
const openFacbutton = document.querySelector("#openFacilitatorList");
const facilitatorList = document.querySelector("ul#facilitatorList");

openFacbutton.onclick = function(e) {
  let contentDiv = facilitatorDiv.getElementsByClassName("content")[0];
  facilitatorDiv.classList.toggle("selected");
  contentDiv.classList.toggle("hidden");
  openFacbutton.classList.toggle("mirror-y");
};
const openTopicButton = document.querySelector("#openTopic");
openTopicButton.onclick = function(e) {
  let id = e.currentTarget.getAttribute("value");
  let topicDiv = document.querySelector(`div.list-item[value="${id}"]`);
  let chatDiv = document.querySelector(`div.list-item.edit[value="${id}"]`);
  topicDiv.classList.toggle("hidden");
  chatDiv.classList.toggle("hidden");
};
