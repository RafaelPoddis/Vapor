<template>
  <NavBar />
  <form @submit.prevent="postGame" class="general">
    <div class="hasAccount" v-if="hasAccount">
      <div class="inputs">
        <div class="container">
          <label class="titles" for="title">Game Title</label>
          <textarea required class="text-box" v-model="gameName" id="title" placeholder="The Game" rows="1"></textarea>
        </div>
        <div class="container">
          <label class="titles" for="description">Description</label>
          <textarea required class="description-input" v-model="gameDescription" id="description" placeholder="Game description..." rows="5"></textarea>
        </div>
        <div class="container">
          <label class="titles" for="genre">Genre</label>
          <Multiselect 
            class="genres-input"
            v-model="selectedGenres"
            :options="gameGenres"
            :multiple="true"
            :taggable="true"
            placeholder="Browse Genres"
            label="name"
            track-by="name"
          />
        </div>
        <div class="container">
          <label class="titles" for="price">Price</label>
          <textarea required class="text-box" v-model="gamePrice" id="price" placeholder="R$ 0,00" rows="1"></textarea>
        </div>
        <div>
          <p class="titles">Content Rating</p>
          <div class="radios">
            <div class="checks">
              <input type="radio" v-model="isAdults" id="minor" :value="false" name="option" checked />
              <label for="minor">For Everyone</label>
            </div>
            <div class="checks">
              <input type="radio" v-model="isAdults" id="adult" :value="true" name="option" />
              <label for="adult">Adults Only</label>
            </div>
          </div>
        </div>
      </div>
  
      <div class="upload-section">
        <p class="titles">Upload your game media here</p>
        <div class="upload-area" 
          @drag.prevent
          @dragstart.prevent
          @dragend.prevent
          @dragover.prevent
          @dragenter.prevent
          @dragleave.prevent
          @drop.prevent="handleDrop"
          @click="$refs.arquivo.click()">
          <input type="file" ref="arquivo" @change="handleFileSelect" accept=".mp4, .jpg, .jpeg, .png" class="hidden" />
          <div class="upload-content">
            <i class="upload-icon">
              <svg xmlns="http://www.w3.org/2000/svg" width="110" height="110" viewBox="0 0 24 24" fill="none"
                stroke="currentColor" stroke-width="0.4" stroke-linecap="round" stroke-linejoin="round" class="up-icon">
                <path
                  d="M10.3 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v10l-3.1-3.1a2 2 0 0 0-2.814.014L6 21" />
                <path d="m14 19.5 3-3 3 3" />
                <path d="M17 22v-5.5" />
                <circle cx="9" cy="9" r="2" />
              </svg></i>
            <p class="upload-text">Drag&Drop your game media here</p>
          </div>
        </div>
        <button class="submit" type="submit">Publish Game</button>
      </div>
    </div>

    <div class="hasAccount" v-else>
      <div class="noAcc">
        <p class="warning">You need an<br>account to use<br>this feature.</p>
        <router-link to="/login" class="login-btn">Login</router-link>
      </div>
    </div>
  </form>
</template>

<script setup>
import NavBar from "@/components/NavBar.vue";
import { onMounted, ref } from 'vue';
import axios from "axios";
import Multiselect from "vue-multiselect";

const hasAccount = ref(true)
const gameName = ref('')
const gamePrice = ref('')
const gameDescription = ref('')
const isAdults = ref()
const gameMedia = ref([])
const gameGenres = ref([])
const selectedGenres = ref([])

onMounted(() => {
  axios
    .get('http://127.0.0.1:8000/testApp/genres/')
    .then(response => {gameGenres.value = response.data, console.log(response.data)})
})

function postGame(){
  axios
    .post('http://127.0.0.1:8000/testApp/games/', {name:gameName.value, price:gamePrice.value, description:gameDescription.value, genre_ids:gameGenres.value, isAdults:isAdults.value})
    .catch(error => console.log(error))
}
</script>

<style scoped lang="css">
.general {
  display: flex;
}

.hasAccount{
  display: flex;
}

.noAcc{
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 1920px;
}

.login-btn{
  color: white;
  font-weight: bolder;
  border-radius: 7px;
  height: 35px;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 250px;
  background-color: rgb(14, 177, 14);
  border: none;
}

.warning{
  display: flex;
  font-weight: bold;
  font-size:xx-large;
  text-align: center;
  margin-bottom: 30px;
}

.container {
  display: flex;
  flex-direction: column;
}

.inputs {
  width: 900px;
  margin-left: 60px;
  display: flex;
  flex-direction: column;
  gap: 64px;
}

.upload-section {
  width: 900px;
}

.submit {
  border-width: 1px;
  border-radius: 7px;
  border-color: aqua;
  background-color: #61acc0;
  color: white;
  height: 40px;
  width: 880px;
  cursor: pointer;
}

.titles {
  font-family: "Montserrat", sans-serif;
  font-size: 26px;
  font-weight: bold;
}

.text-box {
  background-color: #3a3a3a;
  color: white;
  border: 1px solid #5f5f5f;
  border-radius: 5px;
  height: 35px;
  width: 500px;
  resize: none;
}

:deep(.multiselect) {
  background-color: #3a3a3a;
  border: 1px solid #5f5f5f;
  border-radius: 8px;
  padding: 6px;
  width: 500px;
  color: #d1d5db;
  font-size: 14px;
}

:deep(.multiselect__input,
.multiselect__single) {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  outline: none !important;
  color: #d1d5db;
}

:deep(.multiselect__placeholder) {
  color: #5f5f5f;
  padding-left: 6px;
}

:deep(.multiselect__option--highlight) {
  background-color: #2c3e50;
  color: white;
}

:deep(.multiselect__option--selected) {
  background-color: #3b82f6;
  color: white;
}

:deep(.multiselect__tag) {
  display: flex;
  flex-direction: column;
  background-color: #3b82f6;
  color: white;
  border-radius: 4px;
  padding: 2px 6px;
  margin: 2px;
}

:deep(.multiselect__content-wrapper) {
  height: fit-content !important;
}

.description-input {
  background-color: #3a3a3a;
  color: white;
  border: 1px solid #5f5f5f;
  border-radius: 5px;
  height: 125px;
  width: 500px;
  resize: none;
}

.radios {
  display: flex;
  max-width: 300px;
  justify-content: space-between;
}

#minor,
#adult {
  margin-right: 4px;
}

.upload-area {
  margin: 40px auto;
  max-width: 700px;
  border: 2px dashed rgb(255, 255, 255, 0.3);
  border-radius: 8px;
  padding: 80px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.upload-area:hover,
.upload-area.dragging {
  border-color: rgba(255, 255, 255, 0.6);
  background-color: rgba(255, 255, 255, 0.1);
}

.upload-icon {
  font-size: 48px;
  margin-bottom: 16px;
}

.upload-text {
  color: rgba(255, 255, 255, 0.8);
}

.hidden {
  display: none;
}
</style>
