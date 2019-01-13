<template>
    <div>
        <form>
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
        </form>
    </div>
</template>

<script>
export default {
    name: 'Signup',
};
</script>

<style scoped>

</style>
