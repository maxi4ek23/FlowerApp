import React from 'react';
import './Catalog.css';
import Header from '../components/Header/Header';
import CatalogCard from '../components/CatalogCard/CatalogCard';
import { useState } from 'react';
import { useEffect } from 'react';
import datas from '../data/data';
import axios from 'axios';

function Catalog() {

  const filters = ['Filter by event', 'All', 'Wedding', 'Birthday', 'Valentine Day', 'Funerals'];
  let [filterEvent, setFilterEvent] = useState('Filter by event');

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
    } else {
      setIsUserLoggedIn(false);
    }
  };

  const filter = async () => {
    console.log(filterEvent);
    if (filterEvent === 'All' || filterEvent === 'Filter by event') {
      fetchData();
    }
    try {
      const response = await axios.get(`http://127.0.0.1:5000/bouquet/event_type/${filterEvent}`);
      setData(response.data);
    } catch (error) {
      console.log(error);
    }
  }

  const fetchData = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:5000/bouquet');
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
              <select onChange={(e) => setFilterEvent(e.target.value)}>
                {
                  filters.map((type) => <option key={type} value={type}>{type}</option>)
                }
              </select>
              <button onClick={filter} className='catalog__button'>Submit filter</button>

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