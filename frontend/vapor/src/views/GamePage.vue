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
    </div>
</template>

<script setup>
import NavBar from '@/components/NavBar.vue';
import GameImage from '@/assets/gamesImgs/gow.jpg'
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
</style>