const formDivs = document.querySelectorAll("div.list-item.edit");
const showDivs = document.querySelectorAll(".list-item");
const editButton = document.querySelector("#editButton");
const shareButton = document.querySelector("#shareutton");
const editWarningSpan = document.querySelector("#editButton+span");
const shareWarningSpan = document.querySelector("#shareButton+span");
let selectedDisc;

formDivs.forEach((item, i) => {
  item.classList.add("hidden");
});

showDivs.forEach((div, i) => {
  div.addEventListener("click", function(e) {
    div.classList.toggle("selected");
    selectedDisc = div.getAttribute("value");
    editButton.setAttribute("value", selectedDisc);
  });
});

editButton.addEventListener("click", function(e) {
  let val = editButton.getAttribute("value");
  if (val === null) {
    editWarningSpan.classList.toggle("on");
    editWarningSpan.classList.toggle("on");
  } else {
    let showDiv = document.querySelector(`div.list-item[value="${val}"]`);
    let formDiv = document.querySelector(`div.list-item.edit[value="${val}"]`);
    showDiv.classList.toggle("hidden");
    formDiv.classList.toggle("hidden");
  }
});
