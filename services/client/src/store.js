import Vue from 'vue';
import Vuex from 'vuex';
import {signup as userSignup, login as userLogin} from './api/users';

Vue.use(Vuex);

export const state = {
    isLoggedIn: !!localStorage.getItem('token'),
};

export const mutations = {
    loginSuccess(state) {
        state.isLoggedIn = true;
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
        commit('loginSuccess');
        localStorage.setItem('token', result.key);
    },

    /**
     * Calls API signup with the input credentials
     * @param commit
     * @param credentials - username, email, password1, password2
     */
    async signup({commit}, credentials) {
        const result = await userSignup(credentials);
        commit('loginSuccess');
        localStorage.setItem('token', result.key);
    }
};

export default new Vuex.Store({
    state,
    mutations,
    actions,
});
