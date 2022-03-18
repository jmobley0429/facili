const formDivs = document.querySelectorAll("div.list-item.edit");
const showDivs = document.querySelectorAll(".list-item");
const editButton = document.querySelector("button#edit");
const shareButton = document.querySelector("button#share");
const addButton = document.querySelector("button#add");
const warningSpan = document.querySelector("span.warning");
const hamMenu = document.querySelector("#hamburger");

// handle selecting showing of form/display mode on disc cards
let selectedDisc;
formDivs.forEach((item, i) => {
  item.classList.add("hidden");
});

showDivs.forEach((div, i) => {
  div.addEventListener("click", selectDiv);
});

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
  selectedDisc = div.getAttribute("value");
  editButton.setAttribute("value", selectedDisc);
}

// edit button no item selected warning
shareButton.addEventListener("click", toggleWarning);
editButton.addEventListener("click", toggleWarning);
editButton.addEventListener("click", editDiscusssion);

function toggleWarning(e) {
  msg = e.currentTarget.getAttribute("id");
  button = e.currentTarget;
  val = button.getAttribute("value");
  id = button.getAttribute("value");
  if (val === null) {
    warningSpan.textContent = `Select a discussion to ${msg}!`;
    warningSpan.classList.toggle("on");
    setTimeout(() => {
      warningSpan.classList.toggle("on");
    }, 3000);
  }
}

function editDiscusssion(e) {
  var selector = `div.list-item[value="${selectedDisc}"]`;
  var formSelector = `div.list-item.edit[value="${selectedDisc}"]`;
  var titleInpSel = `${formSelector} input[name="title"]`;
  var descInpSel = `${formSelector} textarea[name="description"]`;
  var titleInput = document.querySelector(titleInpSel);
  var descInput = document.querySelector(descInpSel);
  var title = document.querySelector(`${selector} h3`).textContent;
  var desc = document.querySelector(`${selector} p`).textContent;
  var showDiv = document.querySelector(selector);
  var formDiv = document.querySelector(formSelector);

  console.log("hidden");
  showDiv.classList.toggle("hidden");
  showDiv.classList.toggle("selected");
  titleInput.value = title;
  descInput.value = desc;
  formDiv.classList.toggle("hidden");
  formDiv.classList.toggle("selected");
}

function onInput() {
  this.style.height = "auto";
  this.style.height = this.scrollHeight + "px";
}
//ham menu button
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
