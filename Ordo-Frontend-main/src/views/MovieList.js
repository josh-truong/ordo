import React, { useState, useEffect } from 'react'
import MovieCard from '../components/MovieCard/MovieCard'

const MovieList = () => {
    const [items, setItems] = useState([]);
    useEffect(() => {
        fetch("https://lyrical-cacao-345508.uc.r.appspot.com/movies")
            .then(res => res.json())
            .then(
                (result) => {
                    setItems(result);
                },
                (error) => { console.log(error) }
            )
    }, []);

    return (
        <div className='row'>
            {
                items.reverse().map((item) => (
                    <div className='col-12 col-sm-6 col-md-4 col-lg-3' style={{marginTop:'15px'}} key={item.MOVIEID}>
                        <MovieCard 
                            title={item.TITLE}
                            year={item.YEAR}
                            imgURL={item.IMGURL}
                            releaseDate={item.RELEASEDATE}
                            runningTime={item.runningtime}
                            rating={`${item.ORDORATING}/10`}
                            ratingReason={item.RATING}
                            genres={item.GENRES.replaceAll("'", '').split(',')}
                            plot={item.PLOTOUTLINE}
                            morePlot={item.PLOT}
                            more={true}
                            id={item.MOVIEID}
                        />
                    </div>
                ))
            }
        </div>
    )
}

export default MovieList
