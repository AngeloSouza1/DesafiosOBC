function decifrarMensagemAlienigena(numeros) {
  return numeros.map(num => {
    if (num % 3 === 0 && num % 5 === 0) return "ZogBlip";
    if (num % 3 === 0) return "Zog";
    if (num % 5 === 0) return "Blip";
    return String(num);
  });
}


const mensagem = [10, 15, 3, 7];
const decifrada = decifrarMensagemAlienigena(mensagem);

console.log("🛸 Mensagem Decifrada:");
console.log(decifrada);
