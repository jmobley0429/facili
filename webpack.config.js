const path = require("path");

module.exports = {
  entry: "./static/js/create.js", //path to input file
  output: {
    filename: "create-bundle.js",
    path: path.resolve(__dirname, "./static/js-bundles/")
  }
};
