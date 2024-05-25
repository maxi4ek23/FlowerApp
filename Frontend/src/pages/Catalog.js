import React from 'react';
import './Catalog.css';
import Header from '../components/Header/Header';
import CatalogCard from '../components/CatalogCard/CatalogCard';

function Catalog() {

  const datas = [
    {
      name: 'lol',
      age: '12'
    },
    {
      name: 'lol1',
      age: '12'
    },
    {
      name: 'lol2',
      age: '12'
    },
    {
      name: 'lol3',
      age: '12'
    },
    {
      name: 'lol4',
      age: '12'
    },
    {
      name: 'lol5',
      age: '12'
    }
  ]

  return (
    <div>
      <Header />
      <main className='catalog'>
        <div className='catalog__container'>
          <div className='catalog-title-block'>
            <h1 className='catalog__title'>Welcome!!! There all our bouquets</h1>
          </div>
          <div className='catalog-filter-block'>
            <div className='catalog__filters'>
              <select>
                <option>Events</option>
              </select>
              <select></select>

            </div>
          </div>
          <div className='catalog-card-block'>
            {
              datas.map((data, idx) => (
                <CatalogCard item={data} key={idx} />
              ))}
          </div>


        </div>

      </main>
    </div>
  );
};

export default Catalog;