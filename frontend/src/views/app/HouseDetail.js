import Axios from 'axios'
import React, {useState, useEffect} from 'react'
import { useParams } from 'react-router-dom'

const HouseDetail = () => {

    const [house, setHouse] = useState("")

    const {id} = useParams();

    const getSingleHouse = async () => {
        const {data} = await Axios.get(`http://127.0.0.1:8000/api/house/${id}/`)
        console.log(data)
        setHouse(data)
    }

    useEffect(() => {
        getSingleHouse();
    }) // Get Single House API call 

  return (
    <>
    <div>House Detail</div>
    <p>{house.plot_number}</p>
    <img src='{house.house_image}' alt='plot' height="200" width="300" />
    </>
  )
}

export default HouseDetail;