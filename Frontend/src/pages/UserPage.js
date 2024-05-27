import React from 'react';
import Header from '../components/Header/Header';
import './UserPage.css';
import { useState } from 'react';
import { useEffect } from 'react';
import { useNavigate, useParams } from "react-router-dom";
import axios from 'axios';

function UserPage() {

    const [isUserLoggedIn, setIsUserLoggedIn] = useState(false);
    const [user, setUser] = useState({});
    const { id } = useParams();

    useEffect(() => {
        checkUserStatus();
        findUser();
    }, []);

    const checkUserStatus = () => {
        const loggedInUser = JSON.parse(localStorage.getItem('loggined_user'));
        if (loggedInUser) {
            setIsUserLoggedIn(true);
        } else {
            setIsUserLoggedIn(false);
        }
    };

    const findUser = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:5000/user/${id}`);
            console.log(response.data);
            setUser(response.data);
          } catch (error) {
            console.log(error);
          }
    }

    return (
        <div>
            <Header log={isUserLoggedIn} />
            <main className='profile'>
                <div className='profile__container'>
                    <div className='profile-title-block'>
                        <h1 className='profile__title'>Welcome to your profile</h1>
                    </div>
                    <div className='profile-info-block'>
                        <h2>Your info:</h2>
                        <h3>Name: {user.name}</h3>
                        <h5>Email: {user.email}</h5>
                    </div>
                    <div className='profile-card-block'>

                    </div>
                    <div className='profile-order-block'>

                    </div>

                </div>
            </main>
        </div>
    )
}

export default UserPage;