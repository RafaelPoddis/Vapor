<template>
    <div class="general">
        <div class="profile" v-if="logged">
            <p>Logado</p>
        </div>
        <div class="profile" v-else>
            <p>Not logged</p>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const logged = ref(true)
</script>

<style scoped>
.general{
    display: flex;
    justify-content: center;
}
</style>