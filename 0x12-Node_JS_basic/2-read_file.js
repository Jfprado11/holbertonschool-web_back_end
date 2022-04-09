const fs = require('fs');

function countStudents(path) {
  try {
    const fileCsv = fs.readFileSync(path);
    const data = fileCsv.toString().split('\n');
    const dataSeparated = data.filter((items) => items !== '').map((item) => item.split(','));
    dataSeparated.shift();
    console.log(`Number of students: ${dataSeparated.length}`);
    const finalData = dataSeparated.reduce((acum, student) => {
      if (Object.keys(acum).includes(student[3])) {
        acum[student[3]].push(student[0]);
      } else {
        return { ...acum, [student[3]]: [student[0]] };
      }
      return acum;
    }, {});
    Object.keys(finalData).forEach((item) => {
      console.log(`Number of students in ${item}: ${finalData[item].length}. List: ${finalData[item].join(', ')}`);
    });
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
