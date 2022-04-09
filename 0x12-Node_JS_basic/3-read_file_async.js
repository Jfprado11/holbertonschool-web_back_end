const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, { encoding: 'utf8' }, (err, data) => {
      if (err) {
        return reject(new Error('Cannot load the database'));
      }
      const dataGot = data.split('\n');
      const dataSeparated = dataGot.filter((items) => items !== '').map((item) => item.split(','));
      dataSeparated.shift();
      console.log(`Number of students: ${dataSeparated.length}`);
      const finalData = dataSeparated.reduce((acum, student) => {
        const keys = Object.keys(acum);
        if (keys.includes(student[3])) {
          acum[student[3]].push(student[0]);
        } else {
          return { ...acum, [student[3]]: [student[0]] };
        }
        return acum;
      }, {});
      const finalKeys = Object.keys(finalData);
      finalKeys.forEach((item) => {
        console.log(`Number of students in ${item}: ${finalData[item].length}. List: ${finalData[item].join(', ')}`);
      });
      return resolve(finalData);
    });
  });
}

module.exports = countStudents;
