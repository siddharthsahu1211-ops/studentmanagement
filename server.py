from http.server import HTTPServer
from router import StudentRouter

def run_server(HOST: str = "localhost", PORT: int = 8000):
    server = HTTPServer((HOST, PORT), StudentRouter)
    print(f"🚀 Server running at http://{HOST}:{PORT}")
    server.serve_forever()
if __name__ == "__main__":
    run_server()