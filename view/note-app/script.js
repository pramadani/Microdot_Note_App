document.addEventListener('DOMContentLoaded', () => {
    const fetchNotes = () => {
        fetch('/note/notes')
            .then(response => response.json())
            .then(data => {
                const notesList = document.getElementById('notes-list');
                if (data.length) {
                    notesList.innerHTML = data.map(note => `
                        <div class="note">
                            <div class="note-id">ID: ${note.id}</div>
                            <div class="note-content">${note.content}</div>
                        </div>
                    `).join('');
                } else {
                    notesList.innerHTML = 'No notes available.';
                }
            })
            .catch(error => {
                console.error('Error fetching notes:', error);
                document.getElementById('notes-list').textContent = 'Error loading notes.';
            });
    };

    fetchNotes();

    document.getElementById('note-form').addEventListener('submit', event => {
        event.preventDefault();
        const data = Object.fromEntries(new FormData(event.target));
        fetch('/note/notes', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (response.ok) {
                alert('Note saved');
                fetchNotes();
            } else {
                alert('Failed to save note');
            }
        })
        .catch(error => {
            console.error('Error saving note:', error);
            alert('Error saving note');
        });
    });
});
