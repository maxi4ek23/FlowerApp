import { BrowserRouter } from 'react-router-dom';
import './App.css';
import Header from './components/Header/Header';
import {Route, Routes } from "react-router-dom";
import Home from './pages/Home';
import Catalog from './pages/Catalog';
import Login from './pages/Login';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home />}></Route>
        <Route path='/catalog' element={<Catalog />}></Route>
        <Route path='/login' element={<Login />}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
