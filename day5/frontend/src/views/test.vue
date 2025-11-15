<template>
  <div class="test-view">
    <CompForTestView :msgThatWasPassedToUs="this.$route.params.indiaWantsToKnow" />
    <p>This is a test view component.</p>
  </div>
</template>

<script>
import CompForTestView from '@/components/compForTestView.vue'
export default {
  name: 'TestView',
  components: {
    CompForTestView,
  },
}
</script>

<style scoped>
.test-view {
  padding: 1rem;
}
</style>
