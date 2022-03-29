import { uploadPhoto, createUser } from './utils';

export default async function handleProfileSignup() {
  const val = await Promise.all([uploadPhoto(), createUser()]);
  console.log(val[0].body, val[1].firstName, val[1].lastName);
}
