// import the NodeJS modules
const fs = require('fs');               // module for file I/O
const readline = require("readline");   // module for reading line-by-line from file

class Defect {
  constructor(bug_id, component, status, resolution, summary, blocks, depends, fixed_by_username, fixed_by_real_name) {
    this.bug_id = bug_id; // Number
    this.component = component; // String
    this.status = status; // String
    this.resolution = resolution; // String
    this.summary = summary; // String
    this.blocks = blocks; // Array of Numbers
    this.depends = depends; // Array of Numbers
    this.fixed_by_username = fixed_by_username; // String
    this.fixed_by_real_name = fixed_by_real_name; // String
  }
}

function loadObjects() {

  /* ... Your implementation here ... */
  // You can use the readFile from the fs module
  // See the documentation: https://nodejs.org/en/knowledge/file-system/how-to-read-files-in-nodejs/
  // The CSV files are comma-separated
  let defectsCSV = fs.readFileSync("test4/defects.csv", "utf8");
  let dependsCSV = fs.readFileSync("test4/defect_depends.csv", "utf8");
  let blocksCSV = fs.readFileSync("test4/defect_blocks.csv", "utf8");
  let developersCSV = fs.readFileSync("test4/developers.csv", "utf8");

  // go through defects and create a dict such that id can hash to it for later adn create the object with empty blocks, depends, and fixed_by_real_name fields
  let defects = {}
  defectsCSV.split("\n").splice(1).forEach(row => {
    let fields = row.split(",")
    defects[fields[0]] = new Defect(fields[0], fields[1], fields[2], fields[3], fields[4], [], [], fields[13], null)
  });

  // go through depends csv, use id to find list list to append to
  dependsCSV.split("\n").splice(1).forEach(row => {
    row = row.split(",")
    defects[row[0]].depends.push(row[1])
  })

  // do the same for blocks
  blocksCSV.split("\n").splice(1).forEach(row => {
    row = row.split(",")
    defects[row[0]].blocks.push(row[1])
  })

  // no need to find based on id, so just turn dict of defects into a list
  defects = Object.values(defects)
  let developers = {}

  //go through developer csv and map username to real name
  developersCSV.split("\n").splice(1).forEach(row => {
    row = row.split(",")
    developers[row[1]] = row[0]
  })

  // go through every defect and put name accoridng to username and if info missing/undefined in csv set it back to null
  for (let i = 0; i < defects.length; i++) {
    defects[i].fixed_by_real_name = developers[defects[i].fixed_by_username]
    if (defects[i].fixed_by_real_name === '' || defects[i].fixed_by_real_name === undefined) {
      defects[i].fixed_by_real_name = null
    }
  }

  // return the list of defect objects
  return defects;
}


function query1(defects) {
  /* Your implementation here */
  // filter for status = resolved and resolution = fixed and get length of the remainder
  return defects.filter((defect) => defect.status === "RESOLVED" && defect.resolution === "FIXED").length;
}

function query2(defects) {
  /* Your implementation here */
  // filter for summary lowercase has buildbot and get length of the remainder
  return defects.filter((defect) => defect.summary.toLowerCase().includes("buildbot")).length;
}

function query3(defects) {
  /* Your implementation here */
  // filter for reqs, divide by total and conver to a 2 decimal percentage value
  console.log(defects.filter((defect) => defect.status !== "RESOLVED").length)
  return Math.round(defects.filter((defect) => defect.status !== "RESOLVED").length / defects.length * 10000) / 100;
}

function query4(defects) {
  /* Your implementation here */
  // create a dict to store counts for each component name
  let counts = {}
  let res = null;
  let maxcount = 0
  // iterate through and add to component count each time, if its the biggest, set that as max
  for (const defect of defects) {
    let count = counts[defect.component] || 0;
    count++;
    counts[defect.component] = count;
    if (count > maxcount) {
      maxcount = count;
      res = defect.component;
    }
  }
  return res;
}

function query5(defects) {
  /* Your implementation here */
  //filter for only ones data we need
  const filtered_defects = defects.filter((defect) => defect.status === "RESOLVED" && defect.resolution === "FIXED" && defect.component === "Documentation");
  // create a dict to store counts for each username
  let counts = {}
  let res = null;
  let maxcount = 0
  // iterate through and add to component count each time, if its the biggest, set that as max
  // if its equal, only set it as max if alphabetically higher
  for (const defect of filtered_defects) {
    const username = defect.fixed_by_username;
    let count = counts[username] || 0;
    count++;
    counts[username] = count;
    if (count < maxcount) {
      continue
    }
    if (count === maxcount && res.localeCompare(username) > 0) {
      continue
    }
    maxcount = count;
    res = username;
  }
  return res;
}

function query6(defects) {
  // create a graph from the defects and their blocks
  let graph = new Map();
  defects.forEach((defect) => {
    graph.set(defect.bug_id, defect.blocks);
  });
  // create a cache so we know what we already checked
  let checked = new Set()
  //get a list of all the nodes to go through

  // dfs function to find cycle
  function dfs(n, visited) {
    // if its in checked, than we know its already safe
    if (checked.has(n)) {
      return false
    }
    // add current node to the visited set
    visited.add(n)
    for (const nex of graph.get(n)) {
      // if we already visited the nex object in this dfs run, its obvi a cycle so return true
      if (visited.has(nex)) {
        return true;
      }
      // if an element beyond this has a cycle than we have a cycle
      if (dfs(nex, visited)) {
        return true
      }
      // if theres no cycle past this point, we can delete this node from the visited set jsut in case another path leads to this even tho its not a cycle
      visited.delete(nex)
    }
    // since were sure that nothing past this has a cycle we can safely say that this node is safe from a cycle
    checked.add(n)
    return false

  }
  // iterate through every node to check for cycles
  for (const node of graph.keys()) {
    if (checked.has(node)) {
      continue;
    }
    let visited = new Set()
    if (dfs(node, visited)) return true;
  }
  return false;
}


let defects = loadObjects();
console.log(defects.length)
console.log(query1(defects));
console.log(query2(defects));
console.log(query3(defects));
console.log(query4(defects));
console.log(query5(defects));
console.log(query6(defects));


