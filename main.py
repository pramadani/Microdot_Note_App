from microdot import Microdot
from router.note_router import note_app

def create_app():
    app = Microdot()
    app.mount(note_app, url_prefix='/note')
    return app

app = create_app()
app.run(host="0.0.0.0", port=80)