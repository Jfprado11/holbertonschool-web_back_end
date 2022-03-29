export default function handleResponseFromAPI(promise) {
  let isResolved = null;
  promise
    .then(() => {
      console.log('Got a response from the API');
      isResolved = { status: 200, body: 'success' };
    })
    .catch(() => {
      console.log('Got a response from the API');
      isResolved = new Error();
    });
  return isResolved;
}
