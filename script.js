function checkLyrics() {
    const word = document.getElementById("text").textContent;
    console.log(word);
    const pattern = /\[Verse \d+\].+/;
    const matches = word.match(new RegExp(pattern, "g")) || [];
    console.log(matches);
    const div = document.createElement("div");
    const h2 = document.createElement("h2");
    h2.textContent = "Verses Found in the text";
    div.appendChild(h2);
    for (let i = 0; i < matches.length; i++) {
      const p = document.createElement("p");
      p.setAttribute("class", "result");
      p.textContent = matches[i];
      div.appendChild(p);
      document.body.appendChild(div);
    }
  }
  
  function checkJokes() {
    const word = document.getElementById("text").textContent;
    console.log(word);
    const pattern = /(Why did .+\?)\s(Because .+)/;
    const matches = word.match(new RegExp(pattern, "g")) || [];
    console.log(matches);
    const div = document.createElement("div");
    const h2 = document.createElement("h2");
    h2.textContent = "Jokes Found in the text";
    div.appendChild(h2);
    for (let i = 0; i < matches.length; i++) {
      const p = document.createElement("p");
      p.setAttribute("class", "result");
      p.textContent = matches[i];
      div.appendChild(p);
      document.body.appendChild(div);
    }
  }
  
  function checkEpisodes() {
    const word = document.getElementById("text").textContent;
    console.log(word);
    const pattern = /(.)+(S\d{2})(E\d{2}):[ ]?(.)+/;
    const matches = word.match(new RegExp(pattern, "g")) || [];
    console.log(matches);
    const div = document.createElement("div");
    const h2 = document.createElement("h2");
    h2.textContent = "Episodes Found in the text";
    div.appendChild(h2);
    for (let i = 0; i < matches.length; i++) {
      const p = document.createElement("p");
      p.setAttribute("class", "result");
      p.textContent = matches[i];
      div.appendChild(p);
      document.body.appendChild(div);
    }
  }