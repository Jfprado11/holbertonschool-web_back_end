import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const val = Promise.all([uploadPhoto(), createUser()])
    .then((values) => values)
    .catch(() => {
      console.log('Signup system offline');
    });
  val.then((values) => {
    console.log(values[0].body, values[1].firstName, values[1].lastName);
  });
}
