# Matches incoming HTTP paths (URLs) to handlers (like a tiny Express/Django router)

from datetime import datetime
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse

from controllers.students import (
    get_all_students
    , get_student
    , create_student
    , update_student
    , delete_student
)
from core.static import serve_static
from core.responses import send_404
from core.middleware import add_cors_headers

FRONTEND_ROUTES = {"/", "/home", "/students", "/docs"}
def handle_ui_routes(handler, path):
    if path in FRONTEND_ROUTES:
        serve_static(handler, "frontend/pages/index.html")
        return True

    if path.endswith(".html"):
        stripped = path.replace(".html", "")
        if stripped in FRONTEND_ROUTES:
            serve_static(handler, "frontend/pages/index.html")
            return True

    if path.startswith("/frontend/"):
        serve_static(handler, path.lstrip("/"))
        return True

    # if path == "/openapi.yaml":       ``
    #     serve_static(handler, "openapi.yaml")
    #     return True

    return False

class StudentRouter(BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        # Why OPTIONS exists:
        # Browsers enforce security rules.
        # Before a POST/PUT/DELETE request, browsers send a test request: OPTIONS.
        # Server must respond with CORS headers.
        # Without it, frontend fetch() will fail, even if your backend works.
        self.send_response(200)
        add_cors_headers(self)
        self.end_headers()

    def do_GET(self):
        path = urlparse(self.path).path

        # Handle frontend routes
        if handle_ui_routes(self, path):
            return

        # API: List students
        if path == "/api/students":
            return get_all_students(self)

        #  API: Get student by ID
        if path.startswith("/api/students/"):
             student_id = int(path.split("/")[-1])
             return get_student(self, student_id)

        return send_404(self)
    def do_POST(self):
        add_cors_headers(self)
        if self.path == "/api/students":
            return create_student(self)
        return send_404(self)
    def do_PUT(self):
        add_cors_headers(self)
        if self.path.startswith("/api/students/"):
            student_id = int(self.path.split("/")[-1])
            return update_student(self, student_id)
        return send_404(self)
    def do_DELETE(self):
        if self.path.startswith("/api/students/"):
            student_id = int(self.path.split("/")[-1])
            return delete_student(self, student_id)
        return send_404(self)
    
  