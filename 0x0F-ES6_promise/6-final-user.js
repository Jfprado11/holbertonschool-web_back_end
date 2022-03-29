import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const allArray = Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]).then((values) => {
    const array = values.map((elements) => {
      const obj = { status: elements.status };
      if (Object.keys(elements).includes('reason')) {
        Object.assign(obj, { value: elements.reason });
      } else {
        Object.assign(obj, { value: elements.value });
      }
      return obj;
    });
    return array;
  });
  return allArray;
}
