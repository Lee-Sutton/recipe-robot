import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export const state = {
    isLoggedIn: () => localStorage.getItem('token'),
};

export const mutations = {
    login(state) {
        state.pending = true;
    }
};

export const actions = {};

export default new Vuex.Store({
    state,
    mutations,
    actions,
});
