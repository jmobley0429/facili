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
  div.addEventListener("click", function(e) {
    div.classList.toggle("selected");
    selectedDisc = div.getAttribute("value");
    editButton.setAttribute("value", selectedDisc);
  });
});

// edit button no item selected warning
shareButton.addEventListener("click", toggleWarning);
editButton.addEventListener("click", toggleWarning);

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

//ham menu button
let sideNav = document.querySelector("nav");
hamMenu.addEventListener("click", function(e) {
  sideNav.classList.toggle("closed");
  document.addEventListener("click", e => {
    console.log(sideNav.contains(e.target));
    if (!e.target.id == "sideNav" && !sideNav.contains(e.target)) {
      sideNav.classList.toggle("closed");
    }
  });
});
