import readDatabase from '../utils';

const db = process.argv[2];

export default class StudentsController {
  static async getAllStudents(request, response) {
    try {
      response.write('This is the list of our students\n');
      const data = await readDatabase(db);
      const keysFinal = Object.keys(data);
      keysFinal.sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
      keysFinal.forEach((item, idx) => {
        if (idx === keysFinal.length - 1) {
          response.write(`Number of students in ${item}: ${data[item].length}. List: ${data[item].join(', ')}`);
        } else {
          response.write(`Number of students in ${item}: ${data[item].length}. List: ${data[item].join(', ')}\n`);
        }
      });
      response.status(200).end();
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
        response.status(200).send(`List: ${students.join(', ')}`);
      } catch (err) {
        response.status(500).send('Cannot load the database');
      }
    } else {
      response.status(500).send('Major parameter must be CS or SWE');
    }
  }
}
