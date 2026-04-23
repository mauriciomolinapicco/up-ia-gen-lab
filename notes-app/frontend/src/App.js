import React, { useState, useEffect } from 'react';
import CreateNoteForm from './components/CreateNoteForm';
import NoteList from './components/NoteList';
import NoteDetail from './components/NoteDetail';
import LoadingSpinner from './components/LoadingSpinner';
import { noteService } from './services/noteService';
import './App.css';

function App() {
  const [notes, setNotes] = useState([]);
  const [selectedNoteId, setSelectedNoteId] = useState(null);
  const [selectedNote, setSelectedNote] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // Cargar notas al montar el componente
  useEffect(() => {
    loadNotes();
  }, []);

  // Cargar la nota seleccionada cuando cambia el ID
  useEffect(() => {
    if (selectedNoteId) {
      loadSelectedNote(selectedNoteId);
    }
  }, [selectedNoteId]);

  const loadNotes = async () => {
    setLoading(true);
    setError('');
    try {
      const data = await noteService.getAllNotes();
      setNotes(data);
    } catch (err) {
      setError('Error al cargar las notas. Asegúrate de que el servidor está en ejecución.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const loadSelectedNote = async (id) => {
    try {
      const data = await noteService.getNoteById(id);
      setSelectedNote(data);
    } catch (err) {
      setError('Error al cargar la nota');
      console.error(err);
    }
  };

  const handleNoteCreated = () => {
    loadNotes();
    setSelectedNoteId(null);
    setSelectedNote(null);
  };

  const handleSelectNote = (id) => {
    setSelectedNoteId(id);
  };

  const handleDeleteNote = async (id) => {
    if (window.confirm('¿Estás seguro de que deseas eliminar esta nota?')) {
      try {
        await noteService.deleteNote(id);
        loadNotes();
        if (selectedNoteId === id) {
          setSelectedNoteId(null);
          setSelectedNote(null);
        }
      } catch (err) {
        setError('Error al eliminar la nota');
        console.error(err);
      }
    }
  };

  const handleBack = () => {
    setSelectedNoteId(null);
    setSelectedNote(null);
  };

  if (loading) {
    return <LoadingSpinner />;
  }

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>📝 Aplicación de Notas</h1>
        <p className="subtitle">Crea, guarda y organiza tus notas</p>
      </header>

      <main className="app-main">
        {error && (
          <div className="error-banner">
            {error}
            <button onClick={() => setError('')} className="close-error">✕</button>
          </div>
        )}

        {selectedNote ? (
          <NoteDetail note={selectedNote} onBack={handleBack} />
        ) : (
          <>
            <CreateNoteForm onNoteCreated={handleNoteCreated} />
            <NoteList
              notes={notes}
              onSelectNote={handleSelectNote}
              onDeleteNote={handleDeleteNote}
            />
          </>
        )}
      </main>

      <footer className="app-footer">
        <p>© 2024 Aplicación de Notas - Desarrollado con React y Django</p>
      </footer>
    </div>
  );
}

export default App;
