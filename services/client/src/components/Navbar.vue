<template>
    <nav class="navbar" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
            <router-link :to="{name: 'home'}" class="navbar-item">
                <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28">
            </router-link>
        </div>

        <div id="navbarBasicExample" class="navbar-menu">
            <div class="navbar-start">
                <router-link :to="{name: 'home'}" class="navbar-item">Home</router-link>
                <router-link :to="{name: 'about'}" class="navbar-item">About</router-link>
            </div>

            <div class="navbar-end">
                <div class="navbar-item">
                    <div class="buttons">
                        <a class="button is-primary">
                            <strong>Sign up</strong>
                        </a>
                        <a class="button is-light">
                            Log in
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    name: 'Navbar',
};
</script>

<style scoped>

</style>
