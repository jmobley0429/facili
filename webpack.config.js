const path = require('path');

module.exports = {
  entry: '', //path to input file
  output: {
  filename:'index-bundle.js',
  path: path.resolve(__dirname, './static')
  }
}
