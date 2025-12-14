<script setup>
import Header from "./Header.vue";
import Footer from "./Footer.vue";

</script>

<template>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Stalinist One" rel="stylesheet" />
  <Header/>
  <router-view/>
  <Footer/>
</template>

<style scoped>

</style>