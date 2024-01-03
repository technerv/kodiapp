import React, { useEffect, useState, Fragment } from "react";
import {Nav, Navbar} from 'react-bootstrap'

function Navigation() {

  const [isAuth, setIsAuth] = useState(false);

  useEffect(() => {
    if (localStorage.getItem('token') !== null) {
      setIsAuth(true);
    }
  }, []);

  const handleClick = () => {
    localStorage.clear();
    window.location.reload();
  }
    return(
      <>
<nav class="navbar navbar-dark bg-dark">
  {isAuth === true ? (

    <Fragment>
      {''}   
      <div class="container-fluid">
  <Navbar bg="myRed" variant="dark" sticky="top" expand="sm" collapseOnSelect>
  <a href ="/"> <Navbar.Brand>
      </Navbar.Brand></a>
      <Navbar.Toggle />
      <Navbar.Collapse>
      <Nav>
      {/* <div class="nav-link px-3">Welcome</div> */}
        {/* <Nav.Link href='dashboard'>Dashboard</Nav.Link> */}
        <Nav.Link href='plot'>View Plots</Nav.Link>
        <Nav.Link href='house'>View Houses</Nav.Link>
        <Nav.Link href='tenant'>View Tenants</Nav.Link>
      </Nav>
      </Navbar.Collapse>
      </Navbar>
      <div class="navbar-nav">
    <div class="nav-item text-nowrap">
      <button 
      type="button" 
      class="btn btn-sm btn-outline-danger" 
      onClick={handleClick}>Logout</button>
    </div>
  </div>
  </div>
    </Fragment>
  ):(
    <Fragment>
      {''}
      <div class="nav-item text-nowrap">
      <button 
      type="button" 
      class="btn btn-sm btn-outline-danger" 
      >Signup</button>
    </div>
    </Fragment>
  )}
  
</nav>
      </>
    )
}

export default Navigation;