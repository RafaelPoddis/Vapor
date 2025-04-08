<template>
  <header class="top">
    <div class="brand">
      <img alt="Vapor Logo" class="logo" :src="logo" width="55" height="55">
      <router-link to="/" class="title">VAPOR</router-link>
    </div>
    <div class="pages">
      <router-link to="/" class="nav-link" exact-active-class="active">STORE</router-link>
      <router-link to="/library" class="nav-link" exact-active-class="active">LIBRARY</router-link>
    </div>
  </header>
</template>

<script setup>
import logo from "@/assets/logo.svg";
</script>

<style scoped>
.top {
  display: flex;
  background-color: #171d25;
  height: 100px;
}

.pages {
  display: flex;
  margin-left: 35rem;
  justify-content: right;
  align-items: center;
}

.brand {
  display: flex;
  justify-content: left;
  align-items: center;
}

.title {
  font-size: x-large;
  font-family: "Stalinist One", sans-serif;
}

.logo {
  margin: auto 1rem;
  margin-left: 5rem;
}

.active{
  color: #4B8AF8;
}
</style>
