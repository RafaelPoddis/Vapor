<template>
  <NavBar/>
  <div class="section-title">
    <p class="title">New Releases</p>
  </div>
  <div class="games">
    <GameCard name="God of War" price="$250.00"/>
    <GameCard name="Jogo 2" price="$250.00"/>
    <GameCard name="Jogo 3" price="$250.00"/>
    <GameCard name="Jogo 4" price="$250.00"/>
    <GameCard name="Jogo 5" price="$250.00"/>
    <GameCard name="Jogo 6" price="$250.00"/>
    <GameCard name="Jogo 7" price="$250.00"/>
    <GameCard name="Jogo 8" price="$250.00"/>
    <GameCard name="Jogo 9" price="$250.00"/>
    <GameCard 
      v-for="game in games"
      :name="game.name"
      :price="game.price"
      :image="game.image"
    />
  </div>
  <div class="section-title">
    <p class="title">Featured Games</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import GameCard from '@/components/GameCard.vue'
import NavBar from '@/components/NavBar.vue'

const games = ref([
  { id: 1, name: "God of War", price: "$250.00", image: "C:\\Users\\Rafael\\Documents\\VaporProject\\backend\\media\\games\\3\\media\\test1.jpeg" },
  { id: 2, name: "Jogo 2", price: "$150.00", image: "C:\\Users\\Rafael\\Documents\\VaporProject\\backend\\media\\games\\4\\media\\test2.png" },
  { id: 3, name: "Jogo 3", price: "$100.00", image: "C:\\Users\\Rafael\\Documents\\VaporProject\\backend\\media\\games\\4\\media\\test3.png" }
])

defineProps({
  name: String,
  price: String,
  image: String
})
</script>

<style scoped>
.games{
  padding-inline: 60px;
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