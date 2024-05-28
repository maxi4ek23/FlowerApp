import React from 'react';
import { Card } from "antd";
import image from '../../images/8-тр.jpeg'
import './CatalogCard.css';
import { NavLink } from "react-router-dom";

function CatalogCard({ bouquet }) {


    return (
        <Card
            hoverable
            cover={
                <img className="item__img" alt="example" src={image} />
            }
            style={{ width: 300, borderRadius: '15px' }}>

            <div className='bouquet__info'>
                <h1 className='bouquet__title'>Ideal bouquet for {bouquet.eventType}</h1>
                <h3 className='bouquet__desc'>{bouquet.flowers.length} {bouquet.flowers[0].name}s packed in {bouquet.packing.name}</h3>
                <p className="bouquet__price"> <strong>Price:</strong> ${bouquet.price}</p>
                <NavLink to={`/catalog/${bouquet.id}`}>
                    <button className='bouquet__btn'>View more</button>
                </NavLink>
            </div>

        </Card>
    );
}

export default CatalogCard;