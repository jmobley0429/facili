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

/***/ "./static/js/live-discussion.js":
/*!**************************************!*\
  !*** ./static/js/live-discussion.js ***!
  \**************************************/
/***/ (() => {

eval("const discussionFeed = JSON.parse(\n  document.querySelector(\"#feed-item\").textContent\n);\n\nfunction createFeedItem(data) {\n  console.log(data);\n  const feedDiv = document.querySelector(\"#liveFeed\");\n  const listItem = document.createElement(\"div\");\n  listItem.classList.add(\"list-item\");\n  listItem.classList.add(\"feed\");\n  const groupTitleElem = document.createElement(\"h4\");\n  const responseContentElem = document.createElement(\"p\");\n  const facilitator = data.facilitator;\n  const response = data.content;\n  groupTitleElem.textContent = `${facilitator}'s group`;\n  responseContentElem.textContent = response;\n  listItem.appendChild(groupTitleElem);\n  listItem.appendChild(responseContentElem);\n  feedDiv.appendChild(listItem);\n}\n\nconst topicSocket = new WebSocket(\n  `ws://${window.location.host}/ws/topic/${discussionFeed}/`\n);\ntopicSocket.onmessage = function(e) {\n  const data = JSON.parse(e.data);\n  createFeedItem(data);\n};\n\ntopicSocket.onclose = function(e) {\n  console.error(\"Topic socket closed unexpectedly\");\n};\n\ndocument.querySelector(\"#responseInput\").onkeyup = function(e) {\n  if (e.keyCode === 13) {\n    document.querySelector(\"#submitResponseButton\").click();\n  }\n};\n\ndocument.querySelector(\"#submitResponseButton\").onclick = function(e) {\n  const contentInput = document.querySelector(\"#responseInput\");\n  const content = contentInput.value;\n\n  topicSocket.send(JSON.stringify({ content: content }));\n  contentInput.value = \"\";\n};\n\n\n//# sourceURL=webpack://facili/./static/js/live-discussion.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./static/js/live-discussion.js"]();
/******/ 	
/******/ })()
;