import {shallowMount, RouterLinkStub} from '@vue/test-utils';
import Home from '@/views/Home.vue';

describe('Home.vue', () => {
    let wrapper;
    beforeEach(() => {
        wrapper = shallowMount(Home, {
            stubs: {
                RouterLink: RouterLinkStub,
            },
        });
    });
    it('renders the welcome message', () => {
        expect(wrapper.text()).toContain('Welcome to recipe buddy');
    });

    it('should link the user to the create an account page', () => {
        const routerStubs = wrapper.findAll(RouterLinkStub);
        expect(routerStubs.at(0).props().to).toEqual({name: 'signup'});
        expect(routerStubs.at(1).props().to).toEqual({name: 'login'});
    });
});
