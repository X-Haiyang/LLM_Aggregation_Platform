<!--<template>-->
<!--  <img alt="Vue logo" src="./assets/logo.png">-->
<!--  <HelloWorld msg="Welcome to Your Vue.js App"/>-->
<!--</template>-->

<!--<script>-->
<!--import HelloWorld from './components/HelloWorld.vue'-->

<!--export default {-->
<!--  name: 'App',-->
<!--  components: {-->
<!--    HelloWorld-->
<!--  }-->
<!--}-->
<!--</script>-->

<!--<style>-->
<!--#app {-->
<!--  font-family: Avenir, Helvetica, Arial, sans-serif;-->
<!--  -webkit-font-smoothing: antialiased;-->
<!--  -moz-osx-font-smoothing: grayscale;-->
<!--  text-align: center;-->
<!--  color: #2c3e50;-->
<!--  margin-top: 60px;-->
<!--}-->
<!--</style>-->

<template>
  <div id="app">
    <h1>LLM Response Viewer</h1>
    <form @submit.prevent="submitForm">
      <input v-model="prompt" placeholder="Enter your prompt here" />
      <button type="submit">Submit</button>
    </form>
    <div v-if="responses.length > 0">
      <h2>Responses:</h2>
      <ul>
        <li v-for="(response, index) in responses" :key="index">{{ response }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      prompt: '',
      responses: []
    };
  },
  methods: {
    async submitForm() {
      try {
        const response = await axios.post('/api/llm', { prompt: this.prompt });
        this.responses = response.data;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }
  }
};
</script>