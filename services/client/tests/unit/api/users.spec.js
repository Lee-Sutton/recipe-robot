import {signup, login, HOST_URL} from "../../../src/api/users";
import mockAxios from 'jest-mock-axios';
import faker from 'faker';

const user = {
    email: faker.internet.email(),
    password: faker.internet.password(),
};

afterEach(() => {
    mockAxios.reset();
});

test('signup', () => {
    signup(user);
    expect(mockAxios.post).toHaveBeenCalledWith(`${HOST_URL}/api/v1/rest-auth/registration/`, user);
});

test('login', () => {
    login(user);
    expect(mockAxios.post).toHaveBeenCalledWith(`${HOST_URL}/api/v1/rest-auth/login/`, user)
});
