export default function appendToEachArrayValue(array, appendString) {
  for (const idx of array) {
    const value = array[idx];
    array[array] = appendString + value;
  }

  return array;
}
