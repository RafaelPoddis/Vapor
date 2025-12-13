<template>
    <div class="general">
        <div class="profile">
            <div class="main-info">
                <img alt="User Avatar" class="user-avatar" :src="Avatar" width="200" height="200" />
                <div class="info">
                    <h2>Username</h2>
                    <p>InfoInfoInfoInfoInfoInfoInfoInfoInfoInInfoInfoInfoInfoInfoInfoInfoInfoInfoInfoInfoInfovfoInfoInfoInfoInfoInfoInfoInfoInfoInfoInfoInfoInfoInfoInfo</p>
                </div>
                <h2 class="level">Level 600</h2>
            </div>
            <div class="activity">
                <div class="recent-activities">
                    <h1>Recent</h1>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Avatar from '@/assets/userimgs/avatar_test.png'
import axios from 'axios';
import { useRoute } from 'vue-router';

const user = ref()

const route = useRoute()
const userId = route.params.id

onMounted(() => {
  document.title = "PROFILE";
})
</script>

<style scoped>
.general {
    display: flex;
    justify-content: center;
    
    margin-top: 100px;
}

.main-info{
    display: flex;
    gap: 15px;
    margin-top: 25px;
    width: 1200px;
}

.info{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    max-width: 300px;
}

.level{
    margin-left: 550px;
}

p{
    text-wrap: wrap;
    overflow-wrap: break-word;
}
</style>