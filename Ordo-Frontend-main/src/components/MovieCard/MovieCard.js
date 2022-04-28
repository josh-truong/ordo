import React from 'react';
import { Link } from 'react-router-dom';

// Mui
import Chip from '@mui/material/Chip';

// Style
import classNames from 'classnames';
import styles from './MovieCard.module.css'

const MovieCard = (props) => {
    const container = classNames(styles.container);
    const image = classNames(styles.image);
    const middle = classNames(styles.middle);

    return (
        <Link to={'/desc'}
            state={{ props }}
        >
            <div className={container} style={props.more ? { cursor: 'pointer' } : {}}>
                <img src={props.imgURL} className={image} alt={props.title}/>
                <div className={middle} style={{ color: 'white', padding: '10px' }}>
                    <div style={{ fontSize: '20px' }}>{props.title}</div>
                    <div className='row' style={{ marginTop: '15px' }}>
                        <div className='col'>{props.year}</div>|
                        <div className='col'>{props.runningTime}m</div>|
                        <div className='col' style={{color:'#e50914'}}>{props.rating}</div>|
                        <div className='col'>{props.ratingReason}</div>
                    </div>
                    <div className='row' style={{ marginTop: '20px' }}>
                        <div className='col'>
                            {props.genres.map((genre) => {
                                return (
                                    <Chip variant="outlined" label={genre} style={{ width: 'fit-content', color: "white" }} />
                                )
                            })}
                        </div>
                    </div>
                    {
                        props.inOverview && props.morePlot != null ?
                        <div className='row' style={{ textAlign: 'left', margin: '5%', fontSize: '15px' }}>{props.morePlot}</div> :
                        <div className='row' style={{ textAlign: 'left', margin: '5%', fontSize: '15px' }}>{props.plot}</div>
                    }
                </div>
            </div>
        </Link >
    )
}



MovieCard.defaultProps = {
    more: false
}
export default MovieCard
