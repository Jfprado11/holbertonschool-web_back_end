import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('error', (err) =>
  console.log(`Redis client not connected to the server: ${err}`),
);
client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  const getAsync = promisify(client.get).bind(client);
  const res = await getAsync(schoolName);
  console.log(res);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
