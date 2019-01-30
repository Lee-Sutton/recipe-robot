import {signup, currentUser, HOST_URL} from "../../../src/api/users";
import mockAxios from 'jest-mock-axios';
import faker from 'faker';

const user = {
    email: faker.internet.email(),
    password: faker.internet.password(),
};

afterEach(() => {
    mockAxios.reset();
});

test('it should send a post request with the user data', () => {
    signup(user);
    expect(mockAxios.post).toHaveBeenCalledWith(`${HOST_URL}/api/v1/rest-auth/registration/`, user);
});

test('currentUser', async () => {
    const output = await currentUser(token);
    expect(mockAxios.get).toHaveBeenCalledWith(`${HOST_URL}/api/v1/user/`, {
        headers: {
            Authorization: `Token ${token}`
        }
    });
});
