<template>
    <section class="section is-small">
        <div class="container">
            <form @submit.prevent="handleSubmit">
                <div class="field">
                    <label class="label">Username</label>
                    <div class="control">
                        <input class="input" type="text" placeholder="Username" v-model="username"
                               data-cy="username">
                    </div>
                </div>

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
                        <input class="input" type="password" placeholder="Password" v-model="password1"
                               data-cy="password1">
                    </div>
                </div>

                <div class="field">
                    <label class="label">Confirm Password</label>
                    <div class="control">
                        <input class="input" type="password" placeholder="Password"
                               v-model="password2" data-cy="password2">
                    </div>
                </div>

                <div class="field">
                    <button class="is-primary" @submit.prevent="handleSubmit">Submit</button>
                </div>

            </form>
        </div>
    </section>
</template>

<script>
import { signup } from '../api/users';

export default {
    name: 'Signup',
    data() {
        return {
            username: null,
            email: null,
            password1: null,
            password2: null,
        };
    },
    methods: {
        async handleSubmit() {
            await signup({
                username: this.username,
                email: this.email,
                password1: this.password1,
                password2: this.password2,
            });

            this.$router.push('home');
        },
    },
};
</script>

<style scoped>

</style>
