import React, { useState, useEffect } from 'react';
import BarChart from '.';
const MutipleCharts = ({movieid}) => {
    const [items, setItems] = useState([]);

    useEffect(() => {
        fetch(`https://lyrical-cacao-345508.uc.r.appspot.com/movie_tweet_percentage?movieId=${movieid}`)
            .then(res => res.json())
            .then(
                (result) => {
                    setItems(result);
                },
                (error) => { console.log(error) }
            )
    }, []);

    const pos = items['positive percentage'];
    const neu = items['neutral percentage'];
    const neg = items['negative percentage'];
    return (
        <div className='row' style={{ marginBottom: '5%' }}>
            <div className='col'>
                <BarChart value={pos} sentiment='Postive' />
            </div>
            <div className='col'>
                <BarChart value={neu} sentiment='Neutral' />
            </div>
            <div className='col'>
                <BarChart value={neg} sentiment='Negative' />
            </div>
        </div>
    )
}

export default MutipleCharts
