import React, {Component} from 'react';
import './Login.css';

class Login extends Component {

    render() {

        return (
            <div id="Login">
                <div className="center-wrap">
                    <h3> Login </h3>
                </div>
                <form>

                    <div className="form-group row">
                        <input type="text" className="form-control" placeholder="Name"/>
                    </div>
                    <div className="form-group row">
                        <input type="password" className="form-control" placeholder="Password (Optional)"/>
                    </div>
                    <div className="center-wrap">
                        <button className="btn btn-primary"> Login to Carpool</button>
                    </div>

                </form>
            </div>
        );
    }

}

export default Login;
