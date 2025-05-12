function enumerate(i, j) {
  // if upperbound non-positive, return correct amount of nulls in a list
  if (j <= 0) {
    return new Array(j - i + 1).fill(null);
  }
  // if lower bound non-postiive, start res as an array of the proper amount of nulls.
  let res = []
  if (i <= 0) {
    res = new Array(0 - i + 1).fill(null);
    i = 1
  }
  // Perform algorithm such that numerator and denominater add to sum
  // each sum happens sum-2/2 times and then u add 2 to sum and flip numerator inc/dec
  let sum = 4
  let sum_count = 1

  // iterate until k > j and only add to list if k >= i
  for (let k = 1; k <= j; k++) {
    if (k >= i) {
      if (sum % 4 == 2) {
        res.push((sum - 2 * sum_count) + '/' + (2 * sum_count))
      } else {
        res.push((2 * sum_count) + '/' + (sum - 2 * sum_count))
      }
    }
    if ((sum - 2) / 2 === sum_count) {
      sum += 2
      sum_count = 1
    } else {
      sum_count += 1
    }
  }
  return res
}

// console.log(enumerate(1, 2))
// console.log(enumerate(3, 6))
// console.log(enumerate(-1, 4))
// console.log(enumerate(-4, 0))
// console.log(enumerate(1, 1))
