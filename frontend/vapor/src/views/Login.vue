<template>
    <div class="general">
        <div class="content" v-if="login">
            <p>algo</p>
        </div>
        <div class="content" v-else>
            <p>outro</p>
        </div>
    </div>
</template>

<script setup>
import {ref} from 'vue'

const login = ref(false)
</script>

<style scoped>
</style>