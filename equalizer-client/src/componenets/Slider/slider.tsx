import React from "react";
import './slider.css'

const Slider = (props:any) => {
    const onChange = (event:any) => {
        console.log(event.target.value)
    }
    return(
        <input 
            type={"range"} 
            key={props.index} 
            min={props.minValue||0} 
            max={props.maxValue || 100}
            onChange={onChange}
        />
    )
}
export default Slider;