const fs = require('fs');

function countStudents(path) {
  try {
    const fileCsv = fs.readFileSync(path, { encoding: 'utf8' });
    const dataGot = fileCsv.split('\n');
    console.log(dataGot);
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
