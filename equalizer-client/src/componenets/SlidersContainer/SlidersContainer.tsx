import React from 'react'
import './SlidersContainer.css'
import { SlidersData } from './Data/SlidersData';
import Slider from '../Slider/slider';

const SlidersContainer = (props:any) => {
    let counter = -1

    return(
        SlidersData[props.Mode].map((slider:any) => {
            counter++;
            console.log(counter)
            return <Slider
                        index = {counter}
                        minValue = {slider.minValue}
                        maxValue = {slider.maxValue}
                    />
        })
    )
    
}


export default SlidersContainer;