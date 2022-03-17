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

eval("const formDivs = document.querySelectorAll(\"div.list-item.edit\");\nconst showDivs = document.querySelectorAll(\".list-item\");\nconst editButton = document.querySelector(\"#editButton\");\nconst shareButton = document.querySelector(\"#shareButton\");\nconst editWarningSpan = document.querySelector(\"#editButton + span\");\nconst shareWarningSpan = document.querySelector(\"#shareButton+span\");\nlet selectedDisc;\n\nformDivs.forEach((item, i) => {\n  item.classList.add(\"hidden\");\n});\n\nshowDivs.forEach((div, i) => {\n  div.addEventListener(\"click\", function(e) {\n    div.classList.toggle(\"selected\");\n    selectedDisc = div.getAttribute(\"value\");\n    editButton.setAttribute(\"value\", selectedDisc);\n  });\n});\n// edit button no item selected warning\neditButton.addEventListener(\"click\", function() {\n  val = editButton.getAttribute(\"value\");\n  if (val === null) {\n    editWarningSpan.classList.toggle(\"on\");\n    setTimeout(() => {\n      editWarningSpan.classList.toggle(\"on\");\n    }, 2000);\n  }\n});\n\n// share button no item selected warning\n\nshareButton.addEventListener(\"click\", function() {\n  val = editButton.getAttribute(\"value\");\n  if (val === null) {\n    shareWarningSpan.classList.toggle(\"on\");\n    setTimeout(() => {\n      shareWarningSpan.classList.toggle(\"on\");\n    }, 2000);\n  }\n});\n\n\n//# sourceURL=webpack://facili/./static/js/create.js?");

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