export default function updateUniqueItems(mapCheck) {
  mapCheck.forEach((value, key) => {
    if (value === 1) {
      mapCheck.set(key, 100);
    }
  });
  return mapCheck;
}
