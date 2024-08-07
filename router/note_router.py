from microdot import Microdot, send_file
from db.init import read_notes, add_note
import json

note_app = Microdot()

@note_app.route('')
def index(request):
    return send_file('view/note-app/index.html')

@note_app.route('/notes', methods=['POST'])
def save(request):
    json = request.json
    content = json["content"]
    
    add_note(content)
    
    return 'Note saved', 200

@note_app.route('/notes', methods=['GET'])
def get_notes(request):
    notes = read_notes()
    response_body = json.dumps(notes)
    
    return response_body

@note_app.route("/<path:path>")
def static(request, path):
    if ".." in path:
        return "Not found", 404
    return send_file("view/note-app/" + path)