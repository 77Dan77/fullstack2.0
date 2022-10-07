import React, {Component, Fragment} from 'react';
import ReactDOM from 'react-dom';
import { HashRouter as Router, Route, Switch, Routes, Redirect } from "react-router-dom"

import Header from './layout/Header';
import Dashboard from './leads/Dashboard';
import Login from './accounts/Login';
import Register from './accounts/Register';
import PrivateRoute from './common/PrivateRoute';

import { Provider } from "react-redux";
import store from '../store';

class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <Router>
                    <Fragment>
                        <Header />
                        <div className="container">
                            <Routes>
                                <PrivateRoute path="/" element={<Dashboard/>}/>
                                <PrivateRoute path="/register" element={<Register/>}/>
                                <PrivateRoute path="/login" element={<Login/>}/>
                            </Routes>
                        </div>
                    </Fragment>
                </Router>
            </Provider>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'));
