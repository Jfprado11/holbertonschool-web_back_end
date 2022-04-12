import readDatabase from '../utils';

const db = process.argv[2];

export default class StudentsController {
  static async getAllStudents(request, response) {
    const arrayToSend = [];
    try {
      arrayToSend.push('This is the list of our students\n');
      const data = await readDatabase(db);
      delete data.numOfStudents;
      const keysFinal = Object.keys(data);
      keysFinal.sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
      keysFinal.forEach((item, idx) => {
        if (idx === keysFinal.length - 1) {
          arrayToSend.push(`Number of students in ${item}: ${data[item].length}. List: ${data[item].join(', ')}`);
        } else {
          arrayToSend.push(`Number of students in ${item}: ${data[item].length}. List: ${data[item].join(', ')}\n`);
        }
      });
      response.status(200).send(arrayToSend.join(''));
    } catch (err) {
      response.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(request, response) {
    const param = request.params.major;
    if (param === 'CS' || param === 'SWE') {
      try {
        const data = await readDatabase(db);
        const students = data[param];
        const stringToSend = students.join(', ');
        response.status(200).send(`List: ${stringToSend}`);
      } catch (err) {
        response.status(500).send('Cannot load the database');
      }
    } else {
      response.status(500).send('Major parameter must be CS or SWE');
    }
  }
}
