const { createApp, ref, onMounted } = Vue;

const app = createApp({
    setup() {
        const noteContent = ref('');
        const notes = ref([]);
        const displayApp = ref("none")

        const fetchNotes = async () => {
            const response = await axios.get('/note/notes');
            notes.value = response.data;
        };

        const addNote = async () => {
            await axios.post('/note/notes', { content: noteContent.value });
            noteContent.value = '';
            await fetchNotes();
        };

        onMounted(() => {
            fetchNotes();
            displayApp.value = "inline"
        });

        return {
            noteContent,
            notes,
            addNote,
            displayApp
        };
    }
});

app.mount('#app');