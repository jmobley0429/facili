import { initPage } from "./master.js";

document.addEventListener("readystatechange", function(e) {
  initPage("discussion");
});

const addButton = document.querySelector("#addButton");
addButton.addEventListener("click", openModal);
function openModal(e) {
  console.log("clicked");
  let modal = document.querySelector(".modal-bg");
  modal.classList.toggle("hidden");
}
