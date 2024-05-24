
import './Header.css';
import Home from '../../pages/Home';
import Catalog from '../../pages/Catalog';
import Login from '../../pages/Login';
import {NavLink, Route, Routes } from "react-router-dom";
import Logo from '../../images/logo_flo.png';
import { useNavigate } from "react-router-dom";



function Header() {
    const selected = 'active-item';
    const navigate = useNavigate();
    return (
        <div>
            <header className="header">
                <div className="header-container">
                    <NavLink to='/'>
                        <div className="header__logo">
                            <img src={Logo} alt="logo"/>
                        </div>
                    </NavLink>
                    <nav className="header__items">
                        <ul>
                            <li className="header__item">
                                <NavLink  to='/' end className={({ isActive }) => isActive ? selected : undefined}>Home</NavLink>
                            </li>
                            <li className="header__item">
                                <NavLink  to='/catalog' className={({ isActive }) => isActive ? selected : undefined}>Catalog</NavLink>
                            </li>
                        </ul>
                    </nav>
                    <div className='button__block'>
                        <button className='login__button' onClick={() => navigate('/login')}>Login</button>
                    </div>
                </div>
            </header>
        </div>
    );
};


export default Header;