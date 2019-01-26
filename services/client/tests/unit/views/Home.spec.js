import {shallowMount, RouterLinkStub} from '@vue/test-utils';
import Home from '@/views/Home.vue';
import {currentUser} from '@/api/users.js';

jest.mock('@/api/users.js');

describe('Home.vue', () => {
    let wrapper;
    describe('New user view', () => {
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

    describe('Signed in view', () => {
        const user = {
            name: 'Lee',
            id: 1
        };
        it('should render the welcome message to the user', function () {
            currentUser.mockImplementation(() => {
                user
            });
            expect(wrapper.text()).toContain(user.name);
        });
    });
});
