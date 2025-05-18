
function transformarEmFeiticos(codigos) {
  const mapaDeFeiticos = {
    1: "🔥",
    2: "❄️",
    3: "🩹",
    4: "👻",
    5: "🛡️"
  };

  return codigos.map(codigo => mapaDeFeiticos[codigo] || "").join(" ");
}

console.log(transformarEmFeiticos([1, 3, 4, 2, 5])); 
console.log(transformarEmFeiticos([2, 2, 5, 1]));    
