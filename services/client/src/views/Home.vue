<template>
    <section class="hero">
        <div class="hero-body">
            <div class="container has-text-centered">
                <h1 class="title">Welcome to recipe buddy!</h1>
                <p><router-link :to="{name: 'signup'}">Create an account</router-link> or <router-link :to="{name: 'login'}">login</router-link> to get started</p>
            </div>
        </div>
    </section>
</template>

<script>
// @ is an alias to /src

export default {
    name: 'home',
};
</script>
