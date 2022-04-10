import readDatabase from '../utils';

export default class StudentsController {
  static async getAllStudents(request, response) {
    const arrayToSend = [];
    try {
      arrayToSend.push('This is the list of our students\n');
      const data = await readDatabase('database.csv');
      arrayToSend.push(`Number of students: ${data.numOfStudents}\n`);
      delete data.numOfStudents;
      const keysFinal = Object.keys(data);
      keysFinal.forEach((item, idx) => {
        if (idx === keysFinal.length - 1) {
          arrayToSend.push(`Number of students in ${item}: ${data[item].length}. List: ${data[item].join(', ')}`);
        } else {
          arrayToSend.push(`Number of students in ${item}: ${data[item].length}. List: ${data[item].join(', ')}\n`);
        }
      });
      response.status(200).send(arrayToSend.join(''));
    } catch (err) {
      // arrayToSend.push(err.message);
      response.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(request, response) {
    const param = request.params.major;
    if (param === 'CS' || param === 'SWE') {
      try {
        const data = await readDatabase('database.csv');
        const students = data[param];
        response.status(200).send(`List: ${students.join(', ')}`);
      } catch (err) {
        console.log(err);
        response.status(500).send('Cannot load the database');
      }
    } else {
      response.status(500).send('Major parameter must be CS or SWE');
    }
  }
}
