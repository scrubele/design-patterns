import React from 'react'
import UserController from 'components/mvc/controllers/UserController'

export default class UserPage extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        return(
            <React.Fragment>
                <UserController />
            </React.Fragment>
        );
    }
}