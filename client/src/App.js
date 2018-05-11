import React, { Component } from 'react';
import './App.css';
import axios from 'axios';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      cryptos: []
    };
  }
  componentDidMount() {
    axios.get('http://localhost:5000/api/v1/ticker/price', {})
      .then(res => {
        const data = res.data;
        console.log(data)
        const cryptos = []
        for (var key in data) {
          cryptos.push(data[key])
        }
        this.setState({cryptos: cryptos});
      })
  }
  render() {
    return (
      <div className="App">
        <ul>
          {this.state.cryptos.map(function(ticker) {
            return <li>{ticker.symbol} : {ticker.timestamp} : {ticker.last}</li>; 
          })}
        </ul>
      </div>
    );
  }
}

export default App;
