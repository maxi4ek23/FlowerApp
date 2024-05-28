
import './Header.css';
import { NavLink } from "react-router-dom";
import Logo from '../../images/logo_flo.png';
import { useNavigate } from "react-router-dom";
import { useState } from 'react';
import { useEffect } from 'react';



function Header({ log }) {
    const selected = 'active-item';
    const navigate = useNavigate();

    /*const [isUserLoggedIn, setIsUserLoggedIn] = useState(log);

    useEffect(() => {
        checkUserStatus();
    }, []);

    const checkUserStatus = () => {
        const loggedInUser = JSON.parse(localStorage.getItem('loggined_user'));
        if (loggedInUser) {
            setIsUserLoggedIn(true);
        } else {
            setIsUserLoggedIn(false);
        }
    };*/


    return (
        <div>
            <header className="header">
                <div className="header-container">
                    <NavLink to='/'>
                        <div className="header__logo">
                            <img src={Logo} alt="logo" />
                        </div>
                    </NavLink>
                    <nav className="header__items">
                        <ul>
                            <li className="header__item">
                                <NavLink to='/' end className={({ isActive }) => isActive ? selected : undefined}>Home</NavLink>
                            </li>
                            <li className="header__item">
                                <NavLink to='/catalog' className={({ isActive }) => isActive ? selected : undefined}>Catalog</NavLink>
                            </li>
                        </ul>
                    </nav>
                    {
                        log ? (
                            <div className='header__profile'>
                                <NavLink to={`/user/${JSON.parse(localStorage.getItem('loggined_user')).id}`} className={({ isActive }) => isActive ? selected : undefined}>Profile</NavLink>
                            </div> 
                        ) : (
                            <div className='button__block'>
                                <button className='login__button' onClick={() => navigate('/login')}>Login</button>
                            </div>
                        )
                    }
                </div>
            </header>
        </div>
    );
};


export default Header;