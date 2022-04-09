const http = require('http');

const PORT = 1245;
const app = http.createServer((req, res) => {
  res.write('Hello Holberton School!');
  res.end();
});

app.listen(PORT);

module.exports = app;
