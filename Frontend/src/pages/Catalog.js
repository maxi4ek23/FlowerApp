import React from 'react';
import './Catalog.css';
import Header from '../components/Header/Header';
import CatalogCard from '../components/CatalogCard/CatalogCard';
import { useState } from 'react';
import { useEffect } from 'react';
import datas from '../data/data';
import axios from 'axios';

function Catalog() {

  const filters = ['Filter by event', 'Wedding', 'Birthday', 'Valentine Day', 'Funerals'];

  const [isUserLoggedIn, setIsUserLoggedIn] = useState(false);
  const [data, setData] = useState([]);

  useEffect(() => {
    checkUserStatus();
    fetchData();
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

  const fetchData = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:5000/bouquet');
      console.log(response.data);
      setData(response.data);
    } catch (error) {
      console.log(error);
    }
  }

  return (
    <div>
      <Header log={isUserLoggedIn} />
      <main className='catalog'>
        <div className='catalog__container'>
          <div className='catalog-title-block'>
            <h1 className='catalog__title'>Welcome!!! There all our bouquets</h1>
          </div>
          <div className='catalog-filter-block'>
            <div className='catalog__filters'>
              <select>
                {
                  filters.map((type) => <option key={type} value={type}>{type}</option>)
                }
              </select>
              <select></select>

            </div>
          </div>
          <div className='catalog-card-block'>
            {
              data.map((data, idx) => (
                <CatalogCard item={data} key={idx} />
              ))}
          </div>


        </div>

      </main>
    </div>
  );
};

export default Catalog;