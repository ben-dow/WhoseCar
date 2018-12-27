import React, {Component} from 'react';
import Driver from "./Driver";
import Carpooler from "./Carpooler";

class Settings extends Component {

    constructor(props){
        super(props)

        this.SettingTypes = {
            Driver : <Driver/>,
            Carpooler : <Carpooler/>
        }

        this.state = {

            SettingType : null,


        }

        const updateSettingsDisplay = this.updateSettingsDisplay.bind(this);
    }

    updateSettingsDisplay(settingType){
        this.setState({
            SettingType : settingType
        })

    }

    render() {
        return (
            <div>

                <div id="control-buttons">
                    <h3>I will be </h3>
                    <button className={"btn " + (this.state.SettingType === this.SettingTypes.Driver ? 'btn-primary' : 'btn-secondary')} onClick={() => {this.updateSettingsDisplay(this.SettingTypes.Driver)}}>Driving</button>
                    <button className={"btn " + (this.state.SettingType === this.SettingTypes.Carpooler ? 'btn-primary' : 'btn-secondary')} onClick={() => {this.updateSettingsDisplay(this.SettingTypes.Carpooler)}}>Riding</button>
                </div>

                {this.state.SettingType}

            </div>
        )
    }

}

export default Settings;
