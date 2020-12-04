import fs from "fs";

const input = fs.readFileSync("./input.txt", "utf8");
const lines = input.split("\n");

let validPasswords = 0;

for (let line of lines) {
  const minusIndex = line.indexOf("-");
  const firstSpaceIndex = line.indexOf(" ");
  const colonIndex = line.indexOf(":");

  const min = parseInt(line.substr(0));
  const max = parseInt(line.substr(minusIndex + 1, firstSpaceIndex));
  const char = line.charAt(colonIndex - 1);
  const pwd = line.substr(colonIndex + 1);

  if (isValid(min, max, char, pwd)) {
    validPasswords++;
  }
}

function isValid(min, max, char, pwd) {
  const amount = pwd.split(char).length - 1;
  return amount >= min && amount <= max;
}

console.log("valid passwords: ", validPasswords);
