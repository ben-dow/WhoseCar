import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import * as serviceWorker from './serviceWorker';
import {BrowserRouter as Router,Route,Switch,Redirect} from "react-router-dom";
import App from "./App";
import Carpool from "./Components/Carpool/Carpool";
import NewCarpool from "./Components/Setup/NewCarpool";
import Login from "./Components/Authorization/Login";
import Logout from "./Components/Authorization/Logout";
import ExistingCarpool from "./Components/Setup/ExistingCarpool";
import WhoseMyRideHeader from "./Components/util/WhoseMyRideHeader";

ReactDOM.render(
    <div>
    <WhoseMyRideHeader/>
    <Router>
        <Switch>
            <Route exact path="/" component={App}/>
            <Route exact path="/Carpool/">
                <Redirect to="/"/>
            </Route>
            <Route path="/Carpool/:id" component={Carpool}/>
            <Route exact path="/NewCarpool" component={NewCarpool}/>
            <Route exact path="/ExistingCarpool" component={ExistingCarpool}/>
            <Route exact path="/Login" component={Login}/>
            <Route exact path="/Logout" component={Logout}/>


        </Switch>
    </Router>
    </div>
    , document.getElementById('root'));


// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
