import flushPromises from 'flush-promises';
import {state, mutations, actions} from '../../src/store';
import {clearLocalStorage} from '../utils';
import {signup} from '../../src/api/users';

jest.mock('@/api/users.js');

const authToken = {key: '12345'};

beforeEach(() => {
    clearLocalStorage();
});

// describe('state', () => {
//     test('isLoggedIn returns true when an auth token is present', () => {
//         localStorage.setItem('token', true);
//         console.log(localStorage);
//         console.log(state);
//         expect(state.isLoggedIn).toBeTruthy();
//     });
//
//     test('isLoggedIn returns false when a user is not logged in', () => {
//         expect(state.isLoggedIn).toBeFalsy();
//     });
// });

describe('mutations', () => {
    let state;

    beforeEach(() => {
        state = {}
    });

    test('login sets the pending state to true', () => {
        mutations.login(state);
        expect(state.pending).toBeTruthy();
    });

    test('loginSuccess sets pending to false and isLoggedIn to true', () => {
        mutations.loginSuccess(state);
        expect(state.pending).toBeFalsy();
        expect(state.isLoggedIn).toBeTruthy();
    });
});

describe('actions', () => {
    const commit = jest.fn();
    let loginCredentials,
        signupCredentials;

    beforeEach(() => {
        clearLocalStorage();
        jest.resetAllMocks();
        signup.mockResolvedValue(authToken);

        loginCredentials = {
            username: 'Lee',
            email: 'lee@e.com',
            password: 'password'
        };

        signupCredentials = {
            username: loginCredentials.username,
            email: loginCredentials.email,
            password1: loginCredentials.password,
            password2: loginCredentials.password,
        };
    });

    // test('login success', async () => {
    //     await actions.login({commit}, credentials);
    //     expect(commit).toBeCalledWith('loginSuccess');
    //     expect(localStorage.getItem('token')).toBeTruthy();
    // });

    test('signup success', async () => {
        await actions.signup({commit}, signupCredentials);
        await flushPromises();
        expect(signup).toBeCalledWith(signupCredentials);
        expect(commit).toBeCalledWith('signup');
        expect(localStorage.getItem('token')).toEqual(authToken.key);
    });
});
