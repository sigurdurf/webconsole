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
async function sendGreeting() {
  try {
    connect().then(function (server) {
      var greeting = document.getElementById("messageBox").value;
      server.send(greeting);
    });
  } catch (error) {
    console.log("Obbobobb", error);
  }
}
document.getElementById("messageButton").addEventListener("click", (e) => {
  sendGreeting();
});

var terminal = new Terminal();
terminal.open(document.getElementById("terminal"));
terminal.prompt();
