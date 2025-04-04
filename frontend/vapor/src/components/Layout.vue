<script setup>
import Header from "./Header.vue";

</script>

<template>
  <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" />
  <link href="https://fonts.googleapis.com/css?family=Stalinist One" rel="stylesheet" />
  <Header/>
  <div class="general">
    <router-view/>
  </div>
</template>
