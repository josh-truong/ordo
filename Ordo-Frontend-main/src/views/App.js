import React from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route
} from 'react-router-dom';

import MovieList from './MovieList';
import MovieDesc from './MovieDesc';

import Footer from '../components/Footer';
import Navigation from '../components/Navigation/Navigation';

function App() {
  return (
    <>
      <Router>
        <Navigation />
        <div style={{ margin: '0 10% 0 10%' }}>
          <Routes>
            <Route exact path='/' element={<MovieList />} />
            <Route exact path='/desc' element={<MovieDesc />} />
          </Routes>
        </div>
      </Router>
      <Footer />
    </>
  );
}
export default App;
