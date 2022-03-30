import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(
  firstName,
  lastName,
  fileName,
) {
  const sign = signUpUser(firstName, lastName);
  let photo = null;
  try {
    photo = await uploadPhoto(fileName);
  } catch (err) {
    photo = err.toSring();
  }
  return [
    { value: sign, status: 'fulfilled' },
    { value: photo, status: 'rejected' },
  ];
}
