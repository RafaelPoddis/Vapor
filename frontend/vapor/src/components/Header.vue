<template>
  <header>
    <div class="brand">
      <img alt="Vapor Logo" class="logo" :src="logo" width="55" height="55">
      <router-link to="/store" class="title">VAPOR</router-link>
    </div>
    <div class="pages">
      <router-link to="/store" class="nav-link" active-class="active">STORE</router-link>
      <router-link to="/library" class="nav-link" active-class="active">LIBRARY</router-link>
      <router-link to="/profile" class="nav-link" active-class="active">PROFILE</router-link>
    </div>
    <div class="login">
      <router-link to="/login" class="nav-link">Login</router-link>
    </div>
  </header>
</template>

<script setup>
import logo from "@/assets/logo.svg";
</script>

<style scoped>
header {
  display: flex;
  /* Fixo no topo */
  position: fixed;
  top: 0;

  background-color: #171d25;
  height: 100px;
  width: 100%;
  align-items: center;
}

.pages {
  display: flex;
  margin-left: 35rem;
  margin-right: 35rem;
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

.login{
  margin-left: 8rem;
}

.active{
  color: #4B8AF8;
  text-decoration: underline;
}
</style>
