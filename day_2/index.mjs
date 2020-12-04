import fs from "fs";

const input = fs.readFileSync("./input.txt", "utf8");
const lines = input.split("\n");

let validPasswordsFirstTest = 0;
let validPasswordsSecondTest = 0;

const pattern = "([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)";
const re = new RegExp(pattern);

for (let line of lines) {
  const match = re.exec(line);
  const min = parseInt(match[1]);
  const max = parseInt(match[2]);
  const char = match[3];
  const pwd = match[4];

  if (isValid(min, max, char, pwd)) {
    validPasswordsFirstTest++;
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
  const isInFirst = isCharAtIndex(char, firstPos - 1, pwd);
  const isInSecond = isCharAtIndex(char, secondPos - 1, pwd);
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
