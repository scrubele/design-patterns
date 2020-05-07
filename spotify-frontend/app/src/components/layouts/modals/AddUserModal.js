import React from 'react';
import { Modal, Container, Row, Button, Col } from 'react-bootstrap';

class UserModalWithGrid extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            email: "",
            password: "",
            age: 0,
            country: ""
        }
        console.log(props)
    }

    onChangeState(e) {
        this.setState({
            [e.target.name]: e.target.value
        }, () => console.log(this.state))
    }

    formData(e) {
        console.log('here')
        let formData = new FormData();
        formData.append('email', this.state.email);
        formData.append('country', this.state.password);
        formData.append('age', this.state.age);
        return formData
    }

    addUser(e) {
        let formData = this.formData(e)
        this.props.addUser(formData)
        alert("userSuccessfullyAdded")
        this.props.onHide()
        setTimeout(()=>{
            this.props.update();
        }, 1000)
        
    }

    updateUser(e) {
        let formData = this.formData(e)
        this.props.updateUser(formData, this.state.id)
        alert("userSuccessfullyUpdated")
        this.props.onHide()
        this.props.update();
    }
    render() {
        return (
            <Modal show={this.props.show} onHide={this.props.onHide} aria-labelledby="contained-modal-title-vcenter">
                <Modal.Header closeButton>
                    <Modal.Title id="contained-modal-title-vcenter">
                        Add a User
          </Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <Container>
                        <Row className="show-grid">
                            <htmlForm className="row  d-flex justify-content-center">
                                <div className="m-1">
                                    <label htmlFor="email">Email:</label><br />
                                    <input type="text" id="Email" name="email" onChange={this.onChangeState.bind(this)} /><br />
                                </div>
                                <div className="m-1">
                                    <label htmlFor="password">Password:</label><br />
                                    <input type="text" id="password" name="password" onChange={this.onChangeState.bind(this)} />
                                </div>
                                <div className="m-1">
                                    <label htmlFor="age">Age:</label><br />
                                    <input type="number" id="age" name="age" onChange={this.onChangeState.bind(this)} /><br />
                                </div>
                                <div className="m-1">
                                    <label htmlFor="country">Country:</label><br />
                                    <input type="text" id="country" name="country" onChange={this.onChangeState.bind(this)} />
                                </div>
                            </htmlForm>
                        </Row>
                    </Container>
                </Modal.Body>
                <Modal.Footer>
                    <div className="col-md-12 row">
                        <Button className="col-md-12 m-1" variant="dark" onClick={this.addUser.bind(this)}>Add a user</Button>
                        <div className="col-md-6 m-1">
                            <label htmlFor="id">User_id:</label><br />
                            <input type="number" className="w-100" id="id" name="id" onChange={this.onChangeState.bind(this)} /><br />
                        </div>
                        <Button className="col-md-5 m-1" variant="dark" onClick={this.updateUser.bind(this)}>Update a user by id:</Button>
                    </div>
                </Modal.Footer>
            </Modal>
        );
    }
}

export class AddUserModal extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            ModalShow: false
        }
        this.hideModalShow = this.hideModalShow.bind(this)
    }

    setModalShow(e) {
        this.setState({
            ModalShow: true
        })
    }

    hideModalShow(e) {
        this.setState({
            ModalShow: false
        })
    }
    render() {
        return (
            <React.Fragment>
                <Button variant="dark" className="col-md-5" onClick={this.setModalShow.bind(this)}>
                    Add a User
                </Button>
                {this.state.ModalShow ?
                    <UserModalWithGrid show={this.state.ModalShow} onHide={() => this.hideModalShow()} updateUser={this.props.updateUser} addUser={this.props.addUser} update={this.props.update} />
                    : null}
            </React.Fragment>
        );
    }
}
