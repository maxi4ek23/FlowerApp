import React from 'react';
import { Card } from "antd";

function CatalogCard ({item}) {
    return (
        <Card
        style={{width: 300, borderRadius: '15px'}}>
            <h1>{item.name}</h1>
        </Card>
    );
}

export default CatalogCard;