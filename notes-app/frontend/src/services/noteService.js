import axios from 'axios';

const API_BASE_URL = 'http://localhost:8001/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const noteService = {
  // Obtener todas las notas
  getAllNotes: async () => {
    try {
      const response = await api.get('/notes/');
      return response.data;
    } catch (error) {
      throw error.response?.data || 'Error al obtener notas';
    }
  },

  // Obtener una nota por ID
  getNoteById: async (id) => {
    try {
      const response = await api.get(`/notes/${id}/`);
      return response.data;
    } catch (error) {
      throw error.response?.data || 'Error al obtener la nota';
    }
  },

  // Crear una nueva nota
  createNote: async (title, content) => {
    try {
      const response = await api.post('/notes/', {
        title,
        content,
      });
      return response.data;
    } catch (error) {
      throw error.response?.data || 'Error al crear la nota';
    }
  },

  // Actualizar una nota
  updateNote: async (id, title, content) => {
    try {
      const response = await api.put(`/notes/${id}/`, {
        title,
        content,
      });
      return response.data;
    } catch (error) {
      throw error.response?.data || 'Error al actualizar la nota';
    }
  },

  // Eliminar una nota
  deleteNote: async (id) => {
    try {
      await api.delete(`/notes/${id}/`);
    } catch (error) {
      throw error.response?.data || 'Error al eliminar la nota';
    }
  },
};

export default api;
