export default function getStudentIdsSum(arrayObj) {
  const sum = arrayObj.reduce((acum, value) => acum + value.id, 0);
  return sum;
}
