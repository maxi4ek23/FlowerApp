import React from 'react';
import './Login.css';
import Icon, {
  UserOutlined,
  LockOutlined
} from "@ant-design/icons";
import { NavLink } from 'react-router-dom';

function Login() {

  const obj = {
    name: 'm',
    surname: 'p'
  }

  const handle = () => {
    console.log('11');
    console.log(obj);
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
        </form>
        <button onClick={handle} className='input__btn'>Login</button>
      </div>
    </div>
  );
};

export default Login;