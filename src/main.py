import sys
import signal
import pyuv
import os
import stat

def on_http_request(server, error):
    client = pyuv.TCP(server.loop)
    server.accept(client)
    clients.append(client)

    fd = pyuv.fs.open(server.loop, path, os.O_RDONLY, stat.S_IFREG)

    length = 1000
    offset = 0
    read_data = pyuv.fs.read(server.loop, fd, length, offset)

    data = read_data.decode('utf-8')

    response = (
        "HTTP/1.1 200\n" +
        "status: 200\n" +
        "Content-Type: text/plain\n"
        "Content-Length: {}\n".format(len(data)) +
        "\n"+
        data
    )

    response_data = response.encode('utf-8')

    client.write(response_data)
    client.close()
    clients.remove(client)

def signal_cb(handle, signum):
    [c.close() for c in clients]
    signal_h.close()
    server.close()

# Variable declaration
clients = []
signal_h = None
server = None
path = None
loop = None

def main(argv):
    global signal_h, server, path

    print("Server run at port {} and returning file path {}".format(argv[0], argv[1]))

    path = argv[1]

    loop = pyuv.Loop.default_loop()

    server = pyuv.TCP(loop)
    server.bind(("0.0.0.0", int(argv[0])))
    server.listen(on_http_request)

    signal_h = pyuv.Signal(loop)
    signal_h.start(signal_cb, signal.SIGINT)

    loop.run()
    print("Stopped!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <port-number> <file-location>")
        exit()

    main(sys.argv[1:])
