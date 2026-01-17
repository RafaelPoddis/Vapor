<template>
    <main>
        <div class="profile" v-if="!editMode">
            <div class="main-info" v-if="user">
                <img alt="User Avatar" class="user-avatar" :src="Avatar" width="200" height="200" />
                <div class="info">
                    <h2>{{ user.username }}</h2>
                    <textarea class="text-info" disabled cols="50" rows="4">{{ user.about }}</textarea>
                </div>
                <div class="level">
                    <h2>Level {{ user.level }}</h2>
                    <button id="editBtn" @click="editMode=true">Edit Profile</button>
                </div>
            </div>
            <div class="activity">
                <div class="recent-activities">
                    <h1>Recent Activity</h1>
                </div>
            </div>
        </div>
        <div class="edit-mode" v-else>
            <div class="someInfo">
                <img alt="User Avatar" class="user-avatar" :src="Avatar" width="75" height="75" />
                <h2>Username</h2>
            </div>
            <div class="editableContent">
                <div class="buttons">
                    <button class="botoes">General</button>
                    <button class="botoes">Teste</button>
                    <button class="botoes">Teste</button>
                    <button class="botoes">Teste</button>
                </div>
                <div class="separator">
                    <!-- Só pra separar -->
                </div>
                <div>
                    <h1>General</h1>
                    <div class="info-group">
                        <label for="nickname">Nickname</label>
                        <input type="text" id="nickname" name="nickname" v-model="username"/>
                    </div>
                    <div class="info-group">
                        <label for="about">About</label>
                        <textarea id="about" name="about" cols="50" rows="4" v-model="about"></textarea>
                    </div>
                    <button id="editBtn" @click="saveProfile">Save Changes</button>
                </div>
            </div>

        </div>
    </main>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Avatar from '@/assets/userimgs/avatar_test.png'
import axios from 'axios';
import { useRoute } from 'vue-router';

const profileInfo = ref('');

const editMode = ref(false);

const user = ref(null)
const username = ref('');
const about = ref('');

onMounted(() => {
    document.title = "PROFILE";
    // console.log("Fetching profile for user ID:", userId.value);
    axios
        .get(`${import.meta.env.VITE_API_URL}/testApp/authenticateduser/`, {
            headers: {
                Authorization: `Token ${localStorage.getItem("token")}`
            }
        })
        .then((response) => {user.value = response.data
            username.value = response.data.username
            about.value = response.data.about
        })
        .catch((error) => {
            console.error("There was an error fetching the user data:", error);
        });
})

function saveProfile() {
    // Lógica para salvar as alterações do perfil
    axios
        .put(`${import.meta.env.VITE_API_URL}/testApp/user/${user.value.id}/`, {
            username: username.value,
            about: about.value,
        },
        {
            headers: {
                Authorization: `Token ${localStorage.getItem("token")}`
            }
        })
        .then((response) => {
            console.log("Profile updated successfully:", response.data)
        })
        .catch((error) => {
            console.error("There was an error updating the profile:", error.response.data);
        });
    editMode.value = false;
}

defineProps({
    username: {
        type: String,
        default: 'Username'
    },
    level: {
        type: Number,
        default: 1
    },
    about: {
        type: String,
        default: ''
    },
})
</script>

<style scoped>
main {
    display: flex;
    justify-content: center;
    
    margin-top: 100px;
}

.main-info{
    display: flex;
    gap: 15px;
    margin-top: 1.5rem;
    margin-bottom: 3rem;
    width: 1200px;
}

.info{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    max-width: 300px;
}

.text-info{
    background: transparent;
    color: rgba(235, 235, 235, 0.64);
    border: none;
    padding: 5px;
    font-family: "Montserrat", sans-serif;
    resize: none;
}

.level{
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin-left: 33rem;
}

#editBtn{
    width: 120px;
    height: 40px;
    border: 1px solid #2b617c;
    background-color: #1B2838;
    border-radius: 8px;
    color: white;
    font-family: "Montserrat", sans-serif;
    cursor: pointer;
}

#editBtn:hover{
    background-color: #273647;
}

textarea{
    text-wrap: wrap;
    overflow-wrap: break-word;
}

.someInfo{
    display: flex;
    align-items: center;
    background-color: #1B2838;
    width: 62rem;
    gap: 1rem;
    padding: 1rem;
}

.editableContent{
    display: flex;
    margin-top: 2rem;
    height: 70vh;
    /* background-color: antiquewhite; */
}

.buttons{
    display: flex;
    flex-direction: column;
    gap: 1rem;
    width: 10rem;
}

.botoes{
    background: none;
    color: rgba(235, 235, 235, 0.64);
    border: none;
    border-radius: 8px;
    font-family: "Montserrat", sans-serif;
    height: 2rem;
    text-align: left;
    transition: opacity 0.3s ease;
}

.botoes:hover{
    color: white;
    cursor: pointer;
    border-radius: 8px;
    background-color: #1B2838;
}

.botoes:active{
    opacity: 0.6;
}

.separator{
    height: 100%;
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 8px;
    margin-inline: 2rem;
}

.info-group{
    display: flex;
    flex-direction: column;
    margin-bottom: 1.5rem;
}

textarea, input {
    background-color: #3a3a3a;
    color: white;
    border: 1px solid #5f5f5f;
    border-radius: 5px;
    resize: none;
}
</style>