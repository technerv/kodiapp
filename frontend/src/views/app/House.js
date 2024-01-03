import React, {useState, useEffect} from 'react';
import Axios from 'axios'
import { useNavigate } from 'react-router-dom';
import { Table, Card, Row, Col} from 'react-bootstrap';
import {Link} from 'react-router-dom';

function House() {
// create headers that will enable the user to access the bearer token, then allow the plot data to display

  const navigate = useNavigate();

  useEffect(()=>{
    if(!localStorage.getItem('token')) {
      navigate('/')
    }
  })
// View Plot Information
  const [house, setHouse] = useState([])
  // const [isLoading, setIsLoading] = useState(true)

  const getHouse = async () => {
    const response = await Axios.get(`http://127.0.0.1:8000/api/house`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${localStorage.getItem('token')}`
      }
  })
    setHouse(response.data)
  }
  
  useEffect( () => {
    getHouse();   
  }, [])

  // useEffect(() => {
  //   if(plot.length !==0){ 
  //     setIsLoading(false);
  //   }
  //   console.log(plot);
  //   setPlot(plot);
  // },[plot]);

    return (
        <>
<main>

<div className="content">
      <br />
      <Row>
        <Col>
        <Card>
      <Card.Header>
        <h4>View Houses</h4>
        <Link className="btn btn-warning" to="/addhouse">Add New House</Link>
      </Card.Header>
      <Card.Body>
          <Table stripped bordered hover size="sm">
            <thead>
            <tr>
              
              <th width="170">Plot Number</th>
              <th width="170">House Number</th>
              <th width="170">Electricity Number</th>
              <th width="170">Water Number</th>
              <th width="170">Rent Amount</th>
              <th width="170">Is Vacant</th>
              <th width="170">House Image</th>
              <th width="170">Last Updated</th>
              <th width="170">Action</th>
              
            </tr>
            </thead>

          <tbody>
          {
          house.map((house) => (
          <tr key={house.index}>
            
            <td>{house.plot_number}</td>
            <td>{house.house_number}</td>
            <td>{house.electricity_number}</td>
            <td>{house.water_number}</td>
            <td>{house.rent_amount}</td>
            <td>{house.is_vacant?"Vacant":"Occupied"}</td>
            <td><img src={house.house_image} alt={house.house_number}/> </td>
            <td>{house.date_updated}</td>
            <Link className="btn btn-warning" to={`/house/${house.id}/`}>House Detail</Link>
          </tr>

          ))
        }

          </tbody>
          </Table>
          </Card.Body>
          </Card>

        </Col>
      </Row>
        </div>
</main>
        </>
    )
}

export default House;