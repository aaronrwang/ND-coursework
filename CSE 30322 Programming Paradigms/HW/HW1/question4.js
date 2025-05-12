function reversedSum(num1, num2) {

  // turn whatever data type it is to string and reverse it and then back to num
  num1 = Number(reversestr(num1.toString()))
  num2 = Number(reversestr(num2.toString()))

  // add them
  let res = num1 + num2
  // turn number to string, reverse, and back to number
  return Number(reversestr(res.toString()))
}

function reversestr(num) {
  //iterate backwards and add it to new string
  let newNum = ''
  for (let i = num.length - 1; i >= 0; i--) {
    newNum += num[i];
  }
  return newNum
}

// console.log(reversedSum("24", 1))
// console.log(reversedSum(4358, "754"))
// console.log(reversedSum(305, 794))