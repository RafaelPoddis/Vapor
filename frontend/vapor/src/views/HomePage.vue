<template>
  <div class="navigation">
    <nav>
      <router-link to="/" class="nav-link">Home Page</router-link>
      <router-link to="/uploadgame" class="nav-link">Upload Game</router-link>
    </nav>
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
</template>

<script setup>
import { ref } from 'vue'
import GameCard from '@/components/GameCard.vue'

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
.navigation{
  display: flex;
  margin-inline: 640px;
  margin-block: 40px;
  width: 640px;
  height: 35px;
  background-image: radial-gradient(#679FFF, #2C5192);
  justify-content: center;
  align-items: center;
}

.games{
  padding-inline: 60px;
  display: flex;
  flex-wrap: wrap;
}
</style>