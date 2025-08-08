<template>
  <NavBar/>
  <div class="section-title">
    <p class="title">New Releases</p>
  </div>
  <div class="games">
    <GameCard 
    v-for="game in games"
    :name="game.name"
    :price="game.price"
    :image="game.image"
    :id="game.id"
    />
  </div>
  <div class="section-title">
    <p class="title">Featured Games</p>
  </div>
  <div class="games">
    <GameCard 
    v-for="game in games"
    :name="game.name"
    :price="game.price"
    :id="game.id"
    :description="game.description"/>
  </div>
  <!-- <Footer/> -->
</template>

<script setup>
import GameCard from '@/components/GameCard.vue'
import Footer from '@/components/Footer.vue'
import NavBar from '@/components/NavBar.vue'
import { ref, onMounted } from 'vue'
import axios from 'axios'

const games = ref([])

onMounted(() => {
  document.title = "STORE";
  axios
    .get(`${import.meta.env.VITE_API_URL}/testApp/games`)
    .then(response => {games.value = response.data});
})

defineProps({
  name: String,
  price: Number,
  image: String,
  id: Number
})
</script>

<style scoped>
.games{
  padding-inline: 50px;
  display: flex;
  flex-wrap: wrap;
}

.section-title{
  margin-left: 85px;
}

.title{
  font-family: 'Montserrat', sans-serif;
  font-size: 26px;
  font-weight: bold;
}
</style>