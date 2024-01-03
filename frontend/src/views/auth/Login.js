import axios from 'axios';
import React, {useState} from 'react';  
import { useNavigate } from 'react-router-dom';

function Login () {

  const navigate = useNavigate();

  const [values, setValues] = useState({
    email: "",
    password: "",
  });

  const handleSubmit = (e) => {
    e.preventDefault(); //prevent form errors
    axios
    .post("http://127.0.0.1:8000/api/login/", {
      username: values.email,
      password: values.password,
    })
    .then((res) => {
      console.log(res.data)
      localStorage.setItem('token', res.data.token)
      navigate('/dashboard')
      })
      .catch(error => {
        localStorage.clear()
        alert('login error')
        console.log(error)
        window.location.reload();
      })

  }  

    return (
        <div> 
    <div className="container col-xl-10 col-xxl-8 px-4 py-5">
    <div className="row align-items-center g-lg-5 py-5">
      <div className="col-lg-7 text-center text-lg-start">
        <h1 className="display-4 fw-bold lh-1 mb-3">Welcome To Kodi</h1>
        <p className="col-lg-10 fs-4">Kodi Gives You The Right Tools To Manage Your Property Data Easily. </p>
      </div>
      <div className="col-md-10 mx-auto col-lg-5">
        <form onSubmit={handleSubmit} className="p-4 p-md-5 border rounded-3 bg-light">
        {/* <p>{formErrors.email}</p> */}
          <div className="form-floating mb-3">
            <input 
            autoComplete='off'
            type="email" 
            // value={formValues.email}
            onChange={(e)=>setValues({...values,email:e.target.value})}
            className="form-control" 
            placeholder="Enter Email Address"
            />
            <label for="floatingInput">Email address</label>
          </div>
          <div className="form-floating mb-3">
          {/* <p>{formErrors.password}</p> */}
            <input 
            autoComplete='off'
            type="password" 
            // value={formValues.password}
            onChange={(e)=>setValues({...values,password:e.target.value})}
            className="form-control" 
            placeholder="Enter Password" 
            />
            <label for="floatingPassword">Password</label>
          </div>
          <div className="checkbox mb-3">
            <label>
              <input type="checkbox" value="remember-me" /> Remember me
            </label>
          </div>
          <button  className="w-100 btn btn-lg btn-primary" type="submit">Login</button>
          <hr className="my-4" />
          <small className="text-muted">No Account? <a href='signup'>Sign Up Here.</a></small>
        </form>
      </div>
    </div>
  </div>
        </div>
        
    )
}

export default Login;