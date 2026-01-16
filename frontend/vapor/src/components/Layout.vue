<script setup>
import Header from "./Header.vue";
import Footer from "./Footer.vue";

</script>

<template>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Stalinist One" rel="stylesheet" />
  <Header/>
  <main>
    <router-view/>
  </main>
  <Footer/>
</template>

<style scoped>
main {
  flex: 1;
}
</style>