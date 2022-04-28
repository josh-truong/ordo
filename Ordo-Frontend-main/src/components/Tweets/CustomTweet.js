import React, { useState } from 'react'
import { Tweet } from 'react-twitter-widgets'
import './style.css'

const CustomTweet = ({ tweet }) => {
    const [loading, setLoading] = useState(true);
    return (
        <div key={tweet}>
            <Tweet tweetId={tweet} onLoad={() => setLoading(false)} />
            {loading ?
                <div className="spinner-container"  style={{ textAlign:'center' }}>
                    <div className="loading-spinner" style={{ display: 'block', marginRight: 'auto', marginLeft: 'auto' }} />
                    <div className='animate-flicker'>Loading</div>
                </div> : ''}
        </div>
    )
}

export default CustomTweet
