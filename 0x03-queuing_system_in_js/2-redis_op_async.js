import { createClient, print } from "redis";
import { promisify } from "util";

const client = createClient();

client.on('error', (err) => {
    console.error('Redis client not connected to the server: ', err);
});
client.on('connect',() => {
    console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
    try {
        const reply = await getAsync(schoolName);
        console.log(reply);
    } catch (err) {
        console.error('Error:', err);
    }
}

// function displaySchoolValue(schoolName) {
//     client.get(schoolName, (err, reply) => {
//         if (err) {
//             console.error('Error:', err);
//         } else {
//             console.log(reply);
//         }
//     });
// }

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
