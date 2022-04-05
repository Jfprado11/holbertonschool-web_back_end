export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  if (value > 127 || value < -128) {
    throw new Error('Position outside range');
  }
  const arrayTyped = new Int8Array(buffer);
  arrayTyped[position] = value;
  return arrayTyped;
}
