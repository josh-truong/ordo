import React, { useState } from 'react';
import { useLocation } from 'react-router-dom';
import ReactTooltip from "react-tooltip";

import MovieCard from '../MovieCard/MovieCard';
import TwitterFeed from '../Tweets/TwitterFeed';
import MapChart from '../MapChart';

import MutipleCharts from '../BarChart/MutipleCharts';

const MovieOverview = () => {
    const [content, setContent] = useState("");
    const location = useLocation();
    const props = location.state.props;

    return (
        <div style={{ marginTop: '1%' }}>
            <div className='row'>
                <div className='col-sm-3'>
                    <MovieCard {...props} inOverview={true}/>
                </div>
                <div className='col-sm-9' style={{ color: '#fff' }}>
                    <div className='row'>
                        <div className='col-8' style={{ color: '#fff', backgroundColor: 'rgba(0.3,0.3,0.3,0.4)', border: '8px solid #393939' }}>
                            <h3 style={{ textAlign: 'center', fontSize: '1.5vw', marginTop: '3%' }}>
                                World Map Sentiment Analysis
                            </h3>
                            <MapChart setTooltipContent={setContent} />
                            <ReactTooltip>{content}</ReactTooltip>
                            <h3 style={{ textAlign: 'center', fontSize: '1.5vw', marginTop: '3%' }}>
                                Tweets Sentiment Analysis
                            </h3>
                            <MutipleCharts movieid={props.id}/>
                        </div>
                        <div className='col-sm-3'>
                            <TwitterFeed movieid={props.id} />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}


export default MovieOverview
