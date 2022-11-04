import React from "react";
import Graph from "../../componenets/Graph/Graph";
import SlidersContainer from "../../componenets/SlidersContainer/SlidersContainer";
import './Equalizer.css'

const Equalizer = () => {
    return(
        <>
        <div className="graph-container">
            <Graph />
        </div>
        <div className="sliders-container">
            <SlidersContainer Mode={0}/>
        </div>
        </>
    )
}

export default Equalizer;