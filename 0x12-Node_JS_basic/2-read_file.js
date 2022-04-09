const fs = require('fs');

function countStudents(path) {
  try {
    const fileCsv = fs.readFileSync(path, { encoding: 'utf8' });
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
