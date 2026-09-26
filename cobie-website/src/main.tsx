import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.tsx'


import '@fontsource/poppins/400.css'; // Normal
import '@fontsource/poppins/500.css'; // medium

import '@fontsource/poppins/600.css'; // Semibold
import '@fontsource/poppins/700.css'; // Bold

import './index.css'; 

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
