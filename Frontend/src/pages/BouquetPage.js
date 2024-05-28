import React from 'react';
import './Login.css';
import { NavLink } from 'react-router-dom';
import { useState } from 'react';
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import './BouquetPage.css';
import { BouquetBuilder } from '../pattern/BouquetBuilder';
import { addToOrder } from '../redux/orderSlice';
import { useDispatch } from "react-redux";

function BouquetPage() {

    const events = ['Choose event', 'Wedding', 'Birthday', 'Valentine Day', 'Funerals'];
    let [event, setEvent] = useState('Choose event');
    const flowersForBouquet = ['Choose flower', 'Red Rose', 'White Rose', 'Blue Rose', 'Yellow Lily', 'Purple Lavender', 'Red Tulip'];
    let [flowerForBouquet, setFlowerForBouquet] = useState('Choose event');
    const [quantity, setQuantity] = useState(0);
    const packings = ['Choose packing', 'Craft', 'Box'];
    const [packing, setPacking] = useState('');
    const [flowers, setFlowers] = useState([]);
    const [pack, setPack] = useState([]);
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const [item, setItem] = useState({});
    const number = 1;
    const [count, setCount] = useState(1);


    const handleChange = (e) => {
        const value = parseInt(e.target.value, 10); // Перетворюємо введене значення в число
        setQuantity(value);
    };

    const handleChange2 = (e) => {
        const value = parseInt(e.target.value, 10); // Перетворюємо введене значення в число
        setCount(value);
    };

    const handleAdd = ({ item, count }) => {
        dispatch(addToOrder({ item, count }));
        console.log('aaa')
    }

    const navigation = () => {
        navigate(`/catalog`)
    }

    const press = async () => {
        console.log(event);
        console.log(flowerForBouquet);
        console.log(quantity);
        console.log(packing);
        console.log(typeof quantity);
        try {

            const response = await axios.get('http://127.0.0.1:5000/flower');
            /*console.log(response.data);*/
            console.log(response.data);
            setFlowers(response.data)

        } catch (error) {
            console.log(error);
        }

        const lol = {
            name: flowerForBouquet,
            color: "white",
            price: 40
        }
        /*const here = flowers.find(flower => flower.name == flowerForBouquet);*/
        console.log(lol)
        try {

            const response = await axios.get('http://127.0.0.1:5000/packing');
            /*console.log(response.data);*/
            console.log(response.data);
            setPack(response.data)

        } catch (error) {
            console.log(error);
        }
        const lol1 = {
            name: packing,
            price: 55
        }
        console.log(lol1)
        const price = (lol.price * quantity) + lol1.price;
        /*const here1 = pack.find(pac => pac.name == packing);*/
        const bouquetBuilder = new BouquetBuilder();
        const bouquet = bouquetBuilder
            .setEventType(event)
            .setPrice(price)
            .setPacking(lol1)
            .setFlowers(lol, quantity)

        console.log(bouquet);
        setItem(bouquet);

        /*handleAdd({bouquet, number});
        navigation();*/

    }

    return (
        <div className='login__page'>
            <div className='login__form'>
                <h1>Create your own bouquet</h1>
                <form>
                    <div className='input__block'>
                        <div>
                            <input className='input' onChange={handleChange2} name='quantity' type='number' placeholder='Quantity of bouquets' min={1}></input>
                        </div>
                        <div>
                            <select className='select' onChange={(e) => setEvent(e.target.value)}>
                                {
                                    events.map((type) => <option key={type} value={type}>{type}</option>)
                                }
                            </select>
                        </div>
                        <div>
                            <select className='select' onChange={(e) => setFlowerForBouquet(e.target.value)}>
                                {
                                    flowersForBouquet.map((type) => <option key={type} value={type}>{type}</option>)
                                }
                            </select>
                        </div>
                        <div>
                            <input className='input' onChange={handleChange} name='quantity' type='number' placeholder='Quantity of flowers' min={1}></input>
                        </div>
                        <div>
                            <select className='select' onChange={(e) => setPacking(e.target.value)}>
                                {
                                    packings.map((type) => <option key={type} value={type}>{type}</option>)
                                }
                            </select>
                        </div>
                    </div>
                </form>
                <button onClick={press} className='input__btn'>Create and Add to order</button>
                <button onClick={() => { handleAdd({ item, count }); navigation(); }} className='input__btn'>Create and Add to order</button>
            </div>
        </div>
    );
};

export default BouquetPage;