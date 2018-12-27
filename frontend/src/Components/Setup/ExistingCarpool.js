import React, {Component} from 'react';
import {Link} from "react-router-dom";
import * as axios from "axios";

class ExistingCarpool extends Component {


    constructor(props) {
        super(props);
        this.state = {
            isCarpoolNotFound : false
        }


        this.handleGetCarpool = this.handleGetCarpool.bind(this);
        this.handleInputChange = this.handleInputChange.bind(this);

    }

    handleInputChange(event) {
        const target = event.target;
        const value = target.value;
        const name = target.name;

        this.setState({
            [name] : value
        });

    }

    handleGetCarpool(){
        axios({
            method: 'head',
            url: 'http://localhost:5000/Carpool/' + this.state.carpoolID,
        })
            .then(function (response) {
                console.log(response)

            })
            .catch(function(error){
                this.setState({
                    isCarpoolNotFound : true

                });


            }.bind(this));
    }

    render() {

        const isCarpoolNotFound = this.state.isCarpoolNotFound;

        return (
            <div className="center-control" id="ExistingCarpool" >
                {isCarpoolNotFound ? (
                    <div className="alert alert-danger" role="alert">
                        That Carpool ID wasn't found! Try another!
                    </div> ): (<div></div>)}


                <form onSubmit={(e) => {
                    /**
                     * Prevent submit from reloading the page
                     */
                    e.preventDefault();
                    e.stopPropagation();
                    this.handleGetCarpool();
                }}>
                    <Link to="/" className="link">Back to Home</Link>
                    <div className="form-group row">
                        <input type="text" className="form-control"  onChange={this.handleInputChange} name="carpoolID" placeholder="Carpool ID"/>
                    </div>
                    <input type="submit" className="btn btn-primary" value="Find Carpool"/>

                </form>

            </div>
        );
    }

}

export default ExistingCarpool;
