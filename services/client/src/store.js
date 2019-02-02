import Vue from 'vue';
import Vuex from 'vuex';
import {signup as userSignup} from './api/users';

Vue.use(Vuex);

export const state = {
    isLoggedIn: !!localStorage.getItem('token'),
};

export const mutations = {
    signup(state) {
        state.pending = true;
    },
    login(state) {
        state.pending = true;
    },
    loginSuccess(state) {
        state.pending = false;
        state.isLoggedIn = true;
    }
};

export const actions = {
    // login({commit}, credentials) {
    //     console.log('running');
    //     localStorage.setItem('token', 'dummyToken');
    //     commit('loginSuccess');
    // }

    /**
     * Calls signup with the input credentials
     * @param commit
     * @param credentials - username, email, password1, password2
     */
    async signup({commit}, credentials) {
        const result = await userSignup(credentials);
        commit('signup');
        localStorage.setItem('token', result.key);
    }
};

export default new Vuex.Store({
    state,
    mutations,
    actions,
});
