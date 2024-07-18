import React, { useState } from 'react';
import './App.css';
import Logo from './Logo';

function App() {
  const [champ, setChamp] = useState({
    top: '',
    jg: '',
    mid: '',
    adc: '',
    supp: '',
    adcplayer: ''
  });

  const randomize = () => {
    fetch('/api/randomize')
      .then(response => response.json())
      .then(data => {
        setChamp(data);
      });
  };

  return (
    <div className="App">
      <header className="App-header">
      <Logo/>
        <h1>Champ Picker</h1>
      
      <randomizer className="randomizer"> 
        <button className='glow-on-hover'
        type='button'
        onClick={randomize}>Graj!</button>
        <div className="p">
          <p><strong>Top:</strong> {champ.top}</p>
          <p><strong>Jg:</strong> {champ.jg}</p>
          <p><strong>Mid:</strong> {champ.mid}</p>
          <p><strong>Adc:</strong> {champ.adc}</p>
          <p><strong>Supp:</strong> {champ.supp}</p>
          <p><strong>Adc Player:</strong> {champ.adcplayer}</p>
        </div>  
      </randomizer>
      </header>
    </div>
  );
}

export default App;
