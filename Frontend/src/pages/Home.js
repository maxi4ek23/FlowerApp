import React from 'react';
import Header from '../components/Header/Header';
import { useState } from 'react';
import { useEffect } from 'react';

function Home() {

  const [isUserLoggedIn, setIsUserLoggedIn] = useState(false);

  useEffect(() => {
    checkUserStatus();
  }, []);

  const checkUserStatus = () => {
    const loggedInUser = JSON.parse(localStorage.getItem('loggined_user'));
    if (loggedInUser) {
      setIsUserLoggedIn(true);
      console.log('true');
    } else {
      setIsUserLoggedIn(false);
      console.log('false');
    }
  };

  const logout = () => {
    localStorage.removeItem('loggined_user');
    setIsUserLoggedIn(false);
    console.log('false');
  }

  return (
    <div>
      <Header log={isUserLoggedIn} />
      <h1>Home Page</h1>
      <button onClick={logout}>Logout</button>
    </div>
  );
};

export default Home;