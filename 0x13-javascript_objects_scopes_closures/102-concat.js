#!/usr/bin/node
let fs = require('fs');
let data;
fs.readFile(process.argv[2], 'utf8', function(error, data1){
	fs.writeFile(process.argv[4], data1, 'utf8', (err) => {
		if (err) {
		  console.error('Error writing to fileC:', err);
		  return;
		}})
})
fs.readFile(process.argv[3], 'utf8', function(error, data1){
	fs.appendFile(process.argv[4], data1, 'utf8', (err) => {
		if (err) {
		  console.error('Error writing to fileC:', err);
		  return;
		}})
})


