import React from 'react';
import './Login.css';
import Icon, {
  UserOutlined,
  LockOutlined
} from "@ant-design/icons";
import { NavLink } from 'react-router-dom';
import { useState } from 'react';
import axios from 'axios';
import { useNavigate } from "react-router-dom";

function Login() {

  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    email: '',
    password: '',
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const press = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/user/login', formData);
      /*console.log(response.data);*/
      console.log(response.data);
      console.log(localStorage.getItem('lol'));
      /*localStorage.setItem('loggined_user', response.data);*/
      console.log(localStorage.length);
      navigate('/catalog');
    } catch (error) {
      console.log(error);
      if (error.response.data === 'Object not found') {
        alert(error.response.data);
      }
    }
  }

  return (
    <div className='login__page'>
      <div className='login__form'>
        <h1>Login</h1>
        <form>
          <div className='input__block'>
            <div className='input__field'>
              <Icon className='icon' component={UserOutlined} />
              <input onChange={handleChange} name='email' type='text' placeholder='Email'></input>
            </div>
            <div className='input__field'>
              <Icon className='icon' component={LockOutlined} />
              <input onChange={handleChange} name='password' type='password' placeholder='Password'></input>
            </div>
            <p>You don`t have an account? <NavLink to='/signup'>Sigh up</NavLink></p>
          </div>
        </form>
        <button onClick={press} className='input__btn'>Login</button>
      </div>
    </div>
  );
};

export default Login;