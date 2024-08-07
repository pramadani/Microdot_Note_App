import json

DATABASE = "db/note.json"

def init_db():
    if not file_exists(DATABASE):
        with open(DATABASE, 'w') as file:
            file.write("[]")

def file_exists(path):
    try:
        with open(path, 'r'):
            return True
    except:
        return False

def read_notes():
    with open(DATABASE, 'r') as file:
        notes = json.load(file)
    return notes

def write_notes(notes):
    with open(DATABASE, 'w') as file:
        json.dump(notes, file)

def add_note(content):
    notes = read_notes()
    new_id = max(note['id'] for note in notes) + 1 if notes else 1
    notes.append({"id": new_id, "content": content})
    write_notes(notes)
    return new_id

def get_note_by_id(note_id):
    notes = read_notes()
    for note in notes:
        if note['id'] == note_id:
            return note
    return None

def update_note(note_id, new_content):
    notes = read_notes()
    for note in notes:
        if note['id'] == note_id:
            note['content'] = new_content
            write_notes(notes)
            return True
    return False

def delete_note(note_id):
    notes = read_notes()
    notes = [note for note in notes if note['id'] != note_id]
    write_notes(notes)
    return True

init_db()