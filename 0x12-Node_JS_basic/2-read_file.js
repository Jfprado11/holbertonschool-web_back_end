const fs = require('fs');

function countStudents(path) {
  try {
    const fileCsv = fs.readFileSync(path, { encoding: 'utf8' });
    const dataGot = fileCsv.split('\n');
    const dataSeparated = dataGot
      .filter((items) => items !== '')
      .map((item) => item.split(','))
      .shift();
    console.log(`Number of students: ${dataSeparated.length}`);
    const acum = {};
    for (const student in dataSeparated) {
      if (Object.keys(dataSeparated).includes(student[3])) {
        acum[student[3]].push(student[0]);
      } else {
        return { ...acum, [student[3]]: [student[0]] };
      }
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
