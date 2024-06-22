#!/usr/bin/node
let i;

for (i = 0; process.argv[i] !== undefined; i++);

if (i < 3) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
