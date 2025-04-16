<template>
  <NavBar />
  <form class="general" onsubmit="funcao">
    <div class="inputs">
      <div class="container">
        <label class="titles" for="title">Game Title</label>
        <textarea class="text-box" id="title" placeholder="The Game" rows="1"></textarea>
      </div>
      <div class="container">
        <label class="titles" for="description">Description</label>
        <textarea
          class="description-input"
          id="description"
          placeholder="Game description..."
          rows="5"
        ></textarea>
      </div>
      <div class="container">
        <label class="titles" for="genre">Genre</label>
        <textarea class="text-box" id="Genre" placeholder="Browse Genres" rows="1"></textarea>
      </div>
      <div class="container">
        <label class="titles" for="price">Price</label>
        <textarea class="text-box" id="price" placeholder="R$ 0,00" rows="1"></textarea>
      </div>
      <div>
        <p class="titles">Content Rating</p>
        <div class="radios">
          <div class="checks">
            <input type="radio" id="minor" value="minor" name="option" checked />
            <label for="minor">For Everyone</label>
          </div>
          <div class="checks">
            <input type="radio" id="adult" value="adult" name="option" />
            <label for="adult">Adults Only</label>
          </div>
        </div>
      </div>
    </div>

    <div class="upload-section">
      <p class="titles">Upload your game media here</p>
      <div
        class="upload-area"
        @drag.prevent
        @dragstart.prevent
        @dragend.prevent
        @dragover.prevent
        @dragenter.prevent
        @dragleave.prevent
        @drop.prevent="handleDrop"
        :class="{ dragging: isDragging }"
        @click="$refs.arquivo.click()"
      >
        <input type="file" ref="arquivo" @change="handleFileSelect" accept=".pdf" class="hidden" />
        <div class="upload-content">
          <i class="upload-icon"
            ><svg
              xmlns="http://www.w3.org/2000/svg"
              width="110"
              height="110"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="0.4"
              stroke-linecap="round"
              stroke-linejoin="round"
              class="up-icon"
            >
              <path
                d="M10.3 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v10l-3.1-3.1a2 2 0 0 0-2.814.014L6 21"
              />
              <path d="m14 19.5 3-3 3 3" />
              <path d="M17 22v-5.5" />
              <circle cx="9" cy="9" r="2" /></svg
          ></i>
          <p class="upload-text">
            Drag&Drop your game media here
          </p>
        </div>
      </div>
      <button type="submit">Salve</button>
    </div>
  </form>
</template>

<script setup>
import NavBar from "@/components/NavBar.vue";
</script>

<style scoped>
.general {
  display: flex;
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
  margin-right: 60px;
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
