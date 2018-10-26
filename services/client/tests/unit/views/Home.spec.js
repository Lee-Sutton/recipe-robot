import { shallowMount } from '@vue/test-utils';
import Home from '@/views/Home.vue';

describe('Home.vue', () => {
    it('renders the welcome message', () => {
        const wrapper = shallowMount(Home);
        expect(wrapper.text()).toContain('Welcome to recipe buddy');
    });
});
