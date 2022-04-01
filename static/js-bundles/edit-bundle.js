/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ "./static/js/edit.js":
/*!***************************!*\
  !*** ./static/js/edit.js ***!
  \***************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _master_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./master.js */ \"./static/js/master.js\");\n\ndocument.addEventListener(\"readystatechange\", e => {\n  (0,_master_js__WEBPACK_IMPORTED_MODULE_0__.initPage)(\"topic\");\n});\n\n\n//# sourceURL=webpack://facili/./static/js/edit.js?");

/***/ }),

/***/ "./static/js/master.js":
/*!*****************************!*\
  !*** ./static/js/master.js ***!
  \*****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"initPage\": () => (/* binding */ initPage)\n/* harmony export */ });\n/* harmony import */ var _utils_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./utils.js */ \"./static/js/utils.js\");\n\n\nlet selectedDiv;\n\nconst formDivs = document.querySelectorAll(\"div.list-item.edit\");\nconst showDivs = document.querySelectorAll(\".list-item\");\nconst editButton = document.querySelector(\"button#edit\");\nconst shareButton = document.querySelector(\"button#share\");\nconst addButton = document.querySelector(\"button#add\");\nconst warningSpan = document.querySelector(\"span.warning\");\nconst hamMenu = document.querySelector(\"#hamburger\");\nconst cancelEditButtons = document.querySelectorAll(\"#cancelEdit\");\n\nfunction hideForms() {\n  formDivs.forEach((form, i) => {\n    form.addEventListener(\"keydown\", editItemFormSubmit);\n  });\n}\n\nfunction addDivSelect() {\n  showDivs.forEach((div, i) => {\n    if (!div.classList.contains(\"edit\")) {\n      div.addEventListener(\"click\", selectDiv);\n    }\n  });\n}\n\nfunction setFormContent() {\n  formDivs.forEach((form, i) => {\n    var descSel = '.list-item.edit form > textarea[name=\"description\"]';\n    var titleSel = '.list-item.edit form > input[name=\"title\"]';\n    var descInputs = document.querySelectorAll(descSel);\n    var titleInputs = document.querySelectorAll(titleSel);\n    var titles = document.querySelectorAll(\"div.list-item > h3\");\n    var descs = document.querySelectorAll(\"div.list-item > p\");\n\n    titleInputs[i].value = titles[i].textContent;\n    descInputs[i].value = descs[i].textContent;\n  });\n}\n\nfunction selectDiv(e) {\n  let div = e.currentTarget;\n  var isSelected = div.classList.contains(\"selected\");\n  showDivs.forEach((item, i) => {\n    item.classList.remove(\"selected\");\n  });\n  if (isSelected) {\n    div.classList.remove(\"selected\");\n  } else {\n    div.classList.add(\"selected\");\n  }\n  selectedDiv = div.getAttribute(\"value\");\n  editButton.setAttribute(\"value\", selectedDiv);\n}\n\nfunction toggleWarning(e, pagetype) {\n  var msg = e.currentTarget.getAttribute(\"id\");\n  var button = e.currentTarget;\n  var val = button.getAttribute(\"value\");\n  var id = button.getAttribute(\"value\");\n  if (val === null) {\n    warningSpan.textContent = `Select a ${pagetype} to ${msg}!`;\n    warningSpan.classList.toggle(\"on\");\n    setTimeout(() => {\n      warningSpan.classList.toggle(\"on\");\n    }, 3000);\n  }\n}\n\nfunction toggleEditMode(e) {\n  var formSelector = `div.list-item.edit[value=\"${selectedDiv}\"]`;\n  var listItemSelector = `div.list-item[value=\"${selectedDiv}\"]`;\n  var showDiv = document.querySelector(listItemSelector);\n  var formDiv = document.querySelector(formSelector);\n  var form = document.querySelector(`${formSelector} > form`);\n  var cls = [\"hidden\", \"selected\"];\n  (0,_utils_js__WEBPACK_IMPORTED_MODULE_0__.multiToggle)(showDiv, cls);\n  (0,_utils_js__WEBPACK_IMPORTED_MODULE_0__.multiToggle)(formDiv, cls);\n}\n\nfunction cancelEdit(e) {\n  editDiscussion(e);\n}\n\nfunction editItemFormSubmit(e) {\n  if (e.keyCode == 13) {\n    e.preventDefault();\n    return false;\n  }\n}\n\nfunction handleSideNav() {\n  let sideNav = document.querySelector(\"nav\");\n  const html = document.querySelector(\"html\");\n\n  hamMenu.addEventListener(\"click\", toggleNav);\n  sideNav.addEventListener(\"click\", e => {\n    e.stopPropagation();\n  });\n  function toggleNav(e) {\n    e.stopPropagation();\n    sideNav.classList.toggle(\"open\");\n    html.addEventListener(\"click\", e => {\n      sideNav.classList.remove(\"open\");\n    });\n  }\n}\n\nfunction initPage(pagetype) {\n  if (pagetype == \"discussion\") {\n    shareButton.addEventListener(\"click\", toggleWarning);\n  }\n  cancelEditButtons.forEach((btn, i) => {\n    btn.addEventListener(\"click\", toggleEditMode);\n  });\n\n  hideForms();\n  addDivSelect();\n  handleSideNav();\n  setFormContent();\n  editButton.addEventListener(\"click\", e => {\n    toggleWarning(e, pagetype);\n  });\n  editButton.addEventListener(\"click\", toggleEditMode);\n}\n\n\n//# sourceURL=webpack://facili/./static/js/master.js?");

/***/ }),

/***/ "./static/js/utils.js":
/*!****************************!*\
  !*** ./static/js/utils.js ***!
  \****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"multiToggle\": () => (/* binding */ multiToggle)\n/* harmony export */ });\nfunction multiToggle(elem, classes) {\n  classes.forEach((cls, i) => {\n    elem.classList.toggle(cls);\n  });\n}\n\n\n//# sourceURL=webpack://facili/./static/js/utils.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/define property getters */
/******/ 	(() => {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = (exports, definition) => {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	(() => {
/******/ 		__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = __webpack_require__("./static/js/edit.js");
/******/ 	
/******/ })()
;