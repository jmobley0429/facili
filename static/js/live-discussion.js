const discussionFeed = JSON.parse(
  document.querySelector("#feed-item").textContent
);

function createFeedItem(data) {
  console.log(data);
  const feedDiv = document.querySelector("#liveFeed");
  const listItem = document.createElement("div");
  listItem.classList.add("list-item");
  listItem.classList.add("feed");
  const groupTitleElem = document.createElement("h4");
  const responseContentElem = document.createElement("p");
  const facilitator = data.facilitator;
  const response = data.content;
  groupTitleElem.textContent = `${facilitator}'s group`;
  responseContentElem.textContent = response;
  listItem.appendChild(groupTitleElem);
  listItem.appendChild(responseContentElem);
  feedDiv.appendChild(listItem);
}

const topicSocket = new WebSocket(
  `ws://${window.location.host}/ws/topic/${discussionFeed}/`
);
topicSocket.onmessage = function(e) {
  const data = JSON.parse(e.data);
  createFeedItem(data);
};

topicSocket.onclose = function(e) {
  console.error("Topic socket closed unexpectedly");
};

document.querySelector("#responseInput").onkeyup = function(e) {
  if (e.keyCode === 13) {
    document.querySelector("#submitResponseButton").click();
  }
};

document.querySelector("#submitResponseButton").onclick = function(e) {
  const contentInput = document.querySelector("#responseInput");
  const content = contentInput.value;

  topicSocket.send(JSON.stringify({ content: content }));
  contentInput.value = "";
};
