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

/**
 * Login for the input user
 * @param user = {username, email, password}
 * @returns {Promise<AxiosPromise<any>>}
 */
export const login = async (user) => {
    return axios.post(`${HOST_URL}/api/v1/rest-auth/login/`, user);
};
