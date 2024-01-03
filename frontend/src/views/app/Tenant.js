import React, { useState, useEffect } from 'react';
import Axios from 'axios';
import { useNavigate } from 'react-router-dom';

function Tenant() {

  const navigate = useNavigate();

  useEffect(()=>{
    if(!localStorage.getItem('token')) {
      navigate('/')
    }
  })

  const [data, setData] = useState([]);
  const [isLoading, setIsLoading] = useState(true)
  // data state // storage

  useEffect( () => {
    Axios.get("http://127.0.0.1:8000/apis/tenants")
    .then((res) => setData(res.data));
  }, [])


  useEffect(() => {
    if(data.length !==0){
      setIsLoading(false);
    }
    console.log(data);
  },[data]);

    return (
        <>   
       <main>
{/* <section class="py-5 text-center container">
  <div class="row py-lg-5">
    <div class="col-lg-6 col-md-8 mx-auto">
      <h1 class="fw-light">View Tenant Data</h1>
    </div>
  </div>
</section> */}
            <div class="album py-5 bg-light">
  <div class="container">
  <button type="button" class="btn btn-warning" data-bs-toggle="modal" data-bs-target="#exampleModal">
  Add New Tenant
</button>


<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">

<div class="modal-dialog modal-dialog-scrollable">
<form>
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Add New Tenant Information</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
      <div class="mb-3">
    <label for="exampleInputText1" class="form-label">Tenant Name</label>
    <input type="text" class="form-control" id="exampleInputText1" aria-describedby="textHelp" />
  </div>      
  <div class="mb-3">
    <label for="exampleInputText1" class="form-label">House Number</label>
    <input type="text" class="form-control" id="exampleInputText1" aria-describedby="textHelp" />
  </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save Tenant</button>
        <br/>
      </div>
    </div>
    </form>
</div>
</div> <br/><br/>

<div class="modal fade" id="updateModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">

<div class="modal-dialog modal-dialog-scrollable">
<form>
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Update Tenant Information</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
      <div class="mb-3">
    <label for="exampleInputText1" class="form-label">Tenant Name</label>
    <input type="text" class="form-control" id="exampleInputText1" aria-describedby="textHelp" />
  </div>      
  <div class="mb-3">
    <label for="exampleInputText1" class="form-label">House Number</label>
    <input type="text" class="form-control" id="exampleInputText1" aria-describedby="textHelp" />
  </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Update Tenant</button>
        <br/>
      </div>
    </div>
    </form>
</div>
</div> <br/><br/>

    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">

    { isLoading ? (<div class="d-flex align-items-center">
  <strong>Loading...</strong>
  <div class="spinner-border ms-auto" role="status" aria-hidden="true"></div>
</div>) : (
          data.map((con, index) => (
          
          <div key={con.index}>

      <div class="col">
        <div class="card shadow-sm">
        <div class="card-header"> Tenant: <b>{con.tenant_name}</b></div>
          <div class="card-body">
            <p class="card-text">House Number: <b>{con.houseNo}</b><br /> </p>
            <div class="d-flex justify-content-between align-items-center">
              <div class="btn-group">
                <button type="button" data-bs-toggle="modal" data-bs-target="#updateModal" class="btn btn-sm btn-outline-success">Update</button>
                <button type="button" class="btn btn-sm btn-outline-danger">Delete</button>
              </div>
              <small class="text-muted">{con.date_updated}</small>
            </div>
          </div>
        </div>
      </div>           
    </div>
      ))
      )}

  </div>
  
</div>
</div> 

        

</main>
        </>
    )
}

export default Tenant;