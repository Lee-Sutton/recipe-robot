import {state, mutations} from '../../src/store';
import {clearLocalStorage} from '../utils';

beforeEach(() => {
    clearLocalStorage();
});

describe('state', () => {
    test('isLoggedIn returns true when an auth token is present', () => {
        localStorage.setItem('token', true);
        expect(state.isLoggedIn()).toBeTruthy();
    });

    test('isLoggedIn returns false when a user is not logged in', () => {
        expect(state.isLoggedIn()).toBeFalsy();
    });
});

describe('mutations', () => {
    let state;

    beforeEach(() => {
        state = {}
    });

    test('login sets the pending state to true', () => {
        mutations.login(state);
        expect(state.pending).toBeTruthy();
    });
});
