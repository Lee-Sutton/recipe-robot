<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container">
                <router-link to="home" class="navbar-brand">Recipe Robot</router-link>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                        <li class="nav-item active">
                            <router-link to="home" class="nav-link">Home</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link to="about" class="nav-link">About</router-link>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        <welcome></welcome>
    </div>
</template>

<script>
import Welcome from '@/components/Welcome.vue';

export default {
    components: {
        Welcome,
    },
};
</script>
