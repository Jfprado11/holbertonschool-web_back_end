export default function updateStudentGradeByCity(arrayObj, city, newGrades) {
  const newArray = arrayObj
    .filter((item) => item.location === city)
    .map((item) => {
      let data;
      newGrades.forEach((element) => {
        if (element.studentId === item.id) {
          data = { ...item, grade: element.grade };
        }
      });
      if (!data) {
        return { ...item, grade: 'N/A' };
      }
      return data;
    });
  return newArray;
}
