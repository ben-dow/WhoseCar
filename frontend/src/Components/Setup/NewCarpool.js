import React, {Component} from 'react'
import "./NewCarpool.css"
import {Link, Redirect} from 'react-router-dom'
const axios = require('axios');




class NewCarpool extends Component {

    constructor(props) {
        super(props);
        this.state = {
            error: false,
            errorText : ""
        }


        this.handleInputChange = this.handleInputChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleInputChange(event) {
        const target = event.target;
        const value = target.value;
        const name = target.name;

        this.setState({
            [name] : value
        });

    }

    handleSubmit() {

        // Prepare Data

        const dateFormating = this.state.dateOfCarpool + " " + this.state.timeOfCarpool;


        const SubmitData = {
            CarpoolName : this.state.CarpoolName,
            Destination : this.state.Destination,
            Description : this.state.Description,
            Datetime : dateFormating
        }


        axios({
            method: 'post',
            url: '/api/Carpool',
            data: SubmitData
        }).then(
            function (response) {
                this.setState({
                    id : response['data']['id'],
                    redirectToCarpool : true
            })
            }.bind(this)
        ).catch(
            function(error){
                const status = error.response.status

                if(status === 400){
                    this.setState({
                        error : true,
                        errorText : "Bad Form Data"
                    })
                }
                else {
                    this.setState({
                        error: true,
                        errorText: "Lost Connection to API Server"

                    })
                }
            }.bind(this));
    }



    render() {

        if(this.state.redirectToCarpool){
            const carpoolURL = "/Carpool/" + this.state.id;
            return <Redirect to={carpoolURL}/>
        }


        return (
            <div className="center-control" id="NewCarpool">
                {this.state.error &&

                    <div className="alert alert-danger" role="alert">
                        {this.state.errorText}
                    </div>
                }

                <Link to="/" className="link">Back to Home</Link>

                <form >
                    <div className="form-group row">
                        <input name="CarpoolName" onChange={this.handleInputChange} id="carpoolName" className="form-control" type="text" placeholder="Carpool Name" required/>
                        <small id="passwordHelpBlock" className="form-text text-muted">
                            The Name of Your Carpool
                        </small>
                    </div>
                    <div className="form-group row">
                        <input name="Destination" onChange={this.handleInputChange} id="destination" type="text" className="form-control" placeholder="Destination" required/>
                        <small id="passwordHelpBlock" className="form-text text-muted">
                            The Destination of the Carpool
                        </small>
                    </div>
                    <div className="form-group row">
                        <input name="Description" onChange={this.handleInputChange} id="description" type="text" className="form-control" placeholder="Description" required/>
                        <small id="passwordHelpBlock" className="form-text text-muted">
                            The Description of your Event
                        </small>
                    </div>
                    <div className="form-group row">
                        <input name="dateOfCarpool" onChange={this.handleInputChange} id="date" type="Date" className="form-control" placeholder="Date" required/>
                        <small id="passwordHelpBlock" className="form-text text-muted">
                            The Date of your Event
                        </small>
                    </div>

                    <div className="form-group row">
                        <input name="timeOfCarpool" onChange={this.handleInputChange} id="time" type="Time" className="form-control" placeholder="time"/>
                        <small id="passwordHelpBlock" className="form-text text-muted">
                            The time you hope to be leaving
                        </small>
                    </div>

                    <input type="button" onClick={this.handleSubmit} value="Create Carpool" className="btn btn-primary"/>



                </form>


            </div>
        );
    }

}

export default NewCarpool;
