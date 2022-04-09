const http = require('http');
const fs = require('fs');

const PORT = 1245;
const db = process.argv[2];

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, { encoding: 'utf8' }, (err, data) => {
      if (err) {
        return reject(new Error('Cannot load the database'));
      }
      const dataGot = data.split('\n');
      const dataSeparated = dataGot.filter((items) => items !== '').map((item) => item.split(','));
      dataSeparated.shift();
      const acum = { numOfStudents: dataSeparated.length };
      for (const student of dataSeparated) {
        const keys = Object.keys(acum);
        if (keys.includes(student[3])) {
          acum[student[3]].push(student[0]);
        } else {
          acum[student[3]] = [student[0]];
        }
      }
      return resolve(acum);
    });
  });
}

const app = http.createServer(async (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  if (req.url === '/') {
    res.write('Hello Holberton School!');
  }
  if (req.url === '/students') {
    try {
      res.write('This is the list of our students\n');
      const data = await countStudents(db);
      res.write(`Number of students: ${data.numOfStudents}\n`);
      delete data.numOfStudents;
      const keysFinal = Object.keys(data);
      keysFinal.forEach((item, idx) => {
        if (idx === keysFinal.length - 1) {
          res.write(`Number of students in ${item}: ${data[item].length}. List: ${data[item].join(', ')}`);
        } else {
          res.write(`Number of students in ${item}: ${data[item].length}. List: ${data[item].join(', ')}\n`);
        }
      });
    } catch (err) {
      res.write(err.message);
    }
  }
  res.end();
});

app.listen(PORT);

module.exports = app;
