<template>
  <div class="about">
    <!-- <input v-model="this.info" placeholder="Type something..." /> -->
     <!-- <button type="button" v-on:click='console.log("yup kuch toh hhya")' @mouseleave="console.log('bye dua m eyad rakhna')"  >Try it</button> -->
    <h1>{{ this.info }}</h1>
    <br>
    <br>
    <input type="text" v-model="this.State" placeholder="Enter shhhh to get special message" />
    <br>
    <br>
    <button type="button" @click="this.fetchTheMessage(this.State)">Get the message</button>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'AboutView',
  data() {
    return {
      info: null,
      State: '',
    };
  },
  methods: {
    fetchTheMessage(state) {
      if (state === "shhhh") {
        this.info = "Kya bolti public, welcome to LookBack App!";
      } else {
      this.info = "This is the About page of the LookBack App!";
      }
    }
  }

};
</script>
<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
