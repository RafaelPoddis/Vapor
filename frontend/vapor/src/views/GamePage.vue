<template>
    <NavBar/>
    <div class="general">
        <div class="media-section">
            <div class="img-title">
                <img alt="Game Image" class="gameImg" :src="selectedGame?.image" width="720" height="360" />
                <!-- <video width="720" height="400" controls>
                    <source :src="selectedGame?.image" type="video/mp4" />
                    Seu navegador não suporta a tag de vídeo.
                </video> -->
                <div class="game-title">
                    <h1>{{ selectedGame?.name || 'Jogo não encontrado' }}</h1>
                </div>
            </div>
            <div class="game-info">
                <p>DescriptionDescriptionDescription<br>
                    DescriptionDescriptionDescription<br>
                    Description</p>
            </div>
        </div>
        <div class="user-review" v-if="!userReview">
            <textarea class="algo" placeholder="Write something about this game..." rows="3"></textarea>
        </div>
        <div class="user-review" v-else>Nao</div>
        <div class="game-reviews" v-if="gamReviews">
            <p>This game has no reviews</p>
        </div>
        <UserReviewCard/>
        <UserReviewCard/>
        <UserReviewCard/>
        <UserReviewCard/>
    </div>
</template>

<script setup>
import NavBar from '@/components/NavBar.vue';
import GameImage from '@/assets/gamesImgs/gow.jpg'
import { useRoute } from 'vue-router'
import { ref, computed } from 'vue'
import UserReviewCard from '@/components/UserReviewCard.vue';

const route = useRoute()
const gameId = route.params.id
const userReview = ref(false)
const gamReviews = ref(false)

defineProps({
    name: String,
    price: String,
    image: [String, File],
    id: Number
})

const games = ref([
  { id: 1, name: "God of War", price: "$250.00", image: "C:\\Users\\Rafael\\Documents\\VaporProject\\backend\\media\\games\\3\\media\\test1.jpeg" },
  { id: 2, name: "Jogo 2", price: "$150.00", image: GameImage},
  { id: 3, name: "Jogo 3", price: "$100.00", image: "C:\\Users\\Rafael\\Documents\\VaporProject\\backend\\media\\games\\4\\media\\test3.png" },
  { id: 4, name: "God of War 2", price: "$350.00", image: "C:\\Users\\Rafael\\Documents\\VaporProject\\backend\\media\\games\\3\\media\\test1.jpeg" },
  { id: 5, name: "Jogo 4", price: "$68.00", image: "C:\\Users\\Rafael\\Documents\\VaporProject\\backend\\media\\games\\4\\media\\test2.png" },
  { id: 6, name: "Jogo 5", price: "$10.00", image: "C:\\Users\\Rafael\\Documents\\VaporProject\\backend\\media\\games\\4\\media\\test3.png" },
  { id: 7, name: "God of War 3", price: "$20.00", image: "C:\\Users\\Rafael\\Documents\\VaporProject\\backend\\media\\games\\3\\media\\test1.jpeg" },
  { id: 8, name: "Jogo 6", price: "$124.00", image: "C:\\Users\\Rafael\\Documents\\VaporProject\\backend\\media\\games\\4\\media\\test2.png" },
  { id: 9, name: "Jogo 7", price: "$1.50", image: "C:\\Users\\Rafael\\Documents\\VaporProject\\backend\\media\\games\\4\\media\\test3.png" },
])

const selectedGame = computed(() => {
  return games.value.find(game => game.id === Number(gameId))
})
</script>

<style scoped>
.general{
    margin-inline: 240px;
    max-width: 1520px;
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
    height: 125px;
    width: 500px;
    resize: none;
}
</style>