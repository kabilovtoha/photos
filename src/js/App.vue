<template>
  <component :is="layout" />
</template>

<script>

import ContentLayout from './layout/ContentLayout.vue';

export default {
  name: 'App',
  components: {
    ContentLayout,
  },
  computed: {
    layout() {
      return ContentLayout;
    },
  },
  mounted() {
  },
  methods: {
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

input,
i,
a {
  outline: none;
  text-decoration: none;
}

@import '~bootstrap/dist/css/bootstrap.min.css';
@import './assets/style/css/style.css';
</style>
