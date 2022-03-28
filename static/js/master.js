import { multiToggle } from "./utils.js";

let selectedDiv;

const formDivs = document.querySelectorAll("div.list-item.edit");
const showDivs = document.querySelectorAll(".list-item");
const editButton = document.querySelector("button#edit");
const shareButton = document.querySelector("button#share");
const addButton = document.querySelector("button#add");
const warningSpan = document.querySelector("span.warning");
const hamMenu = document.querySelector("#hamburger");

function hideForms() {
  formDivs.forEach((form, i) => {
    form.addEventListener("keydown", editItemFormSubmit);
  });
}

function addDivSelect() {
  showDivs.forEach((div, i) => {
    if (!div.classList.contains("edit")) {
      div.addEventListener("click", selectDiv);
    }
  });
}

function setFormContent() {
  formDivs.forEach((form, i) => {
    var descSel = '.list-item.edit form > textarea[name="description"]';
    var titleSel = '.list-item.edit form > input[name="title"]';
    var descInputs = document.querySelectorAll(descSel);
    var titleInputs = document.querySelectorAll(titleSel);
    var titles = document.querySelectorAll("div.list-item > h3");
    var descs = document.querySelectorAll("div.list-item > p");

    titleInputs[i].value = titles[i].textContent;
    descInputs[i].value = descs[i].textContent;
  });
}

function selectDiv(e) {
  let div = e.currentTarget;
  var isSelected = div.classList.contains("selected");
  showDivs.forEach((item, i) => {
    item.classList.remove("selected");
  });
  if (isSelected) {
    div.classList.remove("selected");
  } else {
    div.classList.add("selected");
  }
  selectedDiv = div.getAttribute("value");
  editButton.setAttribute("value", selectedDiv);
}

function toggleWarning(e, pagetype) {
  var msg = e.currentTarget.getAttribute("id");
  var button = e.currentTarget;
  var val = button.getAttribute("value");
  var id = button.getAttribute("value");
  if (val === null) {
    warningSpan.textContent = `Select a ${pagetype} to ${msg}!`;
    warningSpan.classList.toggle("on");
    setTimeout(() => {
      warningSpan.classList.toggle("on");
    }, 3000);
  }
}

function toggleEditMode(e) {
  var formSelector = `div.list-item.edit[value="${selectedDiv}"]`;
  var listItemSelector = `div.list-item[value="${selectedDiv}"]`;
  var showDiv = document.querySelector(listItemSelector);
  var formDiv = document.querySelector(formSelector);
  var form = document.querySelector(`${formSelector} > form`);
  var cls = ["hidden", "selected"];
  multiToggle(showDiv, cls);
  multiToggle(formDiv, cls);
  showDiv.removeEventListener("click", selectDiv);
  formDiv.removeEventListener("click", selectDiv);
  form.addEventListener("click", e => {
    e.stopPropagation();
  });
}

function cancelEdit(e) {
  editDiscussion(e);
}

function editItemFormSubmit(e) {
  if (e.keyCode == 13) {
    e.preventDefault();
    return false;
  }
}

function handleSideNav() {
  let sideNav = document.querySelector("nav");
  const html = document.querySelector("html");

  hamMenu.addEventListener("click", toggleNav);
  sideNav.addEventListener("click", e => {
    e.stopPropagation();
  });
  function toggleNav(e) {
    e.stopPropagation();
    sideNav.classList.toggle("open");
    html.addEventListener("click", e => {
      sideNav.classList.remove("open");
    });
  }
}

export function initPage(pagetype) {
  if (pagetype == "discussion") {
    shareButton.addEventListener("click", toggleWarning);
  }
  hideForms();
  addDivSelect();
  handleSideNav();
  setFormContent();
  editButton.addEventListener("click", e => {
    toggleWarning(e, pagetype);
  });
  editButton.addEventListener("click", toggleEditMode);
}
