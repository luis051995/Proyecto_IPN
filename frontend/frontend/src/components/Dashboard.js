// src/components/Dashboard.js
import React, { useState } from 'react';
import Grafico from './Grafico';

const Dashboard = () => {
  const [usuarioId, setUsuarioId] = useState('');

  const handleUsuarioChange = (e) => {
    setUsuarioId(e.target.value);
  };

  return (
    <div>
      <h2>Panel del Médico</h2>
      <label htmlFor="usuario">Seleccionar paciente:</label>
      <select id="usuario" onChange={handleUsuarioChange}>
        <option value="">--Selecciona un paciente--</option>
        <option value="1">Paciente 1</option>
        <option value="2">Paciente 2</option>
        {/* Aquí puedes cargar los pacientes dinámicamente con fetch si lo deseas */}
      </select>

      {usuarioId && (
        <div>
          <h3>Gráficas del paciente</h3>
          <Grafico usuarioId={usuarioId} />
        </div>
      )}
    </div>
  );
};

export default Dashboard;
