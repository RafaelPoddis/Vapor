<template>
    <router-link :to="`gamepage/${ id }`">
        <div class="jogo">
            <img alt="Game Image" class="gameImg" :src="GameImage" width="200" height="200" />
            <div class="gameInfo">
                <p>{{ name }}</p>
                <p>{{ price }}</p>
            </div>
        </div>
    </router-link>
</template>

<script setup>
import GameImage from '@/assets/gamesImgs/gow.jpg'

defineProps({
  name: String,
  price: String,
  image: String,
  id: Number
})
</script>

<style scoped>
.jogo{
    margin: 23px;
    max-width: 200px;
    max-height: 235px;
}

.gameInfo{
    display: flex;
    justify-content: space-between;
    align-items: center;
}
</style>