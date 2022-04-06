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

/***/ "./static/js/master.js":
/*!*****************************!*\
  !*** ./static/js/master.js ***!
  \*****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"addDivSelect\": () => (/* binding */ addDivSelect),\n/* harmony export */   \"generateTooltips\": () => (/* binding */ generateTooltips),\n/* harmony export */   \"initDiscussPage\": () => (/* binding */ initDiscussPage),\n/* harmony export */   \"initEditPages\": () => (/* binding */ initEditPages),\n/* harmony export */   \"initStdPages\": () => (/* binding */ initStdPages)\n/* harmony export */ });\n/* harmony import */ var _utils_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./utils.js */ \"./static/js/utils.js\");\n\n\n\nconst formDivs = document.querySelectorAll(\"div.list-item.edit\");\nconst showDivs = document.querySelectorAll(\".list-item\");\nconst editButton = document.querySelector(\"button#edit\");\nconst shareButton = document.querySelector(\"button#share\");\nconst addButton = document.querySelector(\"button#add\");\nconst deleteButton = document.querySelector(\"button#delete\");\nconst warningSpan = document.querySelector(\"span.warning\");\nconst hamMenu = document.querySelector(\"#hamburger\");\nconst cancelEditButtons = document.querySelectorAll(\"#cancelEdit\");\nconst exitAddModalButton = document.querySelector(\"#exitEdit\");\nconst exitButton = document.querySelector(\"#exitShare\");\nconst copyButton = document.querySelector(\"#copyLink\");\nconst cancelDeleteButton = document.querySelector(\"#cancelDelete\");\nconst exitDeleteButton = document.querySelector(\"#exitDelete\");\nconst shareSpan = document.querySelector(\"#shareLink\");\n\nlet confirmDeleteButton = document.querySelector(\"button#confirmDelete\");\nlet selectedDiv;\n\nfunction hideForms() {\n  formDivs.forEach((form, i) => {\n    form.addEventListener(\"keydown\", editItemFormSubmit);\n  });\n}\n\nfunction addDivSelect(pageType) {\n  showDivs.forEach((div, i) => {\n    if (!div.classList.contains(\"edit\")) {\n      div.addEventListener(\"click\", e => {\n        selectDiv(e, pageType);\n      });\n    }\n  });\n}\n\nfunction setFormContent() {\n  formDivs.forEach((form, i) => {\n    var descSel = '.list-item.edit form > textarea[name=\"description\"]';\n    var titleSel = '.list-item.edit form > input[name=\"title\"]';\n    var descInputs = document.querySelectorAll(descSel);\n    var titleInputs = document.querySelectorAll(titleSel);\n    var titles = document.querySelectorAll(\"div.list-item > div > h3\");\n    var descs = document.querySelectorAll(\"div.list-item > div > p\");\n    titleInputs[i].value = titles[i].textContent;\n    descInputs[i].value = descs[i].textContent;\n  });\n}\n\nfunction selectDiv(e, pageType) {\n  let div = e.currentTarget;\n  var isSelected = div.classList.contains(\"selected\");\n  showDivs.forEach((item, i) => {\n    item.classList.remove(\"selected\");\n  });\n  if (isSelected) {\n    div.classList.remove(\"selected\");\n  } else {\n    div.classList.add(\"selected\");\n  }\n  selectedDiv = div.getAttribute(\"value\");\n  if (pageType === \"discussion\" || pageType === \"topic\") {\n    setButtonValueFromSelectedDiv();\n  }\n}\n\nfunction setButtonValueFromSelectedDiv() {\n  var baseUrl = window.location.origin;\n  shareSpan.textContent = `${baseUrl}/share/${selectedDiv}`;\n  editButton.setAttribute(\"value\", selectedDiv);\n  shareButton.setAttribute(\"value\", selectedDiv);\n  deleteButton.setAttribute(\"value\", selectedDiv);\n  confirmDeleteButton.setAttribute(\"value\", selectedDiv);\n}\n\nfunction toggleWarning(e, pageType) {\n  if (pageType == \"share\") {\n    warningSpan.textContent = `Copied!`;\n    warningSpan.classList.toggle(\"on\");\n    setTimeout(() => {\n      warningSpan.classList.toggle(\"on\");\n    }, 3000);\n    return;\n  }\n  var msg = e.currentTarget.getAttribute(\"id\");\n  var button = e.currentTarget;\n  var val = button.getAttribute(\"value\");\n  var id = button.getAttribute(\"value\");\n  if (val === null) {\n    warningSpan.textContent = `Select a ${pageType} to ${msg}!`;\n    warningSpan.classList.toggle(\"on\");\n    setTimeout(() => {\n      warningSpan.classList.toggle(\"on\");\n    }, 3000);\n  }\n}\n\nfunction toggleEditMode(e, pageType) {\n  if (e.currentTarget.value == \"\") {\n    toggleWarning(e, pageType);\n  } else {\n    var formSelector = `div.list-item.edit[value=\"${selectedDiv}\"]`;\n    var listItemSelector = `div.list-item[value=\"${selectedDiv}\"]`;\n    var showDiv = document.querySelector(listItemSelector);\n    var formDiv = document.querySelector(formSelector);\n    var form = document.querySelector(`${formSelector} > form`);\n    var cls = [\"hidden\", \"selected\"];\n    (0,_utils_js__WEBPACK_IMPORTED_MODULE_0__.multiToggle)(showDiv, cls);\n    (0,_utils_js__WEBPACK_IMPORTED_MODULE_0__.multiToggle)(formDiv, cls);\n    formDiv.scrollIntoView({\n      behavior: \"smooth\",\n      block: \"start\",\n      inline: \"start\"\n    });\n  }\n}\n\nfunction editItemFormSubmit(e) {\n  if (e.keyCode == 13) {\n    e.preventDefault();\n    let textArea = e.target;\n    let currentText = textArea.value + \"\\n\";\n    textArea.value = currentText;\n  }\n}\n\nfunction handleSideNav() {\n  let sideNav = document.querySelector(\"nav\");\n  const html = document.querySelector(\"html\");\n\n  hamMenu.addEventListener(\"click\", toggleNav);\n  sideNav.addEventListener(\"click\", e => {\n    e.stopPropagation();\n  });\n  function toggleNav(e) {\n    e.stopPropagation();\n    sideNav.classList.toggle(\"open\");\n    html.addEventListener(\"click\", e => {\n      sideNav.classList.remove(\"open\");\n    });\n  }\n}\n\nfunction toggleShare(e, pageType) {\n  if (e.currentTarget.value === \"\") {\n    toggleWarning(e, pageType);\n  } else {\n    createShareModal(e);\n  }\n}\n\nfunction createShareModal() {\n  let shareModal = document.querySelector(\"#shareModal\");\n  shareModal.classList.toggle(\"hidden\");\n}\n\nfunction copyToClipboard(text) {\n  navigator.clipboard.writeText(text);\n}\n\nfunction openModal(e) {\n  let modal = document.querySelector(\".modal-bg\");\n  modal.classList.toggle(\"hidden\");\n}\nfunction toggleDelete(e, pageType) {\n  if (confirmDeleteButton.value === \"\") {\n    toggleWarning(e, pageType);\n  } else {\n    let deleteModal = document.querySelector(\"#deleteModal\");\n    deleteModal.classList.toggle(\"hidden\");\n    confirmDeleteButton.addEventListener(\"click\", deleteItem);\n  }\n}\nfunction deleteItem(e) {\n  let itemId = deleteButton.value;\n  let deleteForm = document.querySelector(\"form#confirmDelete\");\n  e.currentTarget.value = itemId;\n}\n\nfunction initEditPages(pageType) {\n  cancelEditButtons.forEach((btn, i) => {\n    btn.addEventListener(\"click\", toggleEditMode);\n  });\n  if (pageType == \"topic\") {\n    selectedDiv = shareButton.value;\n    let shareSpan = document.querySelector(\"#shareLink\");\n    var baseUrl = window.location.origin;\n    shareSpan.textContent = `${baseUrl}/share/${selectedDiv}`;\n  }\n  setFormContent();\n  editButton.addEventListener(\"click\", e => {\n    toggleEditMode(e, pageType);\n  });\n  shareButton.addEventListener(\"click\", e => {\n    toggleShare(e, pageType);\n  });\n  deleteButton.addEventListener(\"click\", e => {\n    toggleDelete(e, pageType);\n  });\n  exitButton.addEventListener(\"click\", e => {\n    shareModal.classList.toggle(\"hidden\");\n  });\n  copyButton.addEventListener(\"click\", e => {\n    let text = document.querySelector(\"#shareLink\").textContent;\n    toggleWarning(e, \"share\");\n    copyToClipboard(text);\n    shareModal.classList.toggle(\"hidden\");\n  });\n  exitAddModalButton.addEventListener(\"click\", openModal);\n  addButton.addEventListener(\"click\", openModal);\n\n  [exitDeleteButton, cancelDeleteButton].forEach(btn => {\n    btn.addEventListener(\"click\", () => {\n      deleteModal.classList.toggle(\"hidden\");\n    });\n  });\n}\n\nfunction initStdPages(pageType) {\n  handleSideNav();\n  hideForms();\n}\n\nfunction initDiscussPage(pageType) {\n  addDivSelect(pageType);\n}\n\nfunction generateTooltips(pageType) {\n  let buttonDivs = [...document.querySelectorAll(\"div.button\")];\n  let buttons = document.querySelectorAll(\"div.button > button\");\n  let verbs = {\n    Add: \"a new\",\n    Edit: \"the selected\",\n    Delete: \"the selected\",\n    Share: \"the selected\"\n  };\n\n  buttons.forEach((btn, i) => {\n    var timer;\n    var touchduration = 700;\n    function touchstart() {\n      e.preventDefault();\n      if (!timer) {\n        timer = setTimeout(onlongtouch, touchduration);\n      }\n    }\n    function touchend() {\n      let span = div.getElementsByClassName(\"tooltip\")[0];\n      clearTimeout(timer);\n      span.style.display = \"none\";\n    }\n\n    let onlongtouch = function() {\n      hoverTooltip;\n    };\n    let id = new _utils_js__WEBPACK_IMPORTED_MODULE_0__[\"default\"](btn.getAttribute(\"id\")).capitalize();\n    let tooltip = document.createElement(\"span\");\n    let middleText = verbs[id];\n    tooltip.textContent = `${id} ${middleText} ${pageType}.`;\n    tooltip.classList.add(\"tooltip\");\n    buttonDivs[i].appendChild(tooltip);\n    buttonDivs[i].onmouseover = function(e) {\n      hoverTooltip(e);\n    };\n    buttonDivs[i].addEventListener(\"touchstart\", touchstart);\n    buttonDivs[i].addEventListener(\"touchend\", touchend);\n  });\n}\n\nfunction clearTooltip(e) {}\n\nfunction hoverTooltip(e) {\n  let div = e.currentTarget;\n  let span = div.getElementsByClassName(\"tooltip\")[0];\n  var timeout = setTimeout(() => {\n    span.style.display = \"inline-block\";\n  }, 700);\n  div.onmouseout = function() {\n    clearTimeout(timeout);\n    span.style.display = \"none\";\n  };\n}\n\n\n//# sourceURL=webpack://facili/./static/js/master.js?");

/***/ }),

/***/ "./static/js/masterInit.js":
/*!*********************************!*\
  !*** ./static/js/masterInit.js ***!
  \*********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _master_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./master.js */ \"./static/js/master.js\");\n\n\ndocument.addEventListener(\"readystatechange\", function(e) {\n  (0,_master_js__WEBPACK_IMPORTED_MODULE_0__.initStdPages)();\n});\n\n\n//# sourceURL=webpack://facili/./static/js/masterInit.js?");

/***/ }),

/***/ "./static/js/utils.js":
/*!****************************!*\
  !*** ./static/js/utils.js ***!
  \****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (/* binding */ StringObj),\n/* harmony export */   \"multiToggle\": () => (/* binding */ multiToggle)\n/* harmony export */ });\nfunction multiToggle(elem, classes) {\n  classes.forEach((cls, i) => {\n    elem.classList.toggle(cls);\n  });\n}\n\nclass StringObj {\n  constructor(string) {\n    this.string = string;\n  }\n  capitalize() {\n    let firstLetter = this.string.charAt(0).toUpperCase();\n    let rest = this.string.slice(1);\n    return `${firstLetter}${rest}`;\n  }\n}\n\n\n//# sourceURL=webpack://facili/./static/js/utils.js?");

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
/******/ 	var __webpack_exports__ = __webpack_require__("./static/js/masterInit.js");
/******/ 	
/******/ })()
;