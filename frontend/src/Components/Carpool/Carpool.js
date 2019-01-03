import React, { Component } from 'react';
import "./Carpool.css"
import CarpoolDisplay from "./CarpoolTools/CarpoolDisplay/CarpoolDisplay";
import * as axios from "axios";
import {Link, Redirect, Route, Switch} from 'react-router-dom';
import Login from "./CarpoolTools/Login/Login";
import Settings from "./CarpoolTools/Settings/Settings";
import Share from "./CarpoolTools/Share/Share";
import ToolSelect from "./ToolSelect";
import Cookies from "universal-cookie"

class Carpool extends Component {



    constructor(props){
        super(props);


        this.state = {
            CarpoolID : this.props.match.params.id,
            CarpoolData: null,
            isLoggedIn: false,
            ActiveComponent : "None"


        };

        this.cookies = new Cookies();
        this.checkForTokenInCookie();

        this.fetchCarpoolData = this.fetchCarpoolData.bind(this);


        this.fetchCarpoolData();
    }



    fetchCarpoolData(){
        axios({
            method: 'get',
            url: '/api/Carpool/'+this.state.CarpoolID,

        }).then(function (response) {
            this.setState({
                CarpoolData : response.data
            })
        }.bind(this)).catch(
            function (error) {
                this.setState({
                    CarpoolNotFound : true
                })
            }.bind(this)
        );

    }

    updateControlDisplay(control){

        this.setState({
            ControlTab : control
        })

    }

    checkForTokenInCookie(){
        const token = this.cookies.get('CarpoolUserToken');
        if (token == null){
            return false
        }


    }

    validateToken(token) {
        axios(
            {
                method: 'head',
                url: '/api/ValidateToken'
            }
        );
    }





    render(){

        const isLoggedIn = this.state.isLoggedIn;

        if(this.state.CarpoolNotFound){
            return (<Redirect to='/'/>)
        }

        return (
            <div id="Carpool">

                <div id="Application">
                    <div id = "title">
                        <h3>Carpool: Darien Lake</h3>
                    </div>
                    <div >
                        <h5 className="text-center">
                            <b>Description</b>
                        </h5>
                        <p className="text-center"> We are going to Darien Lake! Be sure to bring water for the day and appropriate clothing! Cost is 10$</p>
                    </div>
                    <table className="table">
                        <tbody>
                        <tr>
                            <th>Destination</th>
                            <th>Date</th>
                            <th>Time</th>
                        </tr>
                        <tr>
                            <td>
                                Darien Lake Amusement Park
                            </td>
                            <td>
                                December 10 2018
                            </td>
                            <td>
                                8:00 AM
                            </td>
                        </tr>
                        </tbody>
                    </table>

                    <div className="border border-light divider"/>

                    <Switch>
                        <Route exact path={`${this.props.match.url}`} render={(props) => <ToolSelect {...props} BaseURL={this.props.match.url} ActiveLink={"None"} LoggedIn={this.state.isLoggedIn} />}/>
                        <Route path={`${this.props.match.url}/Login`} render={(props) => <ToolSelect {...props} BaseURL={this.props.match.url} ActiveLink={"Login"} LoggedIn={this.state.isLoggedIn} />}/>
                        <Route path={`${this.props.match.url}/Display`} render={(props) => <ToolSelect {...props} BaseURL={this.props.match.url} ActiveLink={"Display"} LoggedIn={this.state.isLoggedIn} />}/>
                        <Route path={`${this.props.match.url}/Settings`} render={(props) => <ToolSelect {...props} BaseURL={this.props.match.url} ActiveLink={"Settings"} LoggedIn={this.state.isLoggedIn} />}/>
                        <Route path={`${this.props.match.url}/Share`} render={(props) => <ToolSelect {...props} BaseURL={this.props.match.url} ActiveLink={"Share"} LoggedIn={this.state.isLoggedIn} />}/>

                    </Switch>

                    <Switch>
                        <Route path={`${this.props.match.url}/Login`} render={(props) => <Login {...props} CarpoolID={this.state.CarpoolID} CarpoolData={this.state.CarpoolData} LoggedIn={this.state.isLoggedIn}   />}/>
                        <Route path={`${this.props.match.url}/Display`} render={(props) => <CarpoolDisplay {...props} CarpoolID={this.state.CarpoolID} CarpoolData={this.state.CarpoolData} LoggedIn={this.state.isLoggedIn}    />}/>
                        <Route path={`${this.props.match.url}/Settings`} render={(props) => <Settings {...props} CarpoolID={this.state.CarpoolID} CarpoolData={this.state.CarpoolData} LoggedIn={this.state.isLoggedIn}    />}/>
                        <Route path={`${this.props.match.url}/Share`} render={(props) => <Share {...props} CarpoolID={this.state.CarpoolID} CarpoolData={this.state.CarpoolData} LoggedIn={this.state.isLoggedIn} />} />

                    </Switch>


                </div>


            </div>

        );

    }

}
export default Carpool;
