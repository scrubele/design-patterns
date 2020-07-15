import React from 'react'
import { Modal, Container, Row, Button, Col } from 'react-bootstrap';

export default class UserView extends React.Component {

    constructor(props) {
        super(props);
    }

    removeUser(e){
        this.props.removeUser(this.props.basic_user_id);
        setTimeout(() => {
            this.props.update();
          },
            2200)
    }
    render() {
        return (
                <Col md={3} clasname="md-3 card">
                    <img className="card-img-top" src="user.png" alt="Card image cap" />
                    <div className="card-body">
                        <h5 className="card-title"><b>ID:</b> {this.props.basic_user_id}</h5>
                        <p className="card-text"><b>Email:</b>     {this.props.email}</p>
                        <p className="card-text"><b>Country:</b>  {this.props.country}</p>
                        <p className="card-text"><b>Age:</b>       {this.props.age}</p>
                        <a href="#" className="btn btn-dark w-100 m-1" onClick={this.removeUser.bind(this)}>Remove a user</a>
                        <a href="#" className="btn btn-dark w-100 m-1">Get songs</a>
                    </div>
                </Col>
        )
    }
}