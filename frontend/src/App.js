import React from 'react';
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import './App.css';
import Login from './views/auth/Login';
import Signup from './views/auth/Signup';
import Logout from './views/auth/Logout';
import Dashboard from './views/app/Dashboard'
import Plot from './views/app/Plot';
import AddPlot from './views/app/AddPlot';
// import PlotDetail from './views/app/PlotDetail';
// import UpdatePlot from './views/app/UpdatePlot';
// import House from './views/app/House';
// import AddHouse from './views/app/AddHouse';
// import HouseDetail from './views/app/HouseDetail';
// import Tenant from './views/app/Tenant';
import Footer from './components/layout/Footer';
import Navigation from './components/layout/Navigation';

// import AddTenant from './views/app/AddTenant';

function App() {
  return (
    <>
    <Navigation />
    
    <BrowserRouter>
    <Routes>
      {/* Login */}
      <Route path='/' element={<Login />} /> 
      <Route path='/signup' element={<Signup />} />
      <Route path='/logout' element={<Logout />} />

      {/* Dashboard */}
      <Route path='/dashboard' element={<Dashboard />} />

      {/* Plot */}
      <Route exact path='/plot' element={<Plot />} />
      <Route exact path='/add' element={<AddPlot />} />
      {/* <Route path='/plot/:id/' element={<PlotDetail />}/> */}
      {/* <Route path='/:id/update/' element={<UpdatePlot />}/> */}

      {/* House */}
      {/* <Route path='/house' element={<House />} /> */}
      {/* <Route path='/addhouse' element={<AddHouse />} /> */}
      {/* <Route path='/house/:id/' element={<HouseDetail />}/> */}
      {/* <Route path='/:id/update/' element={<UpdatePlot />}/>      */}
      
      {/* Tenant */}
      {/* <Route path='/tenant' element={<Tenant />} /> */}
      {/* <Route path='/addtenant' element={<AddTenant />}/> */}
    
    </Routes>   
    </BrowserRouter>
    <Footer />
   </>
  )
}

export default App;
