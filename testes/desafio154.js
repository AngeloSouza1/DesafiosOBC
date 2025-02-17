function findGalacticTreasure(planets) {
    const recursosNecessarios = ["stardust", "quantum foam", "dark matter"];
  
    for (const planeta of planets) {
      const possuiTodosRecursos = recursosNecessarios.every(recurso =>
        planeta.resources.includes(recurso)
      );
  
      if (possuiTodosRecursos) {
        return planeta.name;
      }
    }
  
    return "Nenhum planeta contém todos os recursos necessários.";
  }
  


  const planets = [
    { name: "Alpha-7", resources: ["stardust", "quantum foam"] },
    { name: "Zeta-5", resources: ["stardust", "quantum foam", "dark matter"] },
    { name: "Omega-3", resources: ["dark matter"] }
  ];
  
  console.log(findGalacticTreasure(planets)); // ➜ "Zeta-5"
  