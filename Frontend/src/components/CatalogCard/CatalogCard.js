import React from 'react';
import { Card } from "antd";
import image from '../../images/8-тр.jpeg'
import './CatalogCard.css';

function CatalogCard({ item }) {
    return (
        <Card
            hoverable
            cover={
                <img className="item__img" alt="example" src={image} />
            }
            style={{ width: 300, borderRadius: '15px' }}>

            <div className='bouquet__info'>
                <h1 className='bouquet__title'>Ideal bouquet for {item.eventType}</h1>
                <h3 className='bouquet__desc'>Consists of {item.flowers.length} {item.flowers[0].name}s packed in {item.packing.name}</h3>
                <p className="bouquet__price"> <strong>Price:</strong> ${item.price}</p>
                <button className='bouquet__btn'>Add to my order</button>
            </div>

        </Card>
    );
}

export default CatalogCard;