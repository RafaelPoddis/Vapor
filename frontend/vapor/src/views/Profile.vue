<template>
    <div class="general">
        <div class="profile" v-if="logged">
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
        <div class="profile" v-else>
            <p>Not logged</p>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Avatar from '@/assets/userimgs/avatar_test.png'
import axios from 'axios';
import { useRoute } from 'vue-router';

const logged = ref(true)

const user = ref()

const route = useRoute()
const userId = route.params.id

// onMounted(() => {
//     if (!auth.isLoggedIn()) {
//         // Temporário: fazer login automático para desenvolvimento
//         auth.login('123', '648a4b0e40fe9e02f1a091d24f395bc5be780516');
//     }

//     logged.value = auth.isLoggedIn();

//     if (logged.value) {
//         const userId = auth.getUserId();

//         axios
//             .get(`http://127.0.0.1:8000/testApp/user/${userId}`, {
//                 headers: { 'Authorization': `Token ${auth.getToken()}` }
//             })
//             .then(response => {
//                 user.value = response.data;
//             })
//             .catch(error => {
//                 console.error("Erro ao buscar usuário:", error);
//                 logged.value = false;
//             });
//     }
// })
</script>

<style scoped>
.general {
    display: flex;
    justify-content: center;
    
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