import Axios from 'axios'
import React, {useState, useEffect} from 'react'
import { useParams } from 'react-router-dom'

const PlotDetail = () => {

    const [plot, setPlot] = useState("")

    const {id} = useParams();

    const getSinglePlot = async () => {
        const {data} = await Axios.get(`http://127.0.0.1:8000/api/plot/${id}/`, {
          method: 'GET',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            Authorization: `Token ${localStorage.getItem('token')}`
          }
      })
        console.log(data)
        setPlot(data)
    }

    useEffect(() => {
        getSinglePlot();
    }) // Get Single Plot API call 

  return (
    <>
    <div>PlotDetail</div>
    <p>{plot.plot_number}</p>
    <img src='{plot.plot_image}' alt='plot' height="200" width="300" />
    </>
  )
}

export default PlotDetail;