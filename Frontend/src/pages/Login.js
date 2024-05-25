import React from 'react';
import './Login.css';
import Icon, {
  UserOutlined,
  LockOutlined
} from "@ant-design/icons";
import { NavLink } from 'react-router-dom';

function Login() {

  const handle = () => {
    console.log('11');
  }

  return (
    <div className='login__page'>
      <div className='login__form'>
        <h1>Login</h1>
        <form onSubmit={handle}>
          <div className='input__block'>
            <div className='input__field'>
              <Icon className='icon' component={UserOutlined} />
              <input type='text' placeholder='Email'></input>
            </div>
            <div className='input__field'>
              <Icon className='icon' component={LockOutlined} />
              <input type='password' placeholder='Password'></input>
            </div>
            <p>You don`t have an account? <NavLink to='/signup'>Sigh up</NavLink></p>
          </div>
          <button type='submit' className='input__btn'>Login</button>
        </form>
      </div>

    </div>
  );
};

export default Login;