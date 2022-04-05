export default function cleanSet(set, startString) {
  const array = [];
  if (startString.length === 0) return '';
  set.forEach((element) => {
    if (element.startsWith(startString)) {
      array.push(element.slice(startString.length));
    }
  });
  return array.join('-');
}
