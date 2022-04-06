const facilitatorSelect =

const addFacSocket = new WebSocket(
  `ws://${window.location.host}/ws/topic/${discussionFeed}/`
);
addFacSocket.onmessage = function(e) {
  const data = JSON.parse(e.data);
  processData
};

addFacSocket.onclose = function(e) {
  console.error("Topic socket closed unexpectedly");
};

document.querySelector("#responseInput").onkeyup = function(e) {
  if (e.keyCode === 13) {
    document.querySelector("#submitResponseButton").click();
  }
};

document.querySelector("#submitResponseButton").onclick = function(e) {
  const contentInput = document.querySelector("#responseInput");
  const topicId = document.querySelector("#submitResponseButton");
  const content = contentInput.value;
  addFacSocket.send(JSON.stringify({ content: content, topic: topicId }));
  contentInput.value = "";
};
