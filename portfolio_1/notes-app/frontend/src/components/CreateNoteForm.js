import React, { useState } from 'react';
import { noteService } from '../services/noteService';

const CreateNoteForm = ({ onNoteCreated }) => {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    // Validación
    if (!title.trim()) {
      setError('El título es requerido');
      return;
    }
    if (!content.trim()) {
      setError('El contenido es requerido');
      return;
    }

    setLoading(true);
    try {
      await noteService.createNote(title, content);
      setTitle('');
      setContent('');
      onNoteCreated();
    } catch (err) {
      setError(err.title?.[0] || err.content?.[0] || 'Error al crear la nota');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} style={styles.form}>
      <h2>Nueva Nota</h2>
      {error && <div style={styles.error}>{error}</div>}
      
      <div style={styles.formGroup}>
        <label htmlFor="title">Título:</label>
        <input
          id="title"
          type="text"
          placeholder="Ingresa el título"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          style={styles.input}
          disabled={loading}
        />
      </div>

      <div style={styles.formGroup}>
        <label htmlFor="content">Contenido:</label>
        <textarea
          id="content"
          placeholder="Ingresa el contenido"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          style={styles.textarea}
          rows="5"
          disabled={loading}
        />
      </div>

      <button
        type="submit"
        style={{ ...styles.button, opacity: loading ? 0.6 : 1 }}
        disabled={loading}
      >
        {loading ? 'Guardando...' : 'Crear Nota'}
      </button>
    </form>
  );
};

const styles = {
  form: {
    backgroundColor: '#f9f9f9',
    padding: '20px',
    borderRadius: '8px',
    marginBottom: '30px',
    border: '1px solid #ddd',
  },
  formGroup: {
    marginBottom: '15px',
    display: 'flex',
    flexDirection: 'column',
  },
  input: {
    padding: '10px',
    border: '1px solid #ddd',
    borderRadius: '4px',
    fontSize: '14px',
    fontFamily: 'Arial, sans-serif',
  },
  textarea: {
    padding: '10px',
    border: '1px solid #ddd',
    borderRadius: '4px',
    fontSize: '14px',
    fontFamily: 'Arial, sans-serif',
    resize: 'vertical',
  },
  button: {
    backgroundColor: '#4CAF50',
    color: 'white',
    padding: '10px 20px',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
    fontSize: '14px',
    fontWeight: 'bold',
  },
  error: {
    backgroundColor: '#f8d7da',
    color: '#721c24',
    padding: '10px',
    borderRadius: '4px',
    marginBottom: '15px',
    border: '1px solid #f5c6cb',
  },
};

export default CreateNoteForm;
