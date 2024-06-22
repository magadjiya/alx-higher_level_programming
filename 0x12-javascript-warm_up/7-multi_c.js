#!/usr/bin/node
const num = process.argv.length;

if (num > 2) {
  const toNum = Math.floor(process.argv[2]);
  if (isNaN(toNum) || toNum === undefined) {
    console.log('Missing number of occurences');
  } else {
    for (let i = 0; i < toNum; i++) {
      console.log('C is fun');
    }
  }
}
