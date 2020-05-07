import React from 'react'

export default class AddUser extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        return (
            <form className="row">
                <div className="m-1">
                    <label for="fname">Email:</label><br />
                    <input type="text" id="Email" name="fname" /><br />
                </div>
                <div className="m-1">
                    <label for="Password">Password:</label><br />
                    <input type="text" id="Password" name="Password" />
                </div>
                <div className="m-1">
                    <label for="Age">Age:</label><br />
                    <input type="text" id="Age" name="Age" /><br />
                </div>
                <div className="m-1">
                    <label for="Country">Country:</label><br />
                    <input type="text" id="Country" name="Country" />
                </div>
            </form>
        )
    }
}