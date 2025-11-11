<template>
  <div class="general">
    <div class="game-list">
      <h2 margin-bottom="15px">Your Games</h2>
      <input class="search-input">
      <div class="game-name" @click="selectGame(game)" v-for="game in games" :name="game.name">
        <p>{{ game.name }}</p>
      </div>
    </div>

    <div class="content" v-if="!gameSelected">
      <h2>Recently Played</h2>
      <div class="games">
        <LibraryGameCard @click="selectGame(game)" v-for="game in games"
        :name="game.name"
        />
      </div>
    </div>
    <div class="content" v-else>
      <GameInfo :name="selectedGame.name" :id="selectedGame.id"/>
      <div class="achievements">
        <h2>Achievements</h2>
        <div class="progression">
          <div class="text">
            <p>25 / 100 achieved (25%)</p>
          </div>
          <div class="progress-bar">
            <div class="inner-progress-bar"></div>
          </div>
        </div>
      </div>
      <button class="back-btn" @click="deselectGame">Back</button>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import GameInfo from '../components/GameInfo.vue'
import GameImage from '@/assets/gamesImgs/gow.jpg'
import LibraryGameCard from '@/components/LibraryGameCard.vue'

const gameSelected = ref(false)
const selectedGame = ref(null)

onMounted(() => {
  document.title = "LIBRARY";
})

defineProps({
  achievements: Number,
})

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

function selectGame(game) {
  selectedGame.value = game
  gameSelected.value = true
  document.title = `LIBRARY - ${selectedGame.value.name}`;
}

function deselectGame() {
  selectedGame.value = null
  gameSelected.value = false
  document.title = "LIBRARY";
}

</script>

<style scoped>
.general{
  display: flex;
  max-width: 1900px;
}

.game-list{
  background-color: #171d259a;
  width: 380px;
  padding-left: 10px;
  min-height: 100vh;
}

.content{
  margin-left: 25px;
}

.games{
  display: flex;
  flex-wrap: wrap;
}

.game-name:hover{
  background-color: #171d25;
  cursor: pointer;
}

.back-btn{
  border-radius: 7px;
  border: none;
  background-color: #61ACC0;
  color: white;
  height: 30px;
  cursor: pointer;
  margin-top: 15px;
}

.search-input{
  background-color: #3a3a3a;
  color: white;
  border: 1px solid #5f5f5f;
  border-radius: 5px;
  height: 28px;
  margin-bottom: 10px;
}

.progression{
  display: flex;
  flex-direction: column;
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 7px;
  max-width: 225px;
  background-color: rgb(58, 58, 58);
  gap: 7px;
}

.progress-bar{
  border-radius: 15px;
  height: 12px;
  background-color: rgb(143, 143, 143);
}

.inner-progress-bar{
  border-radius: 15px;
  height: 12px;
  background-color: #2d40aa;
  width: 25%;
}
</style>