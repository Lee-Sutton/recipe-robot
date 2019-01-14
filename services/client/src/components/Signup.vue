<template>
    <div>
        <form @submit.prevent="handleSubmit">
            <div class="field">
                <label class="label">Email</label>
                <div class="control">
                    <input class="input" type="text" placeholder="Email" data-cy="email">
                </div>
            </div>

            <div class="field">
                <label class="label">Password</label>
                <div class="control">
                    <input class="input" type="password" placeholder="Password" data-cy="password">
                </div>
            </div>

            <div class="field">
                <label class="label">Confirm Password</label>
                <div class="control">
                    <input class="input" type="password" placeholder="Password"
                           data-cy="password-confirm">
                </div>
            </div>
        </form>
    </div>
</template>

<script>
import { signup } from '../api/users';

export default {
    name: 'Signup',
    methods: {
        handleSubmit() {
            signup();
        },
    },
};
</script>

<style scoped>

</style>
