#!/usr/bin/node
const len = process.argv.length;
const args = process.argv;

if (len === 2) {
  console.log('undefined is undefined');
} else if (len === 3) {
  console.log(`${args[2]} is undefined`);
} else {
  console.log(`${args[2]} is ${args[3]}`);
}
