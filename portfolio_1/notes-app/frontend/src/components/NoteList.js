import React from 'react';

const NoteList = ({ notes, onSelectNote, onDeleteNote }) => {
  if (notes.length === 0) {
    return (
      <div style={styles.emptyMessage}>
        <p>No hay notas aún. ¡Crea una nueva!</p>
      </div>
    );
  }

  return (
    <div style={styles.container}>
      <h2>Mis Notas</h2>
      <div style={styles.list}>
        {notes.map((note) => (
          <div key={note.id} style={styles.noteCard}>
            <div
              onClick={() => onSelectNote(note.id)}
              style={styles.noteContent}
            >
              <h3 style={styles.noteTitle}>{note.title}</h3>
              <p style={styles.notePreview}>{note.content.substring(0, 100)}...</p>
              <small style={styles.noteDate}>
                Actualizado: {new Date(note.updated_at).toLocaleDateString('es-ES')}
              </small>
            </div>
            <button
              onClick={(e) => {
                e.stopPropagation();
                onDeleteNote(note.id);
              }}
              style={styles.deleteButton}
              title="Eliminar nota"
            >
              ✕
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

const styles = {
  container: {
    marginTop: '30px',
  },
  list: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))',
    gap: '15px',
  },
  noteCard: {
    backgroundColor: '#fff',
    padding: '15px',
    borderRadius: '8px',
    border: '1px solid #ddd',
    cursor: 'pointer',
    transition: 'all 0.3s ease',
    display: 'flex',
    flexDirection: 'column',
    position: 'relative',
    boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
  },
  noteContent: {
    flex: 1,
  },
  noteTitle: {
    margin: '0 0 8px 0',
    fontSize: '16px',
    color: '#333',
  },
  notePreview: {
    margin: '0 0 10px 0',
    fontSize: '13px',
    color: '#666',
    lineHeight: '1.4',
  },
  noteDate: {
    color: '#999',
    fontSize: '12px',
  },
  deleteButton: {
    position: 'absolute',
    top: '10px',
    right: '10px',
    backgroundColor: '#f44336',
    color: 'white',
    border: 'none',
    borderRadius: '50%',
    width: '24px',
    height: '24px',
    cursor: 'pointer',
    fontSize: '16px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  emptyMessage: {
    textAlign: 'center',
    padding: '40px 20px',
    color: '#999',
    backgroundColor: '#f9f9f9',
    borderRadius: '8px',
    border: '1px solid #ddd',
    marginTop: '30px',
  },
};

export default NoteList;
