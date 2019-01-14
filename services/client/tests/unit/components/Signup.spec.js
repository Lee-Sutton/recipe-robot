import faker from 'faker';
import { shallowMount } from '@vue/test-utils';
import Signup from '../../../src/components/Signup.vue';
import { signup } from '../../../src/api/users';

jest.mock('../../../src/api/users.js');

describe('Signup test suite', () => {
    let wrapper;

    beforeEach(() => {
        wrapper = shallowMount(Signup);
        jest.resetAllMocks();
    });

    it('should allow the user to signup', () => {
        const user = {
            email: faker.internet.email(),
            password: faker.internet.password(),
        };

        wrapper.find('[data-cy=email]').setValue(user.email);
        wrapper.find('[data-cy=password]').setValue(user.password);
        wrapper.find('[data-cy=password-confirm]').setValue(user.password);
        wrapper.find('form').trigger('submit');
        expect(signup).toHaveBeenCalledWith();
    });
});
