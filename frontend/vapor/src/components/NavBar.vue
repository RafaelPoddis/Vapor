<template>
    <div class="navigation">
        <nav>
        <router-link to="/store" class="nav-link" exact-active-class="active">Home Page</router-link>
        <router-link to="/store/uploadGame" class="nav-link" exact-active-class="active">Upload Game</router-link>
        </nav>
    </div>
</template>

<style scoped>
.navigation{
  display: flex;
  margin-top: 140px;
  margin-inline: 640px;
  margin-bottom: 40px;
  width: 640px;
  height: 35px;
  background-image: radial-gradient(#679FFF, #2C5192);
  justify-content: center;
  align-items: center;
  border-radius: 8px;
}

.active{
    font-weight: bold;
}
</style>