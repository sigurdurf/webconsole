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
      console.log(event.data);
    };
  });
}
async function sendGreeting() {
  try {
    connect().then(function (server) {
      var greeting = "Hello from javascript land";
      server.send(greeting);
    });
  } catch (error) {
    console.log("Obbobobb", error);
  }
}

sendGreeting();
