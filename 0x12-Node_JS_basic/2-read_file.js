const fs = require('fs');

function countStudents(path) {
  try {
    const fileCsv = fs.readFileSync(path, { encoding: 'utf8' });
    const dataGot = fileCsv.split('\n');
    const dataSeparated = dataGot.filter((items) => items !== '').map((item) => item.split(','));
    dataSeparated.shift();
    console.log(`Number of students: ${dataSeparated.length}`);
    const acum = {};
    for (const student of dataSeparated) {
      const keys = Object.keys(acum);
      if (keys.includes(student[3])) {
        acum[student[3]].push(student[0]);
      } else {
        acum[student[3]] = [student[0]];
      }
    }
    const keysFinal = Object.keys(acum);
    keysFinal.forEach((item) => {
      console.log(`Number of students in ${item}: ${acum[item].length}. List: ${acum[item].join(', ')}`);
    });
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
