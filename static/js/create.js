const formDivs = document.querySelectorAll("div.list-item.edit");
const showDivs = document.querySelectorAll(".list-item");
const editButton = document.querySelector("#editButton");
const shareButton = document.querySelector("#shareButton");
const editWarningSpan = document.querySelector("#editButton + span");
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
// edit button no item selected warning
editButton.addEventListener("click", function() {
  val = editButton.getAttribute("value");
  if (val === null) {
    editWarningSpan.classList.toggle("on");
    setTimeout(() => {
      editWarningSpan.classList.toggle("on");
    }, 2000);
  }
});

// share button no item selected warning

shareButton.addEventListener("click", function() {
  val = editButton.getAttribute("value");
  if (val === null) {
    shareWarningSpan.classList.toggle("on");
    setTimeout(() => {
      shareWarningSpan.classList.toggle("on");
    }, 2000);
  }
});
