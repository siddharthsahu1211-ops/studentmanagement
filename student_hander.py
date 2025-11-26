import json
import database 
from utils.responses import send_json, send_404

def parse_body(handler):
    length=int(handler.headers.get("content-length",0))
    raw= handler.rfile.read(length)
    return json.loads(raw.decode("utf-8"))

def get_all_student(handler):
    student = database.get_all_student()
    return send_json(handler,200,students)