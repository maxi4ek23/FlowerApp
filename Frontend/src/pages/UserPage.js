import React from 'react';
import Header from '../components/Header/Header';
import './UserPage.css';
import { useState } from 'react';
import { useEffect } from 'react';
import { useNavigate, useParams } from "react-router-dom";
import axios from 'axios';
import { CardFactory } from '../pattern/CardFactory';
import { OrderBuilder } from '../pattern/OrderBuilder';
import { useSelector } from "react-redux";
import ShoppingItem from '../components/ShoppingItem/ShoppingItem'
import { clear } from '../redux/orderSlice';
import { useDispatch } from "react-redux";


function UserPage() {

    const [selectedOption, setSelectedOption] = useState('');
    const delivers = ['Choose Delivery', 'Nova Posta', 'Meest', 'Ukrposta'];
    let [delivery, setDelivery] = useState('Choose Delivery');
    const deliveryPrice = 50;
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const [isUserLoggedIn, setIsUserLoggedIn] = useState(false);
    const [user, setUser] = useState({});
    const [cardInfo, setCardInfo] = useState({});
    const { id } = useParams();
    const [here, setHere] = useState(false);

    const items = useSelector((state) => state.order.orderItems);
    let totalPrice = useSelector((state) => state.order.orderTotalPrice);

    useEffect(() => {
        checkUserStatus();
        findUser();
        console.log(items);
    }, []);

    const checkUserStatus = () => {
        const loggedInUser = JSON.parse(localStorage.getItem('loggined_user'));
        if (loggedInUser) {
            setIsUserLoggedIn(true);
        } else {
            setIsUserLoggedIn(false);
        }
    };

    const logout = () => {
        console.log(JSON.parse(localStorage.getItem('loggined_user')));
        localStorage.removeItem('loggined_user');
        setIsUserLoggedIn(false);
        console.log('false');
        navigate('/catalog')
    }

    const findUser = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:5000/user/${id}`);
            setUser(response.data);
            if (response.data.card_type !== null) {
                setHere(true);
                cardInfo.type = response.data.card_type;
                if (response.data.card_type == 'gold') {
                    cardInfo.discount = 5
                }
                if (response.data.card_type == 'bonus') {
                    cardInfo.discount = 10
                }
                if (response.data.card_type == 'social') {
                    cardInfo.discount = 15
                }
            }
        } catch (error) {
            console.log(error);
        }
    }


    const handleOptionChange = (event) => {
        setSelectedOption(event.target.value);
    };

    const handleClick = async () => {
        const card = CardFactory.createCard(selectedOption);
        setCardInfo(card);
        const change = user
        change.card_type = selectedOption;
        setUser(change);
        /*console.log(user);*/
        try {
            const response = await axios.put(`http://127.0.0.1:5000/user/${id}`, user);
            /*setUser(response.data);*/
        } catch (error) {
            console.log(error);
        }
        setHere(true);
        /*console.log(here);*/
    };

    const isEmptyObject = (obj) => {
        return Object.keys(obj).length === 0;
    };

    const createOrder = async () => {
        if (!isEmptyObject(cardInfo)) {
            totalPrice = totalPrice * (1 - (cardInfo.discount / 100))
        }
        totalPrice = totalPrice + deliveryPrice;
        const orderBuilder = new OrderBuilder();
        const order = orderBuilder
            .setPrice(totalPrice)
            .setDeliveryType(delivery)
            .setClientId(id)
            .setBouquets(items)
            .build();

        console.log(order);
        try {

            const response = await axios.post('http://127.0.0.1:5000/order', order);
            /*console.log(response.data);*/
            console.log(response.data);

        } catch (error) {
            console.log(error);
        }
        dispatch(clear());
    }

    return (
        <div>
            <Header log={isUserLoggedIn} />
            <main className='profile'>
                <div className='profile__container'>
                    <div className='profile-title-block'>
                        <h1 className='profile__title'>Welcome to your profile</h1>
                    </div>
                    <button className='profile__button' onClick={logout}>Logout</button>
                    <div className='profile-info-block'>
                        <h2 className='profile__subtitle'>Your info:</h2>
                        <h3 className='profile__info'><strong>Name:</strong> {user.name}</h3>
                        <h5 className='profile__info'><strong>Email:</strong> {user.email}</h5>
                    </div>
                    {here === true ? (
                        <div className='profile-card-block'>
                            <h1 className='profile__subtitle'>Here is your card</h1>
                            <div style={{ margin: '25px auto 0' }} className={cardInfo.type}>
                                <h5>{cardInfo.type} card</h5>
                                <div>
                                    <p>{user.id}</p>
                                    <p>{cardInfo.discount}% discount</p>
                                </div>
                            </div>
                        </div>
                    ) : (
                        <div className='profile-card-block'>
                            <h1 className='profile__subtitle'>Do you still don't have our card???</h1>
                            <div>
                                <div className='profile__cards'>
                                    <div className='gold'>
                                        <h5>Gold card</h5>
                                        <div>
                                            <p>{user.id}</p>
                                            <p>5% discount</p>
                                        </div>
                                    </div>
                                    <div className='bonus'>
                                        <h5>Bonus card</h5>
                                        <div>
                                            <p>{user.id}</p>
                                            <p>10% discount</p>
                                        </div>
                                    </div>
                                    <div className='social'>
                                        <h5>Social card</h5>
                                        <div>
                                            <p>{user.id}</p>
                                            <p>15% discount</p>
                                        </div>
                                    </div>
                                </div>
                                <div className='profile__input'>
                                    <input onChange={handleOptionChange} value='gold' name='card' type='radio'></input>
                                    <input onChange={handleOptionChange} value='bonus' name='card' type='radio'></input>
                                    <input onChange={handleOptionChange} value='social' name='card' type='radio'></input>
                                </div>
                                <button onClick={handleClick} className='profile__button'>Get card</button>
                            </div>
                        </div>
                    )}
                    <div className="cart__block">
                        <h1 className="cart__title">Shopping Cart</h1>
                        <div className="cart-item__block">
                            {items.map(({ item, count }) => (
                                <ShoppingItem
                                    id={item.id}
                                    name={item.flowers[0].name}
                                    price={item.price}
                                    key={item.id}
                                />
                            ))}
                        </div>
                        {totalPrice > 0 &&
                            <select className='deliver' onChange={(e) => setDelivery(e.target.value)}>
                                {
                                    delivers.map((type) => <option key={type} value={type}>{type}</option>)
                                }
                            </select>
                        }
                        {totalPrice > 0 && !isEmptyObject(cardInfo) ? (
                            <h3 className="cart__expense">Total price with discount and delivery($50): ${(totalPrice * (1 - (cardInfo.discount / 100))) + deliveryPrice}</h3>
                        ) : (
                            totalPrice > 0 ? (
                                // Другий випадок, якщо totalPrice === 0
                                <h3 className="cart__expense">{totalPrice}</h3>
                            ) : (
                                // Третій випадок, якщо totalPrice не більше 0
                                <div></div>
                            )
                        )}
                        {totalPrice > 0 &&
                            <button onClick={createOrder} className='profile__button'>Create order</button>
                        }
                    </div>

                </div>
            </main>
        </div>
    )
}

export default UserPage;