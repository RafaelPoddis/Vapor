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
    :id="game.id"/>
  </div>
</template>

<script setup>
import GameCard from '@/components/GameCard.vue'
import NavBar from '@/components/NavBar.vue'
import { ref, onMounted } from 'vue'
import axios from 'axios'

const games = ref([])

onMounted(() => {
  axios
    .get('http://127.0.0.1:8000/testApp/games', {headers: {'Authorization': 'Token f70f5d2b34439fac015e2a3dce56f4485aaa681f'}})
    .then(response => {games.value = response.data})
})

// const games = ref([
//   { id: 1, name: "God of War", price: "$250.00", image: "C:\\Users\\Rafael\\Documents\\VaporProject\\backend\\media\\games\\3\\media\\test1.jpeg" },
//   { id: 2, name: "Jogo 2", price: "$150.00", image: "C:\\Users\\Rafael\\Documents\\VaporProject\\backend\\media\\games\\4\\media\\test2.png" },
//   { id: 3, name: "Jogo 3", price: "$100.00", image: "C:\\Users\\Rafael\\Documents\\VaporProject\\backend\\media\\games\\4\\media\\test3.png" },
//   { id: 4, name: "God of War 2", price: "$350.00", image: "C:\\Users\\Rafael\\Documents\\VaporProject\\backend\\media\\games\\3\\media\\test1.jpeg" },
//   { id: 5, name: "Jogo 4", price: "$68.00", image: "C:\\Users\\Rafael\\Documents\\VaporProject\\backend\\media\\games\\4\\media\\test2.png" },
//   { id: 6, name: "Jogo 5", price: "$10.00", image: "C:\\Users\\Rafael\\Documents\\VaporProject\\backend\\media\\games\\4\\media\\test3.png" },
//   { id: 7, name: "God of War 3", price: "$20.00", image: "C:\\Users\\Rafael\\Documents\\VaporProject\\backend\\media\\games\\3\\media\\test1.jpeg" },
//   { id: 8, name: "Jogo 6", price: "$124.00", image: "C:\\Users\\Rafael\\Documents\\VaporProject\\backend\\media\\games\\4\\media\\test2.png" },
//   { id: 9, name: "Jogo 7", price: "$1.50", image: "C:\\Users\\Rafael\\Documents\\VaporProject\\backend\\media\\games\\4\\media\\test3.png" },
// ])

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