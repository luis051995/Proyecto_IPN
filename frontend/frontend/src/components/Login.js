import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const navigate = useNavigate();  // useNavigate instead of useHistory

  const handleSubmit = (event) => {
    event.preventDefault();
    axios
      .post('http://127.0.0.1:8000/api/login/', { username, password })
      .then((response) => {
        // Guarda el token o la información del usuario
        localStorage.setItem('token', response.data.token);
        navigate('/dashboard');  // use navigate for routing
      })
      .catch((error) => {
        setError('Usuario o contraseña incorrectos');
      });
  };

  return (
    <div>
      <h1>Iniciar sesión</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Usuario</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Contraseña</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">Iniciar sesión</button>
      </form>
      {error && <p>{error}</p>}
    </div>
  );
};

export default Login;
