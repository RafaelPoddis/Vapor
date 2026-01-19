<template>
    <main>
        <div class="profile" v-if="!editMode">
            <div class="main-info" v-if="user">
                <img alt="User Avatar" class="user-avatar" :src="API_BASE_URL+avatar" width="200" height="200" />
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
                <img alt="User Avatar" class="user-avatar" :src="API_BASE_URL+avatar" width="75" height="75" />
                <h2>{{ user.username}}</h2>
            </div>
            <div class="editableContent">
                <div class="buttons" @click="changeWindow">
                    <button id="general" class="botoes">General</button>
                    <button id="avatar" class="botoes">Avatar</button>
                    <button id="teste2" class="botoes">Teste 2</button>
                    <button id="teste3" class="botoes">Teste 3</button>
                </div>
                <div class="separator">
                    <!-- Só pra separar -->
                </div>
                <div class="content" v-if="win === 'general'">
                    <h1>General</h1>
                    <div class="info-group">
                        <label for="nickname">Nickname</label>
                        <input type="text" id="nickname" name="nickname" v-model="username"/>
                    </div>
                    <div class="info-group">
                        <label for="about">About</label>
                        <textarea id="about" name="about" cols="50" rows="4" v-model="about"></textarea>
                    </div>
                </div>
                <div class="content" v-else-if="win === 'avatar'">
                    <h1>Avatar</h1>
                    <p>Customize your avatar here.</p>
                    <div class="editavatar"
                        @drag.prevent
                        @dragstart.prevent
                        @dragend.prevent
                        @dragover.prevent
                        @dragenter.prevent
                        @dragleave.prevent
                        @drop.prevent="handleDrop"
                        @click="$refs.arquivo.click()">
                        <p>Click or drag and drop to upload a new avatar</p>
                        <input type="file" ref="arquivo" @change="handleFileSelect" accept=".mp4, .jpg, .jpeg, .png" hidden />
                    </div>
                </div>
                <div class="content" v-else-if="win === 'teste2'">
                    <h1>Teste 2</h1>
                    <p>Content for Teste 2 window.</p>
                </div>
                <div class="content" v-else-if="win === 'teste3'">
                    <h1>Teste 3</h1>
                    <p>Content for Teste 3 window.</p>
                </div>
                <button id="editBtn" @click="saveProfile">Save Changes</button>
            </div>

        </div>
    </main>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Avatar from '@/assets/userimgs/avatar_test.png'
import axios from 'axios';

const editMode = ref(false);
const win = ref('general');

const user = ref(null)
const username = ref('');
const about = ref('');

const API_BASE_URL = "http://localhost:8000/testApp";
const avatar = ref(null);

onMounted(() => {
    document.title = "PROFILE";
    axios
        .get(`${import.meta.env.VITE_API_URL}/testApp/authenticateduser/`, {
            headers: {
                Authorization: `Token ${localStorage.getItem("token")}`
            }
        })
        .then((response) => {user.value = response.data
            username.value = response.data.username
            about.value = response.data.about
            avatar.value = response.data.avatar
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
    window.location.reload();
    editMode.value = false;
}

function changeWindow(event) {
    win.value = event.target.id;
}

function handleFiles(files) {
  if (!files || !files.length) {
    // console.warn("Nenhum arquivo recebido:", files);
    return;
  }

  const file = files[0];

  if (!file || !file.type) {
    // console.warn("Arquivo inválido:", file);
    return;
  }

  if (!file.type.startsWith("image/")) {
    alert("Só imagens são permitidas");
    return;
  }

  const formData = new FormData();
  formData.append("avatar", file);

  axios.put(`${import.meta.env.VITE_API_URL}/testApp/user/${user.value.id}/`, formData, {
    headers: {
      "Content-Type": "multipart/form-data"
    }
  });
}

function handleDrop(event) {
  handleFiles(event.dataTransfer.files);
}

function handleFileSelect(event) {
  handleFiles(event.target.files);
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
    transition: background-color 0.3s ease;
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
    height: 80%;
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 8px;
    margin-inline: 2rem;
}

.info-group{
    display: flex;
    flex-direction: column;
    margin-bottom: 1.5rem;
}

.content{
    flex-grow: 1;
    padding-right: 2rem;
}

.editavatar{
    width: 100%;
    height: 200px;
    background-color: #1B2838;
    border-radius: 8px;
    margin-top: 1rem;
    border: 2px dashed rgba(255, 255, 255, 0.3);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.3s ease;
}

.editavatar:hover,
.editavatar.dragging {
  background-color: rgba(255, 255, 255, 0.1);
}

textarea, input {
    background-color: #3a3a3a;
    color: white;
    border: 1px solid #5f5f5f;
    border-radius: 5px;
    resize: none;
}
</style>