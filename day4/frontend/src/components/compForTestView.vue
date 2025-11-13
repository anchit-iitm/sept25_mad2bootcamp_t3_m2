<template>
    <div class="comp-for-test-view">
        <h1>{{ msgThatWasPassedToUs }}</h1>
    </div>
</template>

<script>
export default {
    name: 'CompForTestView',
    props: {
        msgThatWasPassedToUs: {
            type: String,
            required: true
        }
    }
};
</script>

<style scoped>
.comp-for-test-view {
  padding: 1rem;
}
</style>