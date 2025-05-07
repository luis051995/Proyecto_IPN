import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import axios from 'axios';
import { Chart as ChartJS, CategoryScale, LinearScale, LineElement, PointElement, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, LineElement, PointElement, Title, Tooltip, Legend);

const Grafico = ({ usuarioId }) => {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:8000/api/historial/${usuarioId}/`)
      .then((response) => {
        const { historial } = response.data;
        const fechas = historial.map((h) => h.fecha);
        const acetona = historial.map((h) => h.acetona);

        setData({
          labels: fechas,
          datasets: [
            {
              label: 'Nivel de Acetona',
              data: acetona,
              fill: false,
              borderColor: 'rgb(75, 192, 192)',
              tension: 0.1,
            },
          ],
        });
      })
      .catch((error) => {
        console.error('Hubo un error al obtener los datos del historial:', error);
      });
  }, [usuarioId]);

  if (!data) {
    return <div>Cargando...</div>;
  }

  return (
    <div>
      <h2>Historial de Acetona</h2>
      <Line data={data} />
    </div>
  );
};

export default Grafico;
