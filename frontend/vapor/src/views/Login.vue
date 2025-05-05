<template>
    <div class="general">
        <img alt="Vapor Logo" class="logo" :src="logo" width="55" height="55">
        <p class="title">VAPOR</p>
        <form class="login" @submit.prevent="handleLogin">
            <div class="content" v-if="hasAcc">
                <div class="container">
                    <label class="username" for="username">Username or email address</label>
                    <input type="text" v-model="username" required id="username" name="username">
                </div>
                <div class="container">
                    <div class="password-label">
                        <label class="password" for="password">Password</label>
                        <a href="#" class="forgot-password">Forgot password?</a>
                    </div>
                    <input type="password" v-model="password" required id="password" name="password">
                </div>
                <button class="login-btn" type="submit">Login</button>
            </div>
            <div class="content" v-else>
                <p>outro</p>
            </div>
        </form>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import logo from "@/assets/logo.svg";
import axios from 'axios';
import router from '@/router';

const hasAcc = ref(true)

const username = ref('')
const password = ref('')

function handleLogin() {
    console.log("entrou")
    axios
        .post('http://127.0.0.1:8000/testApp/user/authenticate/', { username:username.value, password:password.value })
        .then(response => {
            localStorage.setItem("token", response.data.token),
            router.back()
        })
}
</script>

<style scoped>
.general {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 60vh;
}

.title {
    font-size: x-large;
    font-family: "Stalinist One", sans-serif;
    color: white;
    margin-bottom: 30px;
}

.content {
    display: flex;
    flex-direction: column;
    gap: 25px;
    max-width: fit-content;
    border: 1px solid;
    border-radius: 8px;
    padding: 55px;
    background-color: #1B2838;
    border-color: #2b617c;
}

.container {
    display: flex;
    flex-direction: column;
    gap: 5px;
}

.password-label {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

input {
    background-color: #3a3a3a;
    color: white;
    border: 1px solid #5f5f5f;
    border-radius: 5px;
    height: 35px;
    width: 300px;
    resize: none;
}

.login-btn {
    cursor: pointer;
    color: white;
    font-weight: bolder;
    border-radius: 7px;
    height: 35px;
    background-color: rgb(14, 177, 14);
    border: none;
}
</style>