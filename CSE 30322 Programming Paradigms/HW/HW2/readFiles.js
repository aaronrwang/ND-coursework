// import the NodeJS modules
const fs = require('fs');               // module for file I/O
const readline = require("readline");   // module for reading line-by-line from file


class Defect {
  constructor(bug_id, component, status, resolution, summary, fixed_by_username) {
    this.bug_id = bug_id; // Number
    this.component = component; // String
    this.status = status; // String
    this.resolution = resolution; // String
    this.summary = summary; // String
    this.blocks = []; // Array of Numbers
    this.depends = []; // Array of Numbers
    this.fixed_by_username = fixed_by_username; // String
    this.fixed_by_real_name = undefined; // String
  }
}
// create input streams
let defectsCSV = fs.readFileSync("defects.csv", "utf8");
let dependsCSV = fs.readFileSync("defect_depends.csv", "utf8");
let blocksCSV = fs.readFileSync("defect_blocks.csv", "utf8");
let developersCSV = fs.readFileSync("developers.csv", "utf8");

// Reads defects CSV line-by-line
let defects = []
// console.log(defectsCSV.split("\n")[0])
defectsCSV.split("\n").slice(1).forEach(row => {
  let fields = row.split(",")
  let defect = new Defect(fields[0], fields[1], fields[2], fields[3], fields[4], fields[13])
  defects.push(defect)
});
console.log(defects)

dependsCSV.split("\n").forEach(row => {
  let [from, to] = row.split(",")
  console.log(from, to)
});

blocksCSV.split("\n").forEach(row => {
  /* Your logic here to parse the rows */
});

developersCSV.split("\n").forEach(row => {
  /* Your logic here to parse the rows */
});