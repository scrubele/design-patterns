import React from 'react';
import axios from 'axios';
import { GetJSONRequest, PostJSONRequest, PutJSONRequest, DeleteJSONRequest } from './Requests';
import UserView from 'components/mvc/views/UserView'

export const UserModel = (ComposedComponent) => {
  class UserModel extends React.Component {
    constructor(props){
      super(props);
      this.state = {
        songs: [],
        newUserData : []
      }
      // this.componentDidMount()
      this.getUsers = this.getUsers.bind(this)
  }

    componentDidMount() {
     this.getUsers();
    }

    getUsers(){
      let makeFileRequest = new Promise(function (resolve, reject) {
        var request = new GetJSONRequest('users')
        request.makeRequest()
        setTimeout(() => {
          resolve(request.response)
        },
          3000)
      })
      makeFileRequest.then(
        response => {
          console.log(response["json_list"]);
          this.setState({ songs: response["json_list"] });
        }
      )
    }
    
    addUser(data){
      console.log(data)
      let makeFileRequest = new Promise(function (resolve, reject) {
        var request = new PostJSONRequest('users', data)
        request.makeRequest()
        setTimeout(() => {
          resolve(request.response)
        },
          2200)
      })
      makeFileRequest.then(
        response => {
          console.log(response)
          console.log('here')
        }
      )
    }

    updateUser(data, user_id){
      console.log(user_id)
      let makeFileRequest = new Promise(function (resolve, reject) {
        var request = new PutJSONRequest('users/'+user_id, data)
        request.makeRequest()
        setTimeout(() => {
          resolve(request.response)
        },
          2200)
      })
      makeFileRequest.then(
        response => {
          console.log(response)
          console.log('here')
        }
      )
    }

    removeUser(user_id){
      console.log(user_id)
      let makeFileRequest = new Promise(function (resolve, reject) {
        var request = new DeleteJSONRequest('users/'+ user_id)
        request.makeRequest()
        setTimeout(() => {
          resolve(request.response)
        },
          2200)
      })
      makeFileRequest.then(
        response => {
          console.log(response)
          console.log('here')
        }
      )
    }
    render() {
      return (
        <ComposedComponent songs={this.state.songs} addUser={this.addUser} removeUser={this.removeUser} updateUser={this.updateUser} getUsers={this.getUsers}/>
      )
    }

    
  }
  return UserModel;
}