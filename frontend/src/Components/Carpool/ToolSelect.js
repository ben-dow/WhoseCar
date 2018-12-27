import React, {Component} from 'react';
import {Link} from "react-router-dom";

class ToolSelect extends Component {
    render() {
        return (

            <div>
                <div id="control-buttons">
                    <Link to={`${this.props.BaseURL}/Login`}><button id="LinkToLogin" type="button" className={"btn " + (this.props.ActiveLink === "Login" ? "btn-primary" : "btn-secondary")}>Login</button></Link>
                    <Link to={`${this.props.BaseURL}/Display`}><button id="LinkToDisplay" type="button" className={"btn " + (this.props.ActiveLink === "Display" ? "btn-primary" : "btn-secondary")}>Display</button></Link>
                    <Link to={`${this.props.BaseURL}/Settings`}><button id="LinkToSettings" type="button" className={"btn " + (this.props.ActiveLink === "Settings" ? "btn-primary" : "btn-secondary")}>Settings</button></Link>
                    <Link to={`${this.props.BaseURL}/Share`}><button id="LinkToShare" type="button" className={"btn " + (this.props.ActiveLink === "Share" ? "btn-primary" : "btn-secondary")}>Share</button></Link>
                </div>
            </div>
        )
    }

}

export default ToolSelect;
