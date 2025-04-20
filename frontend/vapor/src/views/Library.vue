<template>
  <div class="general">
    <div class="game-list">
      <h2 margin-bottom="15px">Your Games</h2>
      <router-link :to="`/library/gameinfo/${ id }`" v-for="game in games" :name="game.name">
        <p>{{ game.name }}</p>
      </router-link>
    </div>

    <div class="content">
      <h2>Recently Played</h2>
      <div class="games">
        <GameCard v-for="game in games"
        :name="game.name"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import GameCard from '@/components/GameCard.vue'
import GameImage from '@/assets/gamesImgs/gow.jpg'

const games = ref([
  { id: 1, name: "God of War", price: "$250.00", image: GameImage },
  { id: 2, name: "Jogo 2", price: "$150.00", image: GameImage},
  { id: 3, name: "Jogo 3", price: "$100.00", image: GameImage },
  { id: 4, name: "God of War 2", price: "$350.00", image: GameImage },
  { id: 5, name: "Jogo 4", price: "$68.00", image: GameImage },
  { id: 6, name: "Jogo 5", price: "$10.00", image: GameImage },
  { id: 7, name: "God of War 3", price: "$20.00", image: GameImage },
  { id: 8, name: "Jogo 6", price: "$124.00", image: GameImage },
  { id: 9, name: "Jogo 7", price: "$1.50", image: GameImage },
])

</script>

<style scoped>
.general{
  display: flex;
  max-width: 1900px;
  margin-inline: 10px;
}

.game-list{
  width: 380px;
}

.content{
  margin-left: 25px;
}

.games{
  display: flex;
  flex-wrap: wrap;
}
</style>