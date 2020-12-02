import { input } from "./input.mjs";

function findTwo() {
  console.log("Find two pairs of numbers where the sum is 2020");
  for (let firstNum of input) {
    for (let secondNum of input) {
      if (firstNum + secondNum == 2020) {
        console.log(` ${firstNum} + ${secondNum} = 2020`);
        console.log(` ${firstNum} * ${secondNum} = ${firstNum * secondNum}`);
        return;
      }
    }
  }
}

function findThree() {
  console.log("Find three pairs of numbers where the sum is 2020");
  for (let firstNum of input) {
    for (let secondNum of input) {
      for (let thirdNum of input) {
        if (firstNum + secondNum + thirdNum == 2020) {
          console.log(` ${firstNum} + ${secondNum} + ${thirdNum} = 2020`);
          console.log(
            ` ${firstNum} * ${secondNum} * ${thirdNum} = ${
              firstNum * secondNum * thirdNum
            }`
          );
          return;
        }
      }
    }
  }
}

findTwo();
findThree();
