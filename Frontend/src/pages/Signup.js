import React from 'react';
import './Signup.css';
import Icon, {
    UserOutlined,
    LockOutlined,
    WomanOutlined
} from "@ant-design/icons";
import { NavLink } from 'react-router-dom';
import { useState } from 'react';
import axios from 'axios';
import { useNavigate } from "react-router-dom";



function Signup() {

    const navigate = useNavigate();

    const [formData, setFormData] = useState({
        name: '',
        email: '',
        password: '',
        is_admin: false,
    });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const press = async () => {
        try {
            
            const response = await axios.post('http://127.0.0.1:5000/user', formData);
            /*console.log(response.data);*/
            console.log(response.data);
            navigate('/login')

            // Додаткові дії після успішної реєстрації користувача
        } catch (error) {
            console.log(error);
            if(error.response.data === 'User with this email already exists') {
                alert(error.response.data);
            }
            // Обробка помилок
        }
    };

    return (
        <div className='signup__page'>
            <div className='signup__form'>
                <h1>Sign up</h1>
                <form>
                    <div className='input__block'>
                        <div className='input__field'>
                            <Icon className='icon' component={WomanOutlined} />
                            <input onChange={handleChange} name='name' type='text' placeholder='Name'></input>
                        </div>
                        <div className='input__field'>
                            <Icon className='icon' component={UserOutlined} />
                            <input onChange={handleChange} name='email' type='text' placeholder='Email'></input>
                        </div>
                        <div className='input__field'>
                            <Icon className='icon' component={LockOutlined} />
                            <input onChange={handleChange} name='password' type='password' placeholder='Password'></input>
                        </div>
                        <p>You already have an account? <NavLink to='/login'>Login</NavLink></p>
                    </div>
                </form>
                <button onClick={press} className='input__btn'>Sign up</button>
            </div>
        </div>
    );
};

export default Signup;