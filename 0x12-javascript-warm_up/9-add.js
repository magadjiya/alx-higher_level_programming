#!/usr/bin/node
const array = process.argv;

function add (a, b) {
  a = Number(a);
  b = Number(b);
  const result = a + b;
  console.log(result);
}

add(array[2], array[3]);
