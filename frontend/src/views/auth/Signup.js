import React from 'react';
// import { useNavigate } from 'react-router-dom';

function Signup () {
//     const navigate = useNavigate();

//     useEffect(()=>{
//       if(!localStorage.getItem('token')) {
//         navigate('/')
//       }
//     }, [])

    return (
        <>       
    
        <div className='Auth-form-container'>
            
            <form className='Auth-form'>
                <div className='Auth-form-content'>
                <h3 className='Auth-form-title'>SIGN UP TO KODI</h3>
                    <div className='form-group mt-3'>
                        <label>Salutation</label>
                        <select class="form-select" aria-label="Default select example">
                        <option selected>Select Salutation</option>
                        <option value="1">Mr</option>
                        <option value="2">Mrs</option>
                        <option value="3">Miss</option>
                        </select>
                    </div>
                    <div className='form-group mt-3'>
                        <label>First Name</label>
                        <input
                        type='text'
                        className='form-control mt-1'
                        placeholder='Enter Your First Name'
                        /> 
                    </div>
                    <div className='form-group mt-3'>
                        <label>Last Name</label>
                        <input
                        type='text'
                        className='form-control mt-1'
                        placeholder='Enter Your Last Name'
                        /> 
                    </div>
                    <div className='form-group mt-3'>
                        <label>Email Address</label>
                        <input
                        type='email'
                        className='form-control mt-1'
                        placeholder='Enter Your Email Address'
                        /> 
                    </div>
                    <div className='form-group mt-3'>
                        <label>Phone Number</label>
                        <input
                        type='text'
                        className='form-control mt-1'
                        placeholder='Enter Your Phone Number'
                        /> 
                    </div>
                    <div className='form-group mt-3'>
                        <label>Gender</label>
                        <select class="form-select" aria-label="Default select example">
                        <option selected>Select Gender</option>
                        <option value="1">Male</option>
                        <option value="2">Female</option>
                        </select>
                    </div>
                    <div className='form-group mt-3'>
                        <label>Account Type</label>
                        <select class="form-select" aria-label="Default select example">
                        <option selected>Select Account Type</option>
                        <option value="1">Tenant</option>
                        <option value="2">Owner</option>
                        </select>
                    </div>
                    <div className='form-group mt-3'>
                        <label>Password</label>
                        <input
                        type='password'
                        className='form-control mt-1'
                        placeholder='Enter Your Password'
                        /> 
                    </div>
                    <div className='d-grid gap-2 mt-3'>
                        <button type='submit' className='btn btn-primary'>Sign Up</button>
                    </div>
                    <p className='forgot-password text-right mt-2'>
                    </p>
                </div>
            </form>
            
        </div>
        </>
        
    )
}

export default Signup;