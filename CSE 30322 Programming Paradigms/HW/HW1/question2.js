function find(nums) {
  let maxx = 0
  let curr = 0
  //iterate through list and if current number is 33 or some equivalent, increase count, else set to 0
  // maxx is the maximum of curr or what it was before
  for (const num of nums) {
    if (num === 33) {
      curr += 1
    } else {
      curr = 0
    }
    maxx = Math.max(curr, maxx);
  }
  return maxx
}

// console.log(find([33, 33, 30, 33, 33, 33]))
// console.log(find([33, 0, 33, 33, 0, 33]))
// console.log(find([33, -10, 33, 33, 8, 3, 33, 33, 9, 33, 33, 33, 33, 33, 33]))
// console.log(find([33, 33, 5, 33, 33, 33]))
// console.log(find([33, 33, 30, 33, 33, 33.0]))
// console.log(find([null, "house", 9, undefined, "33"]))