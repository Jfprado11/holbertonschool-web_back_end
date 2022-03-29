import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const val = Promise.all([uploadPhoto(), createUser()])
    .then((values) => values)
    .catch(() => {
      console.log('Signup system offline');
    });
  return val;
}
