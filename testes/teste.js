
function oneBitCode() {
    console.log("==============================================");
    console.log("| Número | Resultado  |");
    console.log("|--------|------------|");
    for (let i = 1; i <= 100; i++) {
        let output = "";
        
        if (i % 3 === 0 && i % 5 === 0) {
            output = "Code ⚡"; 
        } else if (i % 3 === 0) {
            output = "One 🔵";
        } else if (i % 5 === 0) {
            output = "Bit 🟢";
        } else {
            output = i.toString();
        }
        
        console.log(`|  ${i.toString().padStart(3, ' ')}   | ${output.padEnd(10, ' ')} |`);
    }
    console.log("==============================================");
}


console.log("Desafio OneBitCode!");
oneBitCode();
