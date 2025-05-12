function solve(amount, bottles) {
  if (Math.max(...bottles) < amount) return null; //if amount is greater than any bottle its not possible
  if (amount === 0) return [new Array(bottles.length).fill(0)]; // if amount is 0, then starting = solution
  let visited = new Map() //created a visited set to track back
  visited.set(JSON.stringify(new Array(bottles.length).fill(0)), null); // add starting state to visited
  let q = [JSON.stringify(new Array(bottles.length).fill(0))]; // create the queue with a starting state
  // create bfs to search for solution
  function bfs() {
    while (q.length > 0) {
      let curr_str = q.shift();
      let curr = JSON.parse(curr_str);

      //check takes the current state, sees if any of the changed values = amount returns true if so, otherwise false
      function check(new_str, values) {
        if (!visited.has(new_str)) {
          visited.set(new_str, curr_str);
          q.push(new_str);
        }
        if (values.includes(amount)) return true;
        return false;
      }

      // make a new state by filling one jar every time
      for (let i = 0; i < curr.length; i++) {
        if (curr[i] === bottles[i]) continue;
        copy = [...curr];
        copy[i] = bottles[i];
        copy_str = JSON.stringify(copy);
        if (check(copy_str, [bottles[i]])) return copy_str;
      }

      // make a new state by emptying one jar every time
      for (let i = 0; i < curr.length; i++) {
        if (curr[i] === 0) continue;
        copy = [...curr];
        copy[i] = 0;
        copy_str = JSON.stringify(copy);
        if (check(copy_str, [0])) return copy_str;
      }
      // make a new state by pouring from one jar to another every time
      for (let i = 0; i < curr.length; i++) {
        for (let j = 0; j < curr.length; j++) {
          if (j === i) continue;

          // pour from a to b; we say b_limit is how much space left in b and we fill to the limit or until a runs out
          function pour_from_to(x, y) {
            let a = curr[x];
            let b = curr[y];
            let b_limit = bottles[y] - b;
            let pour = Math.min(a, b_limit);
            a -= pour;
            b += pour;
            if (a === curr[x] && b === curr[y]) return;
            let copy = [...curr];
            copy[x] = a;
            copy[y] = b;
            copy_str = JSON.stringify(copy);
            if (check(copy_str, [a, b])) return copy_str;
          }

          //if pour works, return that
          let copy = pour_from_to(i, j);
          if (copy) return copy;

          // same as above
          copy = pour_from_to(j, i);
          if (copy) copy;
        }
      }
    }
    // nothing worked
    return false;
  }
  let successState = bfs();
  // console.log(visited.size)
  // console.log(count)
  if (!successState) return null; //if nothing worked return null

  // trace back and create the list
  function createRes(curr) {
    let res = [];
    while (curr) {
      res.unshift(JSON.parse(curr));
      curr = visited.get(curr);
    }
    return res;
  }
  let res = createRes(successState);

  // Now zero every other jar
  for (let i = 0; i < bottles.length; i++) {
    let cur = res[res.length - 1];
    if (cur[i] === 0 || cur[i] === amount) continue;
    cur = [...cur];
    cur[i] = 0;
    res.push(cur);
  }

  //return final solution
  return res;
}
console.log("Answer:", solve(2, [5, 3]));
console.log("Answer:", solve(1, [2, 4]));
console.log("Answer:", solve(8, [10, 2, 1]));
console.log("Answer:", solve(8, [3, 4, 2, 1]));

// console.log("Answer:", solve(235, [800, 305, 462, 409, 480, 857, 146, 42, 987, 789, 205, 738, 819, 809, 979, 19, 567, 391, 617, 979, 837, 981, 462, 327, 821, 110, 322, 740, 436, 182, 338, 435, 139, 346, 124, 482, 733, 303, 16, 450, 177, 865, 898, 25, 819, 349, 389, 986, 132, 909, 693, 110, 121, 413, 37, 355, 927, 418, 205, 530, 708, 117, 57, 917, 302, 844, 178, 88, 307, 275, 973, 506, 903, 201, 153, 173, 292, 485, 153, 68, 924, 30, 211, 913, 999, 378, 28, 68, 531, 420, 72, 579, 536, 922, 258, 81, 459, 458, 548, 264]));

// console.log("Answer:", solve(6, new Array(15).fill(7)))
