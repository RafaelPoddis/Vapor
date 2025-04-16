<template>
    <div class="user-card">
        <div class="user-info">
            <img alt="User-Avatar" :src="GameImage" width="90" height="90">
            <p class="username">Username</p>
            <p class="num-reviews">53 reviews</p>
        </div>
        <div class="review-text">
            <p>Jogo foda, chega ser bizarroJogo foda, chega ser bizarro</p>
        </div>
    </div>
</template>

<script setup>
import GameImage from '@/assets/gamesImgs/gow.jpg'
</script>

<style scoped>

.user-card{
    display: flex;
    height: 200px;
}

.review-text{
    background-color: #3a3a3a;
    color: white;
    border: 1px solid #5f5f5f;
    border-radius: 5px;
    height: 160px;
    width: 500px;
    resize: none;
    margin: 20px;
}

.user-info{
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 90px;
    margin: 20px;
}

.username{
    font-size: 16px;
}

.num-reviews{
    font-size: 12px;
}
</style>