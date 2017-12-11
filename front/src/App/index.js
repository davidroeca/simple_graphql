import React, { Component } from 'react';
import './index.css';
import Form from './form'

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Example App</h1>
        </header>
        <p className="App-intro">
          <Form />
        </p>
      </div>
    )
  }
}

export default App
