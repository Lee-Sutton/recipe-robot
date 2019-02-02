import axios from 'axios';

export const HOST_URL = 'http://localhost:8000';

/**
 * Signs up the input user
 * @param user - {username, email, password1, password2}
 * @returns {Promise<AxiosPromise<any>>}
 */
export const signup = async (user) => {
    return axios.post(`${HOST_URL}/api/v1/rest-auth/registration/`, user);
};

// FIXME this should come from the store
// FIXME do I need async here
export const currentUser = async () => {
    return axios.get(`${HOST_URL}/api/v1/user/`);
};
