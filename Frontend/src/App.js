import { BrowserRouter } from 'react-router-dom';
import './App.css';
import Header from './components/Header/Header';
import { Route, Routes } from "react-router-dom";
import Home from './pages/Home';
import Catalog from './pages/Catalog';
import Login from './pages/Login';
import Signup from './pages/Signup';
import UserPage from './pages/UserPage';
import { Provider } from "react-redux";
import store from './redux/store';
import ItemPage from './pages/ItemPage';
import BouquetPage from './pages/BouquetPage';

function App() {
  return (


    <Provider store={store}>
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Home />}></Route>
          <Route path='/catalog' element={<Catalog />}></Route>
          <Route path='/login' element={<Login />}></Route>
          <Route path='/signup' element={<Signup />}></Route>
          <Route path='/user/:id' element={<UserPage />}></Route>
          <Route path='/catalog/:id' element={<ItemPage />}></Route>
          <Route path='/bouquet' element={<BouquetPage />}></Route>
        </Routes>
      </BrowserRouter>
    </Provider>


  );
}

export default App;
