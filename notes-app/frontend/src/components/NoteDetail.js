import React from 'react';

const NoteDetail = ({ note, onBack }) => {
  if (!note) {
    return null;
  }

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('es-ES', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
    });
  };

  return (
    <div style={styles.container}>
      <button onClick={onBack} style={styles.backButton}>
        ← Volver a Notas
      </button>

      <div style={styles.contentContainer}>
        <h1 style={styles.title}>{note.title}</h1>

        <div style={styles.metadata}>
          <span>Creada: {formatDate(note.created_at)}</span>
          <span style={{ marginLeft: '20px' }}>
            Actualizada: {formatDate(note.updated_at)}
          </span>
        </div>

        <div style={styles.contentBox}>
          <p style={styles.content}>{note.content}</p>
        </div>
      </div>
    </div>
  );
};

const styles = {
  container: {
    marginBottom: '30px',
  },
  backButton: {
    backgroundColor: '#2196F3',
    color: 'white',
    padding: '8px 16px',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
    fontSize: '14px',
    marginBottom: '20px',
  },
  contentContainer: {
    backgroundColor: '#fff',
    padding: '30px',
    borderRadius: '8px',
    border: '1px solid #ddd',
    boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
  },
  title: {
    margin: '0 0 15px 0',
    fontSize: '28px',
    color: '#333',
  },
  metadata: {
    color: '#999',
    fontSize: '12px',
    paddingBottom: '15px',
    borderBottom: '1px solid #eee',
    marginBottom: '20px',
  },
  contentBox: {
    backgroundColor: '#f9f9f9',
    padding: '20px',
    borderRadius: '4px',
    border: '1px solid #eee',
  },
  content: {
    margin: 0,
    fontSize: '15px',
    color: '#333',
    lineHeight: '1.6',
    whiteSpace: 'pre-wrap',
  },
};

export default NoteDetail;
