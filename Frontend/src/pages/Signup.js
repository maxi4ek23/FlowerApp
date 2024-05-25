import React from 'react';
import './Signup.css';
import Icon, {
    UserOutlined,
    LockOutlined,
    WomanOutlined
} from "@ant-design/icons";
import { NavLink } from 'react-router-dom';



function Signup() {
    return (
        <div className='signup__page'>
            <div className='signup__form'>
                <h1>Sign up</h1>
                <form>
                    <div className='input__block'>
                    <div className='input__field'>
                            <Icon className='icon' component={WomanOutlined} />
                            <input type='text' placeholder='Name'></input>
                        </div>
                        <div className='input__field'>
                            <Icon className='icon' component={UserOutlined} />
                            <input type='text' placeholder='Email'></input>
                        </div>
                        <div className='input__field'>
                            <Icon className='icon' component={LockOutlined} />
                            <input type='password' placeholder='Password'></input>
                        </div>
                        <p>You already have an account? <NavLink to='/login'>Login</NavLink></p>
                    </div>
                </form>
                <button className='input__btn'>Sign up</button>
            </div>
        </div>
    );
};

export default Signup;