import React from 'react'
import { CircularProgressbar } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';


const BarChart = ({ value, sentiment }) => {
    return (
        <div>
            <div className='row' style={{ textAlign: 'center', fontSize: '20px' }}>
                <span>{sentiment}</span>
            </div>
            <div className='row'>
                <CircularProgressbar
                    value={value}
                    text={`${value}%`}
                />
            </div>
        </div>
    )
}

export default BarChart
