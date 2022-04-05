export default function getListStudentIds(arrayObj) {
  if (!Array.isArray(arrayObj)) {
    return [];
  }
  const newId = arrayObj.map((item) => item.id);
  return newId;
}
