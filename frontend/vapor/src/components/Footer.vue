<template>
    <footer>
        <img alt="Vapor Logo" class="logo" :src="logo" width="100" height="100">
    </footer>
</template>

<script setup>
import logo from "@/assets/valvulalogo.png";
</script>

<style scoped>
footer {
    background-color: #171d25;
    height: 125px;
    display: flex;
    position: fixed;
    bottom: 0;
    width: 100%;
}
</style>