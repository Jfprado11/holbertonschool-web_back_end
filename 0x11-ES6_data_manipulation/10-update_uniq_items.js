export default function updateUniqueItems(mapCheck) {
  mapCheck.forEach((value, key) => {
    if (value === 1) {
      try {
        mapCheck.set(key, 100);
      } catch (err) {
        throw new Error('Cannot process');
      }
    }
  });
  return mapCheck;
}
