import { createStore, applyMiddleware } from "redux";
import { composeWithDevTools} from "redux-devtools-extension";
import thunk from "redux-thunk";
import rootRReducer from './reducers';

const initialState = {};

const middleware = [thunk];

const store = createStore(
    rootRReducer,
    initialState,
    composeWithDevTools(applyMiddleware(...middleware))
);

export default store;