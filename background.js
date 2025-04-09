let currentPokemon = {
    id: 19,
    name: "rattata",
    imageUrl: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/19.png",
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
        // const pokemonId = () => {
        //   const pool = getAvailablePokemonIds();
        //   const index = Math.floor(Math.random() * pool.length);
        //   return pool[index];
        // };
        
        // console.log("Random (safe) Pokémon ID:", pokemonId());
        // console.log("BACKEND ENDPOINT!!!!!!!!!!!!!!!!!!!!!!!");
        // fetch("http://localhost:8000/pokemon")
        // .then(response => response.json())
        // .then(result => {
        //   console.log(result);
        // });
        // fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonId()}`)
        // .then(response => response.json())
        // .then(json => {
        //   currentPokemon = {
        //     id: json.id,
        //     name: json.forms[0].name,
        //     imageUrl: json.sprites.front_default,
        //     level: Math.ceil(Math.random() * 20)
        //   };
        //   console.log(currentPokemon);
        //   port.postMessage({ pokemonFound: currentPokemon });
        // });
      }
    });
  
    port.onDisconnect.addListener(() => {
      console.log("Port disconnected.");
    });
  });
  
async function getRandomPokemon() {
  const pool = getAvailablePokemonIds();
  const index = Math.floor(Math.random() * pool.length);
  const id = pool[index];

  console.log("Random (safe) Pokémon ID:", id);

  // Optionally: test your FastAPI backend
  try {
    const backendRes = await fetch("http://localhost:8000/pokemon");
    const backendData = await backendRes.json();
    console.log("Backend says:", backendData);
  } catch (err) {
    console.warn("Backend not reachable:", err.message);
  }

  // Now get from pokeapi
  try {
    const res = await fetch(`https://pokeapi.co/api/v2/pokemon/${id}`);
    const json = await res.json();

    return {
      id: json.id,
      name: json.forms[0].name,
      imageUrl: json.sprites.front_default,
      level: Math.ceil(Math.random() * 20)
    };
  } catch (error) {
    console.error("Error fetching Pokémon from PokeAPI:", error);
    throw error; // propagate error if needed
  }
}
// List of Pokémon IDs to exclude
  // Starter lines
  //   1, 2, 3,      // Bulbasaur → Venusaur
  //   4, 5, 6,      // Charmander → Charizard
  //   7, 8, 9,      // Squirtle → Blastoise
  //   152,          // Not in Gen 1 but safe check

  // Pikachu line
  //   25, 26,       // Pikachu, Raichu

  // Special/Legendary
  //   144, 145, 146, // Articuno, Zapdos, Moltres
  //   149, 150, 151,      // Dragonite, Mewtwo, Mew
function getAvailablePokemonIds() {
  const excludedIds = [1,2,3,4,5,6,7,8,9,152,25,26,144,145,146,149,150,151];
  const allIds = [];
  for (let i = 1; i <= 151; i++) {
    if (!excludedIds.includes(i)) {
      allIds.push(i);
    }
  }

  return allIds;
}