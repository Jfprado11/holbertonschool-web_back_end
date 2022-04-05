export default function hasValuesFromArray(setCheck, arrayCheck) {
  let hasObj = true;

  arrayCheck.forEach((element) => {
    const check = setCheck.has(element);
    if (!check) {
      hasObj = false;
    }
  });
  return hasObj;
}
