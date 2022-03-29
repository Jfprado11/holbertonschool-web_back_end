export default function handleResponseFromAPI(promise) {
  const isResolved = promise
    .then(() => ({ status: 200, body: 'success' }))
    .catch(() => new Error(''));
  console.log('Got a response from the API');
  return isResolved;
}
