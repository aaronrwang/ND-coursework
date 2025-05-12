function findUserById(users, id) {
  return users.filter((user) => user.id === id).map((user) => user.name)[0] || null;
}


function computeBMIs(users) {
  return users.map((user) => user.weight / (user.height * user.height));
}


let users = [
  { id: 1, name: "Marta", height: 1.74, weight: 59 },
  { id: 2, name: "Josh", height: 1.80, weight: 88 },
  { id: 3, name: "Achilles", height: 1.68, weight: 63 },
  { id: 4, name: "Julius", height: 1.93, weight: 97 },
];

console.log(findUserById(users, 0))
console.log(computeBMIs(users))
