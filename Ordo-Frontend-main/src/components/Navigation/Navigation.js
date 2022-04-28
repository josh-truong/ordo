import React from 'react'
import { Link } from 'react-router-dom';

import { Box, Grid, Typography } from '@mui/material';

const Navigation = () => {
    return (
        <div style={{ color: 'white', backgroundColor: 'rgba(0,0,0,.75)' }}>
            <Box sx={{ mt: 1, ml: 5, mr: 5 }}>
                <Grid container wrap="nowrap" spacing={2} alignItems="center">
                    <Grid item xs={3}>
                        <Link to='/' style={{ textDecoration: 'none', color: 'white' }}>
                            <Typography style={{ overflowWrap: 'word-break' }} variant="h3" color="#e50914">Ordo</Typography>
                        </Link>
                    </Grid>
                    <Grid item xs={6}></Grid>
                    <Grid item xs={3}>
                        <Grid container wrap="nowrap" spacing={5}>
                            <Grid item xs={4}></Grid>
                            <Grid item xs={4}>
                                <Link to='/' style={{ textDecoration: 'none', color: 'white' }}>
                                    <Typography style={{ overflowWrap: 'word-break' }}>HOME</Typography>
                                </Link>
                            </Grid>
                            <Grid item xs={4}></Grid>
                        </Grid>
                    </Grid>
                </Grid>
            </Box>
        </div>
    )
}

export default Navigation
