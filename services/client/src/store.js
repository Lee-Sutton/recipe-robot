import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export const state = {
    isLoggedIn: !!localStorage.getItem('token'),
};

export const mutations = {
    login(state) {
        state.pending = true;
    },
    loginSuccess(state) {
        state.pending = false;
        state.isLoggedIn = true;
    }
};

export const actions = {
    login({commit}, credentials) {
        console.log('running');
        localStorage.setItem('token', 'dummyToken');
        commit('loginSuccess');
    }
};

export default new Vuex.Store({
    state,
    mutations,
    actions,
});
