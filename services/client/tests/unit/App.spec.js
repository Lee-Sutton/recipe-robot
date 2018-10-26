import { mount, RouterLinkStub } from '@vue/test-utils';
import App from '@/App.vue';

describe('App.vue', () => {
    it('Renders the welcome message', () => {
        const wrapper = mount(App, {
            stubs: { RouterLink: RouterLinkStub },
        });
        expect(wrapper.text()).toContain('Welcome');
    });
});
