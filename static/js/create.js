import { initPage } from "./master.js";

document.addEventListener("readystatechange", e => {
  initPage("discussion");
});
// const formDivs = document.querySelectorAll("div.list-item.edit");
// const showDivs = document.querySelectorAll(".list-item");
// const editButton = document.querySelector("button#edit");
// const shareButton = document.querySelector("button#share");
// const addButton = document.querySelector("button#add");
// const warningSpan = document.querySelector("span.warning");
// const hamMenu = document.querySelector("#hamburger");
// let selectedDiv;
//
// // handle selecting showing of form/display mode on disc cards
// formDivs.forEach((form, i) => {
//   form.addEventListener("keydown", editItemFormSubmit);
//   form.classList.add("hidden");
//   let div = showDivs[i];
//   div.addEventListener("click", selectDiv);
// });
//
// formDivs.forEach((form, i) => {
//   let descSel = '.list-item.edit form > textarea[name="description"]';
//   let titleSel = '.list-item.edit form > input[name="title"]';
//   let descInputs = document.querySelectorAll(descSel);
//   let titleInputs = document.querySelectorAll(titleSel);
//   let titles = document.querySelectorAll("div.list-item > h3");
//   let descs = document.querySelectorAll("div.list-item > p");
//
//   titleInputs[i].value = titles[i].textContent;
//   descInputs[i].value = descs[i].textContent;
// });
//
// function selectDiv(e) {
//   let div = e.currentTarget;
//   var isSelected = div.classList.contains("selected");
//   showDivs.forEach((item, i) => {
//     item.classList.remove("selected");
//   });
//   if (isSelected) {
//     div.classList.remove("selected");
//   } else {
//     div.classList.add("selected");
//   }
//   selectedDiv = div.getAttribute("value");
//   editButton.setAttribute("value", selectedDiv);
// }
//
// // edit button no item selected warning
// shareButton.addEventListener("click", toggleWarning);
// editButton.addEventListener("click", toggleWarning);
// editButton.addEventListener("click", toggleEditMode);
//
// function toggleWarning(e) {
//   msg = e.currentTarget.getAttribute("id");
//   button = e.currentTarget;
//   val = button.getAttribute("value");
//   id = button.getAttribute("value");
//   if (val === null) {
//     warningSpan.textContent = `Select a discussion to ${msg}!`;
//     warningSpan.classList.toggle("on");
//     setTimeout(() => {
//       warningSpan.classList.toggle("on");
//     }, 3000);
//   }
// }
//
// function toggleEditMode(e) {
//   var formSelector = `div.list-item.edit[value="${selectedDiv}"]`;
//   var listItemSelector = `div.list-item[value="${selectedDiv}"]`;
//   var title = document.querySelector(`${listItemSelector} h3`).textContent;
//   var desc = document.querySelector(`${listItemSelector} p`).textContent;
//   var showDiv = document.querySelector(listItemSelector);
//   var formDiv = document.querySelector(formSelector);
//   var form = document.querySelector(`${formSelector} > form`);
//   var cls = ["hidden", "selected"];
//   multiToggle(showDiv, cls);
//   multiToggle(formDiv, cls);
//   showDiv.removeEventListener("click", selectDiv);
//   formDiv.removeEventListener("click", selectDiv);
//   form.addEventListener("click", e => {
//     e.stopPropagation();
//   });
// }
//
// function cancelEdit(e) {
//   editDiscussion(e);
// }
//
// function editItemFormSubmit(e) {
//   if (e.keyCode == 13) {
//     e.preventDefault();
//     return false;
//   }
// }
//
// //ham menu button
// let sideNav = document.querySelector("nav");
// const html = document.querySelector("html");
//
// hamMenu.addEventListener("click", toggleNav);
// sideNav.addEventListener("click", e => {
//   e.stopPropagation();
// });
// function toggleNav(e) {
//   e.stopPropagation();
//   sideNav.classList.toggle("open");
//   html.addEventListener("click", e => {
//     sideNav.classList.remove("open");
//   });
// }
