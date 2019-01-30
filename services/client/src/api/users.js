import axios from 'axios';

export const HOST_URL = 'http://localhost:8000';

export const signup = async (user) => {
    return axios.post(`${HOST_URL}/api/v1/rest-auth/registration/`, user);
};

// FIXME this should come from the store
// FIXME do I need async here
export const currentUser = async () => {
    return axios.get(`${HOST_URL}/api/v1/user/`);
};
