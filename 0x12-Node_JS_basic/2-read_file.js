const fs = require('fs');

function countStudents(path) {
  try {
    const fileCsv = fs.readFileSync(path, { encoding: 'utf8' });
    const dataGot = fileCsv.split('\n');
    const dataSeparated = dataGot.filter((items) => items !== '').map((item) => item.split(','));
    dataSeparated.shift();
    console.log(`Number of students: ${dataSeparated.length}`);
    const acum = {};
    const keys = Object.keys(dataSeparated);
    for (const student of dataSeparated) {
      console.log(student);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
