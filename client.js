var terminal = new Terminal({
  cursorBlink: "block",
});

async function connect() {
  return new Promise(function (resolve, reject) {
    var server = new WebSocket("ws://localhost:7560");
    server.onopen = function () {
      resolve(server);
    };
    server.onerror = function (err) {
      reject(err);
    };
    server.onmessage = function (event) {
      terminal.write(event.data);
    };
  });
}
async function sendGreeting(message) {
  try {
    connect().then(function (server) {
      server.send(message);
    });
  } catch (error) {
    console.log("Obbobobb", error);
  }
}

document.getElementById("messageButton").addEventListener("click", (e) => {
  sendGreeting();
});

terminal.open(document.getElementById("terminal"));
let curr_line = "";
let entries = [];

terminal.onKey(function (key, ev) {
  // Enter
  if (key.key == "\r") {
    if (curr_line) {
      sendGreeting(curr_line);
      entries.push(curr_line);
      curr_line = "";
      terminal.write("\r\n");
      terminal.prompt();
    }
  } else {
    console.log(curr_line);
    curr_line += key.key;
    terminal.write(key.key);
  }
});

terminal.prompt = () => {
  if (curr_line) {
    let data = { method: "command", command: curr_line };
    server.send(JSON.stringify(data));
  }
};
terminal.prompt();

window.onload = function () {
  connect();
};
