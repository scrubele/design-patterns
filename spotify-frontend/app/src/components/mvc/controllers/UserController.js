import React from 'react';
import axios from 'axios';
import UserView from 'components/mvc/views/UserView'
import { UserModel } from 'components/mvc/models/UserModel';
import { AddUserModal } from 'components/layouts/modals/AddUserModal';

class UserController extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            songs: []
        }
        // this.update = this.update.bind(this)
    }


    componentDidMount() {
    }

    render() {
        return (
            <React.Fragment>

                <div className="row d-flex justify-content-center align-items-center">
                    <div className="col-md-12 row d-flex justify-content-center align-items-center">
                        <AddUserModal addUser={this.props.addUser} updateUser={this.props.updateUser} update={this.props.getUsers} />
                    </div>
                    <div className="row d-flex justify-content-center align-items-center">
                        {this.props.songs.map(song => <UserView basic_user_id={song[0]} email={song[1]} country={song[4]} age={song[3]} removeUser={this.props.removeUser} update={this.props.getUsers}></UserView>)}
                    </div>
                </div>
            </React.Fragment>
        )
    }
}

export default UserModel(UserController)