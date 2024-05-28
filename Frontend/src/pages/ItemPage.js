import React from 'react';
import Header from '../components/Header/Header';
import './ItemPage.css';
import { useState } from 'react';
import { useEffect } from 'react';
import { useNavigate, useParams } from "react-router-dom";
import axios from 'axios';
import { addToOrder } from '../redux/orderSlice';
import { useDispatch } from "react-redux";


function ItemPage() {

  const [isUserLoggedIn, setIsUserLoggedIn] = useState(false);
  const { id } = useParams();
  const [count, setCount] = useState(1);
  const [item, setItem] = useState({});
  const navigate = useNavigate();
  const [bouquetName, setBouquetName] = useState('');
  const [packing, setPacking] = useState({});
  const dispatch = useDispatch();

  useEffect(() => {
    checkUserStatus();
    findItem()
  }, []);

  const checkUserStatus = () => {
    const loggedInUser = JSON.parse(localStorage.getItem('loggined_user'));
    if (loggedInUser) {
      setIsUserLoggedIn(true);
      console.log('true');
    } else {
      setIsUserLoggedIn(false);
      console.log('false');
    }
  };

  const findItem = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:5000/bouquet/${id}`);
      setItem(response.data);
      console.log(response.data);
      setBouquetName(response.data.flowers[0].name)
      setPacking(response.data.packing);
    } catch (error) {
      console.log(error);
    }

  }

  const handleAdd = ({ item, count }) => {
    if(isUserLoggedIn == false) {
      navigate('/login');
    } else {
      dispatch(addToOrder({ item, count }));
    console.log('aaa')
    }
  }

  const navigation = () => {
    navigate(`/catalog`)
  }

  return (
    <div>
      <Header log={isUserLoggedIn} />
      <main className="item-page">
        <div className="item-page__container">
          <div className="item-page-block">
            <img alt="bouquet" className="item-page__img" src={item.image} />
            <div className="right">
              <h2 className="item-page__title">Ideal {bouquetName} Bouquet</h2>
              <div className="item-page__desc">{item.eventType}</div>
              <div className="item-page__desc">Packed in: {packing.name}</div>
              <div>
                <span className="question">Countable field:</span>
                <input onChange={(e) => setCount(+e.target.value)}
                  defaultValue={1} className="input-number" type='number'></input>
              </div>
            </div>
          </div>
          <div className="under-block">
            <div className="price-block">Price: ${item.price}</div>
            <div className="buttons-block">
              <button className="first-btn" onClick={() => navigate(-1)}>Go back</button>
              <button onClick={() => { handleAdd({ item, count }); navigation(); }} className="button">Add to cart</button>
            </div>
          </div>
          <div>

          </div>
        </div>
      </main>
    </div>
  );
};

export default ItemPage;