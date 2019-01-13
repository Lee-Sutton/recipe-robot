import { mount } from '@vue/test-utils';
import App from '@/App.vue';

describe('App.vue', () => {
    let wrapper;

    beforeEach(() => {
        wrapper = mount(App, {
            stubs: ['router-link', 'router-view'],
        });
    });

    it('should render the navbar for the user', () => {
        expect(wrapper.find('nav').text()).toContain('Home');
        expect(wrapper.find('nav').text()).toContain('About');
    });
});
