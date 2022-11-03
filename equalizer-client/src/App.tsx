import Equalizer from './pages/Equalizer/Equalizer'
import './App.css';
import Header from './componenets/Header/Header';
import Slider from "./componenets/Slider/slider";

function App() {
    return (
        <div className="App">
            <Header/>
            <Equalizer/>
            <Slider/>
            <Slider/>
            <Slider/>

        </div>
    );
}

export default App;
