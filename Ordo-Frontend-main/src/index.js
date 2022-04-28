import React from 'react';
import * as ReactDOMClient from 'react-dom/client';
import App from './views/App';
import reportWebVitals from './test/reportWebVitals';


const container = document.getElementById('root');

// Create a root.
const root = ReactDOMClient.createRoot(container)

root.render(<App tab='home'/>) // Intial render
root.render(<App tab='profile'/>)

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
