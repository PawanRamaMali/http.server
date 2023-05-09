import http.server
import socketserver
import os

# Define the directory you want to share
shared_directory = "G:/file_path/"

# Change the working directory to the shared directory
os.chdir(shared_directory)

# Define the port you want to use for the server
port = 8000

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", port), handler)

print(f"Serving files from {shared_directory} on port {port}")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down the server.")
    httpd.shutdown()
    httpd.server_close()
