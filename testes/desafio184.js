function verticalDance(sprite) {
  if (!Array.isArray(sprite) || sprite.length === 0 || !sprite.every(row => Array.isArray(row) && row.length === sprite.length)) {
    throw new Error("Matriz inválida. Certifique-se de que seja uma matriz quadrada n x n.");
  }

  return sprite.slice().reverse().map(row => [...row]); 
}

// Matriz 3x3
console.log(verticalDance([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]));

// Matriz 2x2
console.log(verticalDance([
  [10, 20],
  [30, 40]
]));


// Matriz 4x4 (mais complexa)
console.log(verticalDance([
  [1, 0, 1, 0],
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [0, 0, 0, 0]
]));
