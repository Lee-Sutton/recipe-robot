import faker from 'faker';
import { shallowMount } from '@vue/test-utils';
import Signup from '../../../src/components/Signup.vue';
import flushPromises from 'flush-promises';
import { signup } from '../../../src/api/users';

jest.mock('../../../src/api/users.js');

describe('Signup test suite', () => {
    let wrapper;

    const $router = {
        push: jest.fn()
    };

    beforeEach(() => {
        wrapper = shallowMount(Signup, {
            mocks: {
                $router
            }
        });
        jest.resetAllMocks();
    });

    it('should allow the user to signup', async () => {

        const user = {
            username: faker.internet.userName(),
            email: faker.internet.email(),
            password: faker.internet.password(),
        };

        wrapper.find('[data-cy=username]').setValue(user.username);
        wrapper.find('[data-cy=email]').setValue(user.email);
        wrapper.find('[data-cy=password1]').setValue(user.password);
        wrapper.find('[data-cy=password2]').setValue(user.password);
        wrapper.find('form').trigger('submit');
        expect(signup).toHaveBeenCalledWith({
            username: user.username,
            email: user.email,
            password1: user.password,
            password2: user.password,
        });
        await flushPromises();

        // The user is directed back to the home page
        expect($router.push).toHaveBeenCalledWith('home');
    });
});
