import { mount, RouterLinkStub } from '@vue/test-utils';
import App from '@/App.vue';

describe('App.vue', () => {
    let wrapper;

    beforeEach(() => {
        wrapper = mount(App, {
            stubs: {
                RouterLink: RouterLinkStub,
            },
        });
    });

    it('should render the navbar for the user', () => {
        expect(wrapper.find('nav').text()).toContain('Recipe Robot');
    });
});
