import fs from "fs";

const input = fs.readFileSync("./input.txt", "utf8");
const lines = input.split("\n");

let validPasswordsFirstTest = 0;
let validPasswordsSecondTest = 0;

for (let line of lines) {
  const minusIndex = line.indexOf("-");
  const firstSpaceIndex = line.indexOf(" ");
  const colonIndex = line.indexOf(":");

  const min = parseInt(line.substr(0));
  const max = parseInt(line.substr(minusIndex + 1, firstSpaceIndex));
  const char = line.charAt(colonIndex - 1);
  const pwd = line.substr(colonIndex + 1);

  if (isValid(min, max, char, pwd)) {
    validPasswordsFirstTest++
  }

  if (isValidToboggan(min, max, char, pwd)) {
    validPasswordsSecondTest++;
  }
}

function isValid(min, max, char, pwd) {
  const amount = pwd.split(char).length - 1;
  return amount >= min && amount <= max;
}

function isValidToboggan(firstPos, secondPos, char, pwd) {
  const isInFirst = isCharAtIndex(char, firstPos, pwd);
  const isInSecond = isCharAtIndex(char, secondPos, pwd);
  const xor = !!(isInFirst ^ isInSecond);
  return xor;
}

function isCharAtIndex(char, index, text) {
  if (index >= text.length) {
    return false;
  }

  return char === text.charAt(index);
}

console.log("Valid passwords for first test: ", validPasswordsFirstTest);
console.log("Valid passwords for second test: ", validPasswordsSecondTest);
