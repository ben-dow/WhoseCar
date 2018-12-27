import React, {Component} from 'react';
import "./Share.css"

class Share extends Component {

    constructor(props){
        super(props)

        this.state = {
            CarpoolID : props.CarpoolID,
            msg  : "Copy To Clipboard"
        }

        this.copyTextInput = React.createRef();

        this.onCopyToClipBoard = this.onCopyToClipBoard.bind(this)
    }


    onCopyToClipBoard(){
        const input = this.copyTextInput.current;

        input.select();
        document.execCommand("copy")

        this.setState({
            msg : "Copied!"
        })

    }

    render() {
        return (
            <div id="sharing">
                <input ref={this.copyTextInput} className="link-display form-control" type="text" value={"whosemyride.com/Carpool/" + this.state.CarpoolID} readOnly/>
                <input onClick={this.onCopyToClipBoard} type="button" className="btn btn-primary ShareButton" value={this.state.msg}/>
            </div>
            )
    }

}

export default Share;
