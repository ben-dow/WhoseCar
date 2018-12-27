import React, { Component } from 'react';
import './App.css';
import {Link} from 'react-router-dom'

class App extends Component {
  render() {
    return (
        <div className="center-control" id="homepage">
            <h3>What would you like todo?</h3>
            <Link to='/NewCarpool'><button type="button" className="btn btn-primary">New Carpool</button></Link>
            <Link to='/ExistingCarpool'><button type="button" className="btn btn-primary">Existing Carpool</button></Link>

        </div>

    );
  }
}

export default App;
