import Vue from 'vue';
import Vuex from 'vuex';
import {signup as userSignup, login as userLogin} from './api/users';

Vue.use(Vuex);

export const state = {
    isLoggedIn: !!localStorage.getItem('token'),
};

export const mutations = {
    /**
     * To be called after a successful login attempt
     * @param token (Payload) - auth token returned by the api
     */
    loginSuccess(state, token) {
        state.isLoggedIn = true;
        localStorage.setItem('token', token);
    }
};

export const actions = {

    /**
     * Calls API login with the input credentials
     * @param commit
     * @param credentials
     * @returns {Promise<void>}
     */
    async login({commit}, credentials) {
        const result = await userLogin(credentials);
        commit('loginSuccess', result.key);
    },

    /**
     * Calls API signup with the input credentials
     * @param commit
     * @param credentials - username, email, password1, password2
     */
    async signup({commit}, credentials) {
        const result = await userSignup(credentials);
        commit('loginSuccess', result.key);
    }
};

export default new Vuex.Store({
    state,
    mutations,
    actions,
});
