import axios from 'axios';

export const HOST_URL = 'http://localhost:8000';

export const signup = async (user) => {
    await axios.post(`${HOST_URL}/api/v1/rest-auth/registration/`, user);
};
