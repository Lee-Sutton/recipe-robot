import { shallowMount, RouterLinkStub } from '@vue/test-utils';
import Navbar from '@/components/Navbar.vue';

describe('Navbar.vue', () => {
    it('Renders the navigation bar for the user', () => {
        const wrapper = shallowMount(Navbar, {
            stubs: { RouterLink: RouterLinkStub },
        });
        expect(wrapper.text()).toContain('Recipe Robot');
        expect(wrapper.text()).toContain('About');
    });
});
