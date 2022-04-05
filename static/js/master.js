import { multiToggle } from "./utils.js";

const formDivs = document.querySelectorAll("div.list-item.edit");
const showDivs = document.querySelectorAll(".list-item");
const editButton = document.querySelector("button#edit");
const shareButton = document.querySelector("button#share");
const addButton = document.querySelector("button#add");
const deleteButton = document.querySelector("button#delete");
const warningSpan = document.querySelector("span.warning");
const hamMenu = document.querySelector("#hamburger");
const cancelEditButtons = document.querySelectorAll("#cancelEdit");
const exitAddModalButton = document.querySelector("#exitEdit");
const exitButton = document.querySelector("#exitShare");
const copyButton = document.querySelector("#copyLink");
const cancelDeleteButton = document.querySelector("#cancelDelete");
const exitDeleteButton = document.querySelector("#exitDelete");
const shareSpan = document.querySelector("#shareLink");

let confirmDeleteButton = document.querySelector("button#confirmDelete");
let selectedDiv;

function hideForms() {
  formDivs.forEach((form, i) => {
    form.addEventListener("keydown", editItemFormSubmit);
  });
}

function addDivSelect(pageType) {
  showDivs.forEach((div, i) => {
    if (!div.classList.contains("edit")) {
      div.addEventListener("click", e => {
        selectDiv(e, pageType);
      });
    }
  });
}

function setFormContent() {
  formDivs.forEach((form, i) => {
    var descSel = '.list-item.edit form > textarea[name="description"]';
    var titleSel = '.list-item.edit form > input[name="title"]';
    var descInputs = document.querySelectorAll(descSel);
    var titleInputs = document.querySelectorAll(titleSel);
    var titles = document.querySelectorAll("div.list-item > div > h3");
    var descs = document.querySelectorAll("div.list-item > div > p");
    titleInputs[i].value = titles[i].textContent;
    descInputs[i].value = descs[i].textContent;
  });
}

function selectDiv(e, pageType) {
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
  if (pageType === "discussion" || pageType === "topic") {
    setButtonValueFromSelectedDiv();
  }
}

function setButtonValueFromSelectedDiv() {
  var baseUrl = window.location.origin;
  shareSpan.textContent = `${baseUrl}/share/${selectedDiv}`;
  editButton.setAttribute("value", selectedDiv);
  shareButton.setAttribute("value", selectedDiv);
  deleteButton.setAttribute("value", selectedDiv);
  confirmDeleteButton.setAttribute("value", selectedDiv);
}

function toggleWarning(e, pageType) {
  if (pageType == "share") {
    warningSpan.textContent = `Copied!`;
    warningSpan.classList.toggle("on");
    setTimeout(() => {
      warningSpan.classList.toggle("on");
    }, 3000);
    return;
  }
  var msg = e.currentTarget.getAttribute("id");
  var button = e.currentTarget;
  var val = button.getAttribute("value");
  var id = button.getAttribute("value");
  if (val === null) {
    warningSpan.textContent = `Select a ${pageType} to ${msg}!`;
    warningSpan.classList.toggle("on");
    setTimeout(() => {
      warningSpan.classList.toggle("on");
    }, 3000);
  }
}

function toggleEditMode(e, pageType) {
  if (e.currentTarget.value == "") {
    toggleWarning(e, pageType);
  } else {
    var formSelector = `div.list-item.edit[value="${selectedDiv}"]`;
    var listItemSelector = `div.list-item[value="${selectedDiv}"]`;
    var showDiv = document.querySelector(listItemSelector);
    var formDiv = document.querySelector(formSelector);
    var form = document.querySelector(`${formSelector} > form`);
    var cls = ["hidden", "selected"];
    multiToggle(showDiv, cls);
    multiToggle(formDiv, cls);
    formDiv.scrollIntoView({
      behavior: "smooth",
      block: "start",
      inline: "start"
    });
  }
}

function editItemFormSubmit(e) {
  if (e.keyCode == 13) {
    e.preventDefault();
    let textArea = e.target;
    let currentText = textArea.value + "\n";
    textArea.value = currentText;
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

function toggleShare(e, pageType) {
  if (e.currentTarget.value === "") {
    toggleWarning(e, pageType);
  } else {
    createShareModal(e);
  }
}

function createShareModal() {
  let shareModal = document.querySelector("#shareModal");
  shareModal.classList.toggle("hidden");
}

function copyToClipboard(text) {
  navigator.clipboard.writeText(text);
}

function openModal(e) {
  let modal = document.querySelector(".modal-bg");
  modal.classList.toggle("hidden");
}
function toggleDelete(e, pageType) {
  if (confirmDeleteButton.value === "") {
    toggleWarning(e, pageType);
  } else {
    let deleteModal = document.querySelector("#deleteModal");
    deleteModal.classList.toggle("hidden");
    confirmDeleteButton.addEventListener("click", deleteItem);
  }
}
function deleteItem(e) {
  let itemId = deleteButton.value;
  let deleteForm = document.querySelector("form#confirmDelete");
  e.currentTarget.value = itemId;
}

export function initEditPages(pageType) {
  cancelEditButtons.forEach((btn, i) => {
    btn.addEventListener("click", toggleEditMode);
  });
  if (pageType == "topic") {
    selectedDiv = shareButton.value;
    let shareSpan = document.querySelector("#shareLink");
    var baseUrl = window.location.origin;
    shareSpan.textContent = `${baseUrl}/share/${selectedDiv}`;
  }
  setFormContent();
  editButton.addEventListener("click", e => {
    toggleEditMode(e, pageType);
  });
  shareButton.addEventListener("click", e => {
    toggleShare(e, pageType);
  });
  deleteButton.addEventListener("click", e => {
    toggleDelete(e, pageType);
  });
  exitButton.addEventListener("click", e => {
    shareModal.classList.toggle("hidden");
  });
  copyButton.addEventListener("click", e => {
    let text = document.querySelector("#shareLink").textContent;
    toggleWarning(e, "share");
    copyToClipboard(text);
    shareModal.classList.toggle("hidden");
  });
  exitAddModalButton.addEventListener("click", openModal);
  addButton.addEventListener("click", openModal);

  [exitDeleteButton, cancelDeleteButton].forEach(btn => {
    btn.addEventListener("click", () => {
      deleteModal.classList.toggle("hidden");
    });
  });
}

export function initStdPages(pageType) {
  handleSideNav();
  hideForms();
}

export function initDiscussPage(pageType) {
  addDivSelect(pageType);
}
