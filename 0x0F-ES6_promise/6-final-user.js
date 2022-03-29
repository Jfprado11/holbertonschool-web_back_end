/* eslint-disable no-param-reassign */
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const allArray = Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]).then((values) => {
    values.forEach((elements) => {
      if (Object.keys(elements).includes('reason')) {
        Object.assign(elements, { value: elements.reason });
        delete elements.reason;
      }
    });
    return values;
  });
  return allArray;
}
