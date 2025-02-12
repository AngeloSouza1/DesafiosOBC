// Função para ajustar a playlist do DJ Robô
function ajustarPlaylist(playlist) {
    return playlist.filter(musica => musica.toLowerCase() !== 'barulho');
}

// Exemplo de uso
const playlistOriginal = [
    'Bohemian Rhapsody',
    'barulho',
    'Space Oddity',
    'barulho',
    'Hey Jude',
    'Superstition'
];

const playlistAjustada = ajustarPlaylist(playlistOriginal);

console.log("\uD83C\uDFB6✨ Ajuste a Playlist do DJ Robô! ✨\uD83C\uDFB6\n");
console.log("==============================================");
console.log("🎵 Playlist Original:");
console.log(`   🎧 ${playlistOriginal.join(', ')}`);
console.log("----------------------------------------------");
console.log("🎶 Playlist Ajustada:");
console.log(`   🚀 ${playlistAjustada.join(', ')}`);
console.log("==============================================\n");
console.log("🌌 Pronto para animar a balada intergaláctica! 🚀🥳");
