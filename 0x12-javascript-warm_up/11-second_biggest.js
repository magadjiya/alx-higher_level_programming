#!/usr/bin/node
const array = process.argv.slice(2).map(Number);
const len = process.argv.length - 2;
let i;

if (len === 0 || len === 1) {
  console.log(0);
} else {
  let biggest = array[0];
  let secondBiggest = -Infinity;

  for (i = 0; i < len; i++) {
    if (array[i] > biggest) {
      biggest = array[i];
    }
  }

  for (i = 0; i < len; i++) {
    if (array[i] !== biggest) {
      if (array[i] > secondBiggest) {
        secondBiggest = array[i];
      }
    }
  }
  console.log(secondBiggest);
}
