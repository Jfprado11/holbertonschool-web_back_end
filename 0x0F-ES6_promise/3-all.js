import { uploadPhoto, createUser } from './utils';

export default async function handleProfileSignup() {
  let val = null;
  try {
    val = await Promise.all([uploadPhoto(), createUser()]);
    console.log(val[0].body, val[1].firstName, val[1].lastName);
  } catch (err) {
    console.log('Signup system offline');
  }
  return val;
}
