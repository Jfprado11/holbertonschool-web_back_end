const fs = require('fs');

function countStudents(path) {
  try {
    const fileCsv = fs.readFileSync(path);
    return fileCsv;
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
