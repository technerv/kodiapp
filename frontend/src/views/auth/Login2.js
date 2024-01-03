import React, { useState } from 'react';

function Login() {

    const adminUser = {
        email: "admin@technerv.com",
        password: "newdream"
    }

    const [user, setUser] = useState({email:"", password: ""});
    const [error, setError] = useState("");

    const loginUser = (user) => {
        console.log();

        if (user.email == adminUser.email && user.password == adminUser.password) {
            console.log("Logged In");
        } else {
            console.log("Details do not match")
        }
    }

    const logoutUser = () => {
        console.log("Logout")
    }

    const submitHandler = (e) => {
        e.preventDefault();
        console.log(user);

        setUser(user)

    }

  return (
    <div className='App'>
        {(user.email !="") ? (
            <div className='welcome'>
                <h2>Welcome, <span>{user.email}</span></h2>
                <button>Logout</button>
            </div>
        ) : (
          <form onSubmit={submitHandler}>
            <h2>Login</h2>
            <input type="email" name="email" id="name" onChange={e => setUser({...user, email: e.target.value})} value={user.email} />
            <input type="password" name="password" id="name" onChange={e => setUser({...user, password: e.target.value})} value={user.password} />

          </form>


            
        )}
    </div>
  )
}

export default Login