function organizaInventario(itens) {
  return itens
    .slice()                 
    .sort()                  
    .join('\n');             
}

const tesouros = [
  "Poções de Mana",
  "Espadas de Prata",
  "Escudos Retorcidos",
  "Poções de Vida",
  "Elmos Encantados"
];

console.log(organizaInventario(tesouros));
