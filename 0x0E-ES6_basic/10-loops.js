export default function appendToEachArrayValue(array, appendString) {
  for (const idx of array) {
    const value = idx;
    array.push(appendString + value);
  }

  return array;
}
