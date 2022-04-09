const express = require('express');

const fs = require('fs');

const app = express();
const port = 1245;
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

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.set('content-type', 'text/plain');
  const arrayToSend = [];
  try {
    arrayToSend.push('This is the list of our students\n');
    const data = await countStudents(db);
    arrayToSend.push(`Number of students: ${data.numOfStudents}\n`);
    delete data.numOfStudents;
    const keysFinal = Object.keys(data);
    keysFinal.forEach((item, idx) => {
      if (idx === keysFinal.length - 1) {
        arrayToSend.push(`Number of students in ${item}: ${data[item].length}. List: ${data[item].join(', ')}`);
      } else {
        arrayToSend.push(`Number of students in ${item}: ${data[item].length}. List: ${data[item].join(', ')}\n`);
      }
    });
    res.send(arrayToSend.join(''));
  } catch (err) {
    arrayToSend.push(err.message);
    res.send(arrayToSend.join(''));
  }
});

app.listen(port);

module.exports = app;
