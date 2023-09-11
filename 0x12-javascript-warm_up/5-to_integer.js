#!/usr/bin/node
if (!(isNaN(process.argv[2]))) {
  console.log(process.argv[2] | 0);
} else {
  console.log('Not a number');
}
