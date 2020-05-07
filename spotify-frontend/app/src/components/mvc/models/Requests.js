// import { BASE_URL  } from 'constants/Constants'
const BASE_URL = 'http://DESKTOP-DDAN4MP:8080/';

const BASE_HEADERS = {
    'Access-Control-Allow-Origin': true
}

export class BaseRequest {

    constructor(method, headers, body, url) {
        this.method = method
        this.headers = headers
        this.body = body
        this.url = BASE_URL+url
        this.response = ""
        console.log(this.body)
    }

    stringify() {
        return JSON.stringify(this)
    }

    toDict() {
        return JSON.parse(this.stringify())
    }

    makeFileRequest = function () {
        var data = {
            method: this.method,
            headers: this.headers,
            body: this.body
        }
        fetch(this.url, data)
            .then((response) => {
                if (response.ok) {
                    return response.blob().then((myBlob) => {
                        var objectURL = URL.createObjectURL(myBlob);
                        this.response = objectURL;
                    });
                } else {
                    return response.json().then((jsonError) => {
                        this.response = jsonError;
                    });
                }
            });
    }

    makeJSONRequest = function () {
        let formData = new FormData();
        formData.append('email', 'John');
        formData.append('country', 'John123');
        var data = {
            method: this.method,
            headers: this.headers,
            body: this.body
        }
        fetch(this.url, data)
            .then((response) => {
                if (response.ok) {
                    return response.json().then((data) => {
                        this.response = data;
                        console.log(this.response)
                    });
                } else {
                    return response.json().then((jsonError) => {
                        this.response = jsonError;
                    });
                }
            });
    }
}

export class GetJSONRequest extends BaseRequest {

    constructor(URL, body) {
        super('GET', BASE_HEADERS, body, URL)
    }

    makeRequest(){
        this.makeJSONRequest()
    }
}

export class PostJSONRequest extends BaseRequest {

    constructor(URL, body) {
        super('Post', BASE_HEADERS, body, URL)
    }

    makeRequest(){
        this.makeJSONRequest()
    }

    makeJSONRequest = function () {
        var data = {
            method: this.method,
            headers: this.headers,
            body: this.body
        }

        fetch(this.url, data)
            .then((response) => {
                if (response.ok) {
                    return response.json().then((data) => {
                        this.response = data;
                        console.log(this.response)
                    });
                } else {
                    return response.json().then((jsonError) => {
                        this.response = jsonError;
                    });
                }
            });
    }
}

export class DeleteJSONRequest extends BaseRequest {

    constructor(URL, body) {
        super('Delete', BASE_HEADERS, body, URL)
    }

    makeRequest(){
        this.makeJSONRequest()
    }

    makeJSONRequest = function () {
        var data = {
            method: this.method,
            headers: this.headers,
            body: this.body
        }

        fetch(this.url, data)
            .then((response) => {
                if (response.ok) {
                    return response.json().then((data) => {
                        this.response = data;
                        console.log(this.response)
                        alert(JSON.stringify(this.response))
                    });
                } else {
                    return response.json().then((jsonError) => {
                        this.response = jsonError;
                    });
                }
            });
    }
}

export class PutJSONRequest extends BaseRequest {

    constructor(URL, body) {
        super('PUT', BASE_HEADERS, body, URL)
    }

    makeRequest(){
        this.makeJSONRequest()
    }

}