import React, {useState, useEffect} from 'react';
// import Axios from 'axios';
// import { useNavigate } from 'react-router-dom';
import { Table, Card, Row, Col} from 'react-bootstrap';
import {Link} from 'react-router-dom';

function Plot() {

  const [data, setData] = useState([]);
  
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const url = "http://localhost:8000/api/plot"
    fetch(url, {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        Authorization: `Token ${localStorage.getItem('token')}`
      }
  })
    .then((response) => response.json())
    .then((json) => {
      setData(json)
      console.log(json, "json");
      //return json;
    }, [])
    .catch((error) => {
      console.error(error);
    })
  },[]);

  useEffect(() => {
    if(data.length !==0){
      setIsLoading(false);
    }
    console.log(data);
  },[data]);

    return (
      <div className="content">
      {/* <Dashboard /> */}
      <br />
      <Row>
        <Col>
        <Card>
      <Card.Header>
        <h4>View Records</h4>
        <Link className="btn btn-warning" to="/add">Add Plot</Link>
      </Card.Header>
      <Card.Body>
          <Table stripped bordered hover size="sm">
            <thead>
            <tr>
              
              <th width="170">Plot Number</th>
              {/* <th width="170">Email Address</th> */}
              <th width="170">Action</th>
              
            </tr>
            </thead>

          <tbody>
          { isLoading ? (<h6>Loading ... </h6>) : (
          data.map((con, index) => (
          <tr key={con.index}>
            
            <td>{con.plot_number}</td>
            {/* <td>{con.email}</td> */}
            <Link className="btn btn-warning" to={`/${con.id}/`}>Show Detail</Link>
            
          </tr>

          ))
          )}

          </tbody>
          </Table>
          </Card.Body>
          </Card>

        </Col>
      </Row>
            {/* <Footer/> */}
      </div>

    )
}

export default Plot;