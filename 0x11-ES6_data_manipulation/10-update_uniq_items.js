export default function updateUniqueItems(mapCheck) {
  if (mapCheck instanceof Map === false) {
    throw new Error('Cannot process');
  }
  mapCheck.forEach((value, key) => {
    if (value === 1) {
      mapCheck.set(key, 100);
    }
  });
  return mapCheck;
}
