import React, { useState } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './components/Login';

const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLogin = (status) => {
    setIsLoggedIn(status);
  };

  return (
    <BrowserRouter> {/* Wrap everything inside BrowserRouter */}
      <div>
        <h1>Bienvenido al sistema de gestión de pacientes</h1>
        <Routes>
          {/* Define routes here */}
          <Route
            path="/"
            element={!isLoggedIn ? <Login onLogin={handleLogin} /> : <div>Loading...</div>}
          />
          <Route
            path="/dashboard"
            element={isLoggedIn ? (
              <div>
                <h2>Dashboard del Médico</h2>
                {/* Aquí puedes agregar las gráficas y demás contenido del médico */}
              </div>
            ) : (
              <div>Redirigiendo...</div>
            )}
          />
        </Routes>
      </div>
    </BrowserRouter>
  );
};

export default App;
