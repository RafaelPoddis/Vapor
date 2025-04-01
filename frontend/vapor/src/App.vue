<script setup>
import { ref } from 'vue'

const count = ref("Essa")

function funcao(){
  if (count.value === "Essa"){
    count.value = "Aquela"
  }
  else{
    count.value = "Essa"
  }
}
</script>

<template>
  <link href='https://fonts.googleapis.com/css?family=Montserrat' rel='stylesheet'>
  <link href='https://fonts.googleapis.com/css?family=Stalinist One' rel='stylesheet'>
  <div class="top">
    <div class="brand">
      <img alt="Vapor Logo" class="logo" src="./assets/logo.svg" width="55" height="55">
      <a class="title" href="App.vue">VAPOR</a>
    </div>
    <div class="pages">
      <a class="store-link" href="./HelloWorld.vue">STORE</a>
      <a class="library-link" href="./TheWelcome.vue">LIBRARY</a>
    </div>
  </div>
  <div>
    <p>Menssagem: {{ count }}</p>
    <button @click="funcao">Clica eu</button>
  </div>
</template>

<style scoped>
.top{
  display: flex;
  background-color: #171D25;
  height: 100px;
}

.pages{
  display: flex;
  margin-left: 35rem;
  justify-content: right;
  align-items: center;
}

.brand{
  display: flex;
  justify-content: left;
  align-items: center;
}

.title{
  font-size: x-large;
  font-family: 'Stalinist One', sans-serif;
}

.logo{
  margin: auto 1rem;
  margin-left: 5rem;
}

</style>
