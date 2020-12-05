const fs = require("fs");

const input = fs.readFileSync("./input.txt", "utf8");
const lines = input.split("\n");

function calcHits(rightSteps, downSteps, lines) {
  treesHit = 0;
  rightPos = rightSteps;
  downPos = downSteps;

  while (downPos < lines.length) {
    if (lines[downPos][rightPos] === "#") {
      treesHit++;
    }

    downPos += downSteps;
    rightPos = (rightPos + rightSteps) % 31;
  }
  return treesHit;
}

console.log("Hit trees on the way down (1 right, 1 down): " + calcHits(1, 1, lines));
console.log("Hit trees on the way down (3 right, 1 down): " + calcHits(3, 1, lines));
console.log("Hit trees on the way down (5 right, 1 down): " + calcHits(5, 1, lines));
console.log("Hit trees on the way down (7 right, 1 down): " + calcHits(7, 1, lines));
console.log("Hit trees on the way down (1 right, 2 down): " + calcHits(1, 2, lines));
