<template>
    <main>
        <img class="cover-img" :src="GameImage">
        <div class="game-detail">
          <h1>{{ name }}</h1>
          <button class="play-btn">
            <i>
              <svg 
                xmlns="http://www.w3.org/2000/svg" 
                width="24" height="24" 
                viewBox="0 0 24 24" 
                fill="white" 
                stroke="currentColor" 
                stroke-width="2" 
                stroke-linecap="round" 
                stroke-linejoin="round" 
                class="lucide-play">
                <polygon points="6 3 20 12 6 21 6 3"/>
              </svg>
            </i>PLAY</button>
        </div>
      </main>
</template>

<script setup>
import GameImage from '@/assets/gamesImgs/gow.jpg'

defineProps({
    name: String,
    id: Number,
})
</script>

<style scoped>
main{
    display: flex;
    flex-direction: column;
    margin-top: 25px;
}

.cover-img{
  width: 1500px;
  height: 320px;
}

h1{
  font-weight: bold;
}

.play-btn{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  background-color: green;
  color: white;
  border-radius: 7px;
  border: none;
  width: 150px;
  height: 40px;
  font-size: x-large;
  cursor: pointer;
}

.game-detail{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  margin-top: 7px;
  margin-bottom: 15px;
}
</style>