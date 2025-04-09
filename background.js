let currentPokemon = {
  id: 19,
  name: "rattata",
  imageUrl: "https://img.pokemondb.net/sprites/x-y/normal/rattata.png",
  level: 1
};

chrome.runtime.onConnect.addListener(function(port) {
    if (port.name !== "TEAM_ROCKET") return;
    console.log("Connected to popup via port");
    port.postMessage({starterPokemon: currentPokemon});
    port.onMessage.addListener(function(msg) {
      if (msg.request === "SEND_INITIAL_POKEMON") {
        port.postMessage({ question: "Who's there?" });
        // port.postMessage({ newUser: checkNewUser() });
      } else if (msg.answer === "Madame") {
        port.postMessage({ question: "Madame who?" });
      } else if (msg.answer === "Madame... Bovary") {
        port.postMessage({ done: "😂 Good one!" });
      }
      else if (msg.request === "SEND_POKEMON") {

        console.log("Send new pokemon request......."); 
        getRandomPokemon()
          .then(pokemon => {
            currentPokemon = pokemon;
            port.postMessage({ pokemonFound: currentPokemon });
          })
          .catch(error => {
            console.error("Error getting random Pokémon:", error);
            // Optional: send error message back to popup
          });
      }
    });
  
    port.onDisconnect.addListener(() => {
      console.log("Port disconnected.");
    });
  });
  
async function getRandomPokemon() {
  
  try {
    const backendRes = await fetch("http://localhost:8000/pokemon");
    const backendData = await backendRes.json();
    console.log("Backend says:", backendData);
    return {
      id: backendData.ID,
      name: backendData.Name,
      imageUrl: backendData.Picture,
      level: Math.ceil(Math.random() * 20)
    };
  } catch (err) {
    console.warn("Backend not reachable:", err.message);
  }
}