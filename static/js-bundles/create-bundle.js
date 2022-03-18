/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./static/js/create.js":
/*!*****************************!*\
  !*** ./static/js/create.js ***!
  \*****************************/
/***/ (() => {

eval("const formDivs = document.querySelectorAll(\"div.list-item.edit\");\nconst showDivs = document.querySelectorAll(\".list-item\");\nconst editButton = document.querySelector(\"button#edit\");\nconst shareButton = document.querySelector(\"button#share\");\nconst addButton = document.querySelector(\"button#add\");\nconst warningSpan = document.querySelector(\"span.warning\");\nconst hamMenu = document.querySelector(\"#hamburger\");\n\n// handle selecting showing of form/display mode on disc cards\nlet selectedDisc;\nformDivs.forEach((item, i) => {\n  item.classList.add(\"hidden\");\n});\n\nshowDivs.forEach((div, i) => {\n  div.addEventListener(\"click\", function(e) {\n    div.classList.toggle(\"selected\");\n    selectedDisc = div.getAttribute(\"value\");\n    editButton.setAttribute(\"value\", selectedDisc);\n  });\n});\n\n// edit button no item selected warning\nshareButton.addEventListener(\"click\", toggleWarning);\neditButton.addEventListener(\"click\", toggleWarning);\n\nfunction toggleWarning(e) {\n  msg = e.currentTarget.getAttribute(\"id\");\n  button = e.currentTarget;\n  val = button.getAttribute(\"value\");\n  id = button.getAttribute(\"value\");\n  if (val === null) {\n    warningSpan.textContent = `Select a discussion to ${msg}!`;\n    warningSpan.classList.toggle(\"on\");\n    setTimeout(() => {\n      warningSpan.classList.toggle(\"on\");\n    }, 3000);\n  }\n}\n\n//ham menu button\nlet sideNav = document.querySelector(\"nav\");\nhamMenu.addEventListener(\"click\", function(e) {\n  sideNav.classList.toggle(\"closed\");\n  document.addEventListener(\"click\", e => {\n    console.log(sideNav.contains(e.target));\n    if (!e.target.id == \"sideNav\" && !sideNav.contains(e.target)) {\n      sideNav.classList.toggle(\"closed\");\n    }\n  });\n});\n\n\n//# sourceURL=webpack://facili/./static/js/create.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./static/js/create.js"]();
/******/ 	
/******/ })()
;