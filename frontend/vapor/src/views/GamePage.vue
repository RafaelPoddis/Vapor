<template>
    <NavBar/>
    <div class="general">
        <div class="media-section">
            <img alt="Game Image" class="gameImg" :src="GameImage" width="720" height="360" />
            <div class="game-info">
                <p>DescriptionDescriptionDescription<br>
                    DescriptionDescriptionDescription<br>
                    Description</p>
            </div>
        </div>
        <div class="user-review-section" v-if="!userReview">
            <p>algo sendo mostrado</p>
        </div>
        <div class="reviews" v-if="gameReview">
            <div class="container">
                <div class="player-info">
                    <img alt="Player Avatar" class="player-avatar" :src="GameImage" width="96" height="96" />
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import NavBar from '@/components/NavBar.vue';
import GameImage from '@/assets/gamesImgs/gow.jpg'
import { ref } from 'vue'

const userReview = ref(true)
const gameReview = ref(true)

</script>

<style scoped>
.general{
    margin-inline: 200px;
    max-width: 1520px;
}

.media-section{
    margin: 40px;
    display: flex;
}

.game-info{
    margin-left: 40px;
}

.user-review-section{
    background-color: blue;
}
</style>