import faker from 'faker';
import { shallowMount } from '@vue/test-utils';
import Signup from '../../../src/components/Signup.vue';

describe('App.vue', () => {
    let wrapper;

    beforeEach(() => {
        wrapper = shallowMount(Signup);
    });

    it('should render a login form', () => {
        const user = {
            email: faker.internet.email(),
            password: faker.internet.password(),
        };

        wrapper.find('[data-cy=email]').setValue(user.email);
        wrapper.find('[data-cy=password]').setValue(user.password);
        wrapper.find('[data-cy=password-confirm]').setValue(user.password);
        wrapper.find('form').trigger('submit');
    });
});
