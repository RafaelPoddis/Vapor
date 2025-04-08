<template>
  <NavBar/>
  <div class="general">
    <div class="inputs">
      <div class="container">
        <label class="titles" for="title">Game Title</label>
        <textarea class="text-box" id="title" placeholder="The Game" rows="1"></textarea>
      </div>
      <div class="container">
        <label class="titles" for="description">Description</label>
        <textarea class="description-input" id="description" placeholder="Game description..." rows="5"></textarea>
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
            <input type="radio" id="minor" value="minor" checked />
            <label for="minor">For Everyone</label>
          </div>
          <div class="checks">
            <input type="radio" id="adult" value="adult" />
            <label for="adult">Adults Only</label>
          </div>
        </div>
      </div>
    </div>
    
    <div class="upload-media">
      <p> media duahduaisgdsa</p>
    </div>
  </div>
</template>

<script setup>
import NavBar from '@/components/NavBar.vue';
</script>

<style scoped>
.general{
  display: flex;
}

.container{
  display: flex;
  flex-direction: column;
}
.inputs{
  width: 900px;
  margin-left: 60px;
  display: flex;
  flex-direction: column;
  gap: 64px;
}

.upload-media{
  width: 900px;
  margin-right: 60px;
}

.titles{
  font-family: 'Montserrat', sans-serif;
  font-size: 26px;
  font-weight: bold;
}

.text-box{
  background-color: #3a3a3a;
  color: white;
  border: 1px solid #5F5F5F;
  border-radius: 5px;
  height: 35px;
  width: 500px;
}

.description-input{
  background-color: #3a3a3a;
  color: white;
  border: 1px solid #5F5F5F;
  border-radius: 5px;
  height: 125px;
  width: 500px;
}

.radios{
  display: flex;
  max-width: 300px;
  justify-content: space-between;
}

#minor, #adult{
  margin-right: 4px;
}
</style>