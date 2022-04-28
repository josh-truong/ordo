import React, { useState, useEffect } from 'react';
import CustomTweet from './CustomTweet'

import { Typography } from '@mui/material';


const TwitterFeed = ({movieid}) => {
  const [tweets, setTweets] = useState([]);
  useEffect(() => {
    fetch(`https://lyrical-cacao-345508.uc.r.appspot.com/tweets?movieId=${movieid}`)
      .then(res => res.json())
      .then(
        (result) => {
          setTweets(result);
        },
        (error) => { console.log(error) }
      )
  }, []);


  return (
    <div style={{ width: '40vh', height: 'auto', margin: '0 1% 1% 1%', float: 'center' }}>
      <Typography variant='h5'>Twitter Review's</Typography>
      <div style={{ height: '90vh', overflow: 'auto' }}>
        {
          tweets.map((tweet) => (
            <CustomTweet tweet={tweet.TWEETID} key={tweet.TWEETID}/>
          ))
        }
      </div>
    </div>
  )
}

export default TwitterFeed


