const path = require("path");

module.exports = [
  {
    entry: "./static/js/create.js", //path to input file
    output: {
      filename: "create-bundle.js",
      path: path.resolve(__dirname, "./static/js-bundles/")
    }
  },
  {
    entry: "./static/js/edit.js", //path to input file
    output: {
      filename: "edit-bundle.js",
      path: path.resolve(__dirname, "./static/js-bundles/")
    }
  },
  {
    entry: "./static/js/live-discussion.js", //path to input file
    output: {
      filename: "live-discussion-bundle.js",
      path: path.resolve(__dirname, "./static/js-bundles/")
    }
  },
  {
    entry: "./static/js/share.js", //path to input file
    output: {
      filename: "share-bundle.js",
      path: path.resolve(__dirname, "./static/js-bundles/")
    }
  },
  {
    entry: "./static/js/results.js", //path to input file
    output: {
      filename: "results-bundle.js",
      path: path.resolve(__dirname, "./static/js-bundles/")
    }
  },
  {
    entry: "./static/js/discuss.js", //path to input file
    output: {
      filename: "discuss-bundle.js",
      path: path.resolve(__dirname, "./static/js-bundles/")
    }
  },
  {
    entry: "./static/js/masterInit.js", //path to input file
    output: {
      filename: "master-bundle.js",
      path: path.resolve(__dirname, "./static/js-bundles/")
    }
  }
];
