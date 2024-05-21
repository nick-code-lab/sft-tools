const readline = require('readline');
const fs = require('fs');

const inputFilePath = 'ds_data.jsonl'; // Replace with your input JSONL file
const outputFilePath = 'ds_data.json'; // Replace with the desired output JSON file

const jsonArray = [];

const rl = readline.createInterface({
  input: fs.createReadStream(inputFilePath),
  crlfDelay: Infinity
});

rl.on('line', (line) => {
  const jsonObject = JSON.parse(line);
  jsonArray.push(jsonObject);
});

rl.on('close', () => {
  fs.writeFileSync(outputFilePath, JSON.stringify(jsonArray, null, 2));
  console.log('JSON array file has been created successfully.');
});