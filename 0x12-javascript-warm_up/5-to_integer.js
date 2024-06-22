#!/usr/bin/node
const len = process.argv.length;
const toNum = Math.floor(process.argv[2]);

if (len === 2 || isNaN(toNum)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${toNum}`);
}
