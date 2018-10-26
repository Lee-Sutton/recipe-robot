import { shallowMount } from '@vue/test-utils';
import Welcome from '@/components/Welcome.vue';

describe('Welcome.vue', () => {
    it('renders the welcome message', () => {
        const wrapper = shallowMount(Welcome);
        expect(wrapper.text()).toContain('Welcome to recipe buddy');
    });
});
