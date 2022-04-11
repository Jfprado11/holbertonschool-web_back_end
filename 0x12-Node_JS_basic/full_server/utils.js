const fs = require('fs');

export default function readDatabase(path) {
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
