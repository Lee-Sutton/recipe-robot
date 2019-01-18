<template>
    <div>
        <form @submit.prevent="handleSubmit">
            <div class="field">
                <label class="label">Email</label>
                <div class="control">
                    <input class="input" type="text" placeholder="Email" v-model="email"
                           data-cy="email">
                </div>
            </div>

            <div class="field">
                <label class="label">Password</label>
                <div class="control">
                    <input class="input" type="password" placeholder="Password" v-model="password"
                           data-cy="password">
                </div>
            </div>

            <div class="field">
                <label class="label">Confirm Password</label>
                <div class="control">
                    <input class="input" type="password" placeholder="Password"
                           v-model="passwordConfirm" data-cy="password-confirm">
                </div>
            </div>
        </form>
    </div>
</template>

<script>
import { signup } from '../api/users';

export default {
    name: 'Signup',
    data() {
        return {
            email: null,
            password: null,
            passwordConfirm: null,
        };
    },
    methods: {
        handleSubmit() {
            signup({
                email: this.email,
                password: this.password,
                passwordConfirm: this.passwordConfirm,
            });
        },
    },
};
</script>

<style scoped>

</style>
