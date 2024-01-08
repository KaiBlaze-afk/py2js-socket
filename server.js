const net = require('net');

const server = net.createServer((socket) => {
  console.log('Client connected');

  // Handle incoming data from the client
  socket.on('data', (data) => {
    console.log(`Received from client: ${data}`);

    // Respond to the client
    socket.write(`Server received: ${data}, right?`);
  });

  // Handle client disconnection
  socket.on('end', () => {
    console.log('Client disconnected');
  });
});

const PORT = 3000;
server.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
