<template>
    <router-link :to="`/store/gamepage/${ id }`">
        <div class="jogo">
            <img alt="Game Image" class="gameImg" :src="image" width="200" height="200" />
            <div class="gameInfo">
                <p>{{ name }}</p>
                <p>${{ price }}</p>
            </div>
        </div>
    </router-link>
</template>

<script setup>

defineProps({
  name: String,
  price: Number,
  image: String,
  id: Number,
  description: String
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

.jogo{
    transition: transform 0.3s ease;
}

.jogo:hover {
  transform: scale(1.1);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.4);
  border-radius: 8px;
}
</style>