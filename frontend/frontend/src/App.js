// App.js

import React, { useState } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import Login from './components/Login';
import Grafico from './components/Grafico';

const theme = createTheme({
  palette: {
    primary: {
      main: '#4caf50', // Verde
    },
    secondary: {
      main: '#ff9800', // Naranja
    },
  },
});

const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLogin = (status) => {
    setIsLoggedIn(status);
  };

  return (
    <ThemeProvider theme={theme}>
      <BrowserRouter>
        <div style={{ padding: '20px', backgroundColor: '#f0f8ff', minHeight: '100vh' }}>
          <h1 style={{ color: theme.palette.primary.main }}>Bienvenido al sistema de gestión de pacientes</h1>
          <Routes>
            <Route
              path="/"
              element={!isLoggedIn ? <Login onLogin={handleLogin} /> : <div>Redirigiendo al dashboard...</div>}
            />
            <Route
              path="/dashboard"
              element={isLoggedIn ? (
                <div>
                  <h2 style={{ color: theme.palette.secondary.main }}>Dashboard del Médico</h2>
                  <Grafico usuarioId={1} />
                </div>
              ) : (
                <div>Redirigiendo...</div>
              )}
            />
          </Routes>
        </div>
      </BrowserRouter>
    </ThemeProvider>
  );
};

export default App;
