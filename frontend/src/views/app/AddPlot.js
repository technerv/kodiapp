import React, {useState} from 'react';
import Axios from 'axios';
import {Link} from 'react-router-dom';
import {useNavigate} from 'react-router';
import { ButtonGroup, Card, Col, Row } from 'react-bootstrap';
import {
  Form,
  FormGroup,
  Input,
} from 'reactstrap';

function AddPlot() {

    let navigate = useNavigate();
    //create state data setData
    const url=`http://127.0.0.1:8000/api/plot/create/`
    const [data, setData] = useState({
      plot_number: '',
      // phoneno: "",
      // email: ""
    })
    
    function submit(e){
      e.preventDefault();
      Axios.post(url, {
        method: 'GET', //initiate token in order to be able to post the data inside the database
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          Authorization: `Token ${localStorage.getItem('token')}`
        }
    },
    {
        plot_number: data.plot_number,
        // phoneno: data.phoneno,
        // email: data.email
      })
      .then(res=>{
        setData({
          plot_number: "",
          // phoneno: "",
          // email: ""
    })
        //console.log(res.data)
        window.alert("New Plot Added")
        navigate("/")
      })

    }

    function handle(e) {
     const newdata =  { ...data }
     newdata[e.target.id] = e.target.value
     setData(newdata)
     console.log(newdata)
    }

    //End

    return (
    <div className="content">
    <Row>
    <Col>

    </Col>
<Col>
<Card>
      <Card.Header><h4>Add New Record</h4></Card.Header>
      <Card.Body>

            <Form onSubmit={(e) => submit(e)}>
              <FormGroup>
              <Input
                name = "plot_number"
                id = "plot_number"
                value={data.plot_number}
                type="text"
                placeholder="Plot Number"
                onChange={(e)=>handle(e)}
              />

              {/* <Input
                name = "phoneno"
                id = "phoneno"
                value={data.phoneno}
                type="integer"
                placeholder="Your Phone Number"
                onChange={(e)=>handle(e)}
              />

              <Input
              name = "email"
              id = "email"
              value={data.email}
              type="email"
              placeholder="Your Email Address"
              onChange={(e)=>handle(e)}
              /> */}

              </FormGroup>
              <ButtonGroup>
              <button type='submit' className='btn btn-success'>Submit</button>
              <Link to="/" className="btn btn-danger">Cancel</Link>

              </ButtonGroup>

            </Form>
      </Card.Body>

      </Card>
</Col>
<Col>

</Col>

    </Row>

        </div>
    )
}

export default AddPlot;