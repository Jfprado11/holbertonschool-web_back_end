export default function handleResponseFromAPI(promise) {
  let isResolved = null;
  promise
    .then(() => {
      isResolved = { status: 200, body: 'success' };
    })
    .catch(() => {
      isResolved = new Error('');
    });
  console.log('Got a response from the API');
  return isResolved;
}
