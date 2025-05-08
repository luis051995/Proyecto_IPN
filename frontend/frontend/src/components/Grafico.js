// Grafico.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import ChartComponent from './ChartComponent';

const Grafico = ({ usuarioId }) => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchHistorial = async () => {
      try {
        const token = localStorage.getItem('access');
        const response = await axios.get(`http://127.0.0.1:8000/api/historial/${usuarioId}/`, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });

        if (response.data.historial) {
          const formattedData = response.data.historial.map(entry => ({
            fecha: entry.fecha,
            acetona: entry.acetona
          }));
          setData(formattedData);
        } else {
          console.warn("No se recibió historial");
          setData([]); // Vacío pero no null
        }
      } catch (error) {
        console.error("Error al obtener historial:", error);
        setData([]); // Para prevenir el error "data is null"
      }
    };

    fetchHistorial();
  }, [usuarioId]);

  return (
    <div>
      <h3>Historial de Acetona</h3>
      <ChartComponent data={data} />
    </div>
  );
};

export default Grafico;
