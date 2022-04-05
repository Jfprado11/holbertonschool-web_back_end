export default function getStudentsByLocation(arrayObj, city) {
  return arrayObj.filter((item) => item.location === city);
}
