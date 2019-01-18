import { shallowMount, RouterLinkStub } from '@vue/test-utils';
import Navbar from '@/components/Navbar.vue';

describe('Navbar.vue', () => {
    let wrapper = null;

    beforeEach(() => {
        wrapper = shallowMount(Navbar, {
            stubs: { RouterLink: RouterLinkStub },
        });
    });
    it('Renders the navigation bar for the user', () => {
        expect(wrapper.text()).toContain('Home');
        expect(wrapper.text()).toContain('About');
    });

    it('should link to the signup and login pages', () => {
        const routerStubs = wrapper.findAll(RouterLinkStub);
        expect(routerStubs.at(0).props().to).toEqual({name: 'home'});
        expect(routerStubs.at(2).props().to).toEqual({name: 'about'});
        expect(routerStubs.at(3).props().to).toEqual({name: 'signup'});
        expect(routerStubs.at(4).props().to).toEqual({name: 'login'});
    });
});
