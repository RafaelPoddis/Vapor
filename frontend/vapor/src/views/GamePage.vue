<template>
    <title v-if="game">{{ game.name }}</title>
    <NavBar/>
    <div class="general" v-if="game">
        <div class="media-section">
            <div class="img-title">
                <img alt="Game Image" class="gameImg" :src="game.image" width="720" height="360" />
                <div class="game-title">
                    <h1 v-if="game">{{ game.name }}</h1>
                </div>
            </div>
            <div class="game-info">
                <p>{{ game.description }}</p>
                <p>Price:  ${{ game.price }}</p>
            </div>
        </div>
        <div class="user-review" v-if="!userReview">
            <form @submit="postReview" class="post-review">
                <div class="picture">
                    <img alt="UserAvatar" class="user-avatar" :src="GameImage" width="150" height="150">
                    <textarea class="algo" placeholder="Write something about this game..." rows="3"></textarea>
                </div>
                <div class="buttons">
                    <div class="question">
                        <label class="question" for="answer">Do you recommend this game?</label>
                        <div class="quest-buttons">
                            <button class="yes-button" type="button">Yes</button>
                            <button class="no-button" type="button">No</button>
                        </div>
                    </div>
                    <div class="stars">
                        <button v-for="(star, index) in 5" :key="index" 
                        class="star-btn"
                        @mouseover="hoverIndex = index"
                        @mouseleave="hoverIndex = -1">
                            <svg 
                            xmlns="http://www.w3.org/2000/svg"
                            width="24" height="24" 
                            viewBox="0 0 24 24" 
                            fill="none"
                            :class="{ filled: index <= hoverIndex }"
                            stroke="#A0AAB1" 
                            stroke-width="1" 
                            stroke-linecap="round" 
                            stroke-linejoin="round" 
                            class="lucide-star">
                            <path d="M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z"/></svg></button>                        
                    </div>
                    <button class="submit" type="submit">Publish Review</button>
                </div>
            </form>
        </div>
        <div class="user-review" v-else>Nao</div>
        <div class="game-reviews" v-if="hasReviews">
            <UserReviewCard 
            v-if="game.ratings"
            v-for="rating in ratings" :key="rating.id"
            :userId="rating.user"
            :reviewBody="rating.body"/>
        </div>
        <div class="game-reviews" v-else>
            <p>This game has no reviews</p>
        </div>
    </div>
</template>

<script setup>
import NavBar from '@/components/NavBar.vue';
import GameImage from '@/assets/gamesImgs/gow.jpg'
import { useRoute } from 'vue-router'
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import UserReviewCard from '@/components/UserReviewCard.vue';

const route = useRoute()
const gameId = route.params.id
const userReview = ref()

const body = ref('')
const value = ref()
const userId = ref()

const ratings = computed(() => game.value?.ratings || [])

const hasReviews = computed(() => {
  return game.value && game.value.ratings && game.value.ratings.length > 0
})

const hoverIndex = ref(-1)

const game = ref(null)

onMounted(() => {
    axios
    .get(`http://127.0.0.1:8000/testApp/games/${gameId}/detail`)
    .then(response => {game.value = response.data})
})

function postReview(){
    axios
        .post(`http://127.0.0.1:8000/testApp/games/${gameId}/ratings`, {value:value.value, body:body.value, user:userId.value})
}
</script>

<style scoped>
.general{
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-inline: 240px;
    max-width: 1520px;
}

.submit{
    border-width: 1px;
    border-radius: 7px;
    border-color: aqua;
    background-color: #61ACC0;
    color: white;
    height: 30px;
    cursor: pointer;
}

.user-review{
    max-width: 775px;
}

.star-btn{
    border: none;
    background: none;
}

.lucide-star {
  transition: fill 0.2s ease, stroke 0.2s ease;
}

.filled{
    fill: #FDAA05;
    stroke: #FDAA05;
}

.yes-button{
    width: 70px;
    height: 30px;
    border-color: #22FF00;
    border-radius: 7px;
    color: #22FF00;
    background-color: #318033;
    cursor: pointer;
    border-width: 1px;
}

.no-button{
    width: 70px;
    height: 30px;
    color: #FF0000;
    border-color: #FF0000;
    background-color: #7B3535;
    border-radius: 7px;
    cursor: pointer;
    border-width: 1px;
}

.buttons{
    margin-top: 15px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.quest-buttons{
    max-width: 150px;
    display: flex;
    justify-content: space-between;
}

.media-section{
    margin-bottom: 40px;
    display: flex;
}

.game-info{
    margin-left: 40px;
}

.algo{
    background-color: #3a3a3a;
    color: white;
    border: 1px solid #5f5f5f;
    border-radius: 5px;
    height: 150px;
    width: 600px;
    resize: none;
    margin-left: 25px;
}

.picture{
    display: flex;
}

.game-reviews{
    margin-top: 80px;
}
</style>