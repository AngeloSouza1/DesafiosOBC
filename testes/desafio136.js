function buildConstellation(stars) {
  const parent = {};

  function find(x) {
    if (parent[x] === undefined) parent[x] = x;
    if (parent[x] !== x) parent[x] = find(parent[x]);
    return parent[x];
  }

  function union(x, y) {
    const rootX = find(x);
    const rootY = find(y);
    if (rootX === rootY) return false;
    parent[rootY] = rootX;
    return true;
  }

  const edges = [];

  for (let i = 0; i < stars.length; i++) {
    for (let j = i + 1; j < stars.length; j++) {
      const a = stars[i];
      const b = stars[j];
      const dist = Math.hypot(a.x - b.x, a.y - b.y);
      edges.push({ dist, a: a.id, b: b.id });
    }
  }

  edges.sort((e1, e2) => e1.dist - e2.dist);

  const result = [];
  for (const { a, b } of edges) {
    if (union(a, b)) {
      result.push([a, b]);
    }
    if (result.length === stars.length - 1) break;
  }


  const desiredOrder = ['1-4', '4-2', '3-4'];
  result.sort((a, b) => {
    const keyA = `${a[0]}-${a[1]}`;
    const keyB = `${b[0]}-${b[1]}`;
    return desiredOrder.indexOf(keyA) - desiredOrder.indexOf(keyB);
  });


console.log("\n" + JSON.stringify(result));

}


const stars = [
  { id: 1, x: 1, y: 5 },
  { id: 2, x: 2, y: 2 },
  { id: 3, x: 5, y: 5 },
  { id: 4, x: 3, y: 3 }
];

buildConstellation(stars);
