import React from 'react'

const Footer = () => {
    return (
        <div style={{height:'20px',position:'relative',textAlign:"center",color:'white'}}>
            <footer style={{ backgroundColor:'#f3f3f3' }} className="d-flex justify-content-center">
                <div className='row' style={{ position: 'absolute', top: '50%', marginTop:'15px' }}>
                    <div className='col' style={{ margin: '15px', whiteSpace: 'nowrap' }}>COPYRIGHT &copy; {new Date().getFullYear()} Team ORDO. All Rights Reserved.</div>
                </div>
            </footer>
        </div>
    )
}

export default Footer
