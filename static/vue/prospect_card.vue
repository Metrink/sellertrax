<template>
    <div>{{ test }}</div>
</template>

<script>
module.exports = {
    data: function() {
        return { test: 'Hello World' };
    }
}
</script>

<style scoped>
div {
    font-size: 3em;
    text-align: center;
}
</style>