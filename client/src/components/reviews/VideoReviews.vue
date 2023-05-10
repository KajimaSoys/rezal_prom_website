<template>
  <swiper
    :modules="modules"
    :slides-per-view="slidesPerView"
    :space-between="16"
    :navigation="{ nextEl: '.swiper-button-next-2', prevEl: '.swiper-button-prev-2' }"
    :pagination="{ el: '.swiper-pagination-2', clickable: true, bulletClass: 'swiper-pagination-bullet', bulletActiveClass: 'swiper-pagination-bullet-active' }"
  >
    <swiper-slide
        v-for="(review, index) in this.reviewVideoArr"
        :key="index"
        class="review-card"
    >
      <div class="review-video" @click="showVideoWrapper(review.video_link)">
        <img
            :src="`${this.backendURL}${review.image}`"
            alt=""
            class="review-preview-image"
        >
        <svg width="40" height="40" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg" class="review-preview-icon">
          <circle cx="30" cy="30" r="30" fill="white"/>
          <path d="M39.8623 27.8782C41.1956 28.648 41.1956 30.5725 39.8623 31.3424L26.1748 39.2448C24.8415 40.0146 23.1748 39.0524 23.1748 37.5128L23.1748 21.7078C23.1748 20.1682 24.8415 19.206 26.1748 19.9758L39.8623 27.8782Z" fill="#DD1D1D"/>
        </svg>
      </div>
    </swiper-slide>
  </swiper>
  <div class="swiper-controls">
    <div class="swiper-button-prev swiper-button-prev-2">
      <svg width="20" height="18" viewBox="0 0 20 18" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path fill-rule="evenodd" clip-rule="evenodd" d="M8.0973 0.156443L0.183064 8.53296L0.182131 8.53401L0.172611 8.54412C-0.0572777 8.78808 -0.0578003 9.2114 0.172625 9.456L0.181719 9.46565L0.182583 9.46662L8.09723 17.8436C8.29484 18.0527 8.58788 18.0522 8.78497 17.8416C9.01494 17.5958 9.01372 17.1747 8.78313 16.9306L1.86931 9.61291H19.4835C19.7116 9.61291 20 9.39746 20 9.00001C20 8.60256 19.7116 8.3871 19.4835 8.3871H1.86919L8.78325 1.06935C9.01382 0.825229 9.01501 0.404166 8.78505 0.158436C8.58785 -0.0522866 8.29489 -0.0526697 8.0973 0.156443Z" fill="black"/>
      </svg>
    </div>
    <div class="swiper-pagination swiper-pagination-2"></div>
    <div class="swiper-button-next swiper-button-next-2">
      <svg width="20" height="18" viewBox="0 0 20 18" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path fill-rule="evenodd" clip-rule="evenodd" d="M11.9027 0.156443L19.8169 8.53296L19.8179 8.53401L19.8274 8.54412C20.0573 8.78808 20.0578 9.2114 19.8274 9.456L19.8183 9.46565L19.8174 9.46662L11.9028 17.8436C11.7052 18.0527 11.4121 18.0522 11.215 17.8416C10.9851 17.5958 10.9863 17.1747 11.2169 16.9306L18.1307 9.61291H0.516543C0.288381 9.61291 0 9.39746 0 9.00001C0 8.60256 0.288382 8.3871 0.516543 8.3871H18.1308L11.2168 1.06935C10.9862 0.825229 10.985 0.404166 11.215 0.158436C11.4121 -0.0522866 11.7051 -0.0526697 11.9027 0.156443Z" fill="black"/>
      </svg>
    </div>
  </div>
</template>

<script>
import { Navigation, Pagination, Scrollbar, A11y } from 'swiper';

// Import Swiper Vue.js components
import { Swiper, SwiperSlide } from 'swiper/vue';

// Import Swiper styles
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import {computed, onBeforeUnmount, onMounted, ref} from "vue";

export default {
  name: "VideoReviews",
  components: {
    Swiper,
    SwiperSlide,
  },
  inject: ['backendURL', 'showVideo'],
  props: [
    'reviewVideoArr'
  ],
  setup() {
    const modules = [Navigation, Pagination, A11y];
    const windowWidth = ref(window.innerWidth);
    // TODO return ? 2 : 4 after video review add
    const slidesPerView = computed(() => windowWidth.value < 990 ? 2 : 3);

    const updateWindowWidth = () => {
      windowWidth.value = window.innerWidth;
    };

    onMounted(() => {
      window.addEventListener('resize', updateWindowWidth);
    });

    onBeforeUnmount(() => {
      window.removeEventListener('resize', updateWindowWidth);
    });

    return {
      modules,
      slidesPerView,
    };
  },

  methods: {
    showVideoWrapper(video_link) {
      const videoId = video_link.split('/')[video_link.split('/').length - 1];
      this.showVideo(videoId);
    },

  }
}
</script>

<style scoped>
.swiper-controls {

  justify-content: center;
  align-items: flex-start;
  margin-top: 50px;
  flex-direction: row;
  gap: 30px;

  /* TODO replace with display: flex; when video review count 4 */
  display: none;
}


.swiper-button-next,
.swiper-button-prev {
  border-radius: 50%;
  border: 1px solid #BDBDBD;
  width: 50px;
  height: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  position: inherit;
}

.swiper-button-prev svg, .swiper-button-next svg{
  -webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none; /* Chrome, Safari, Opera */
  -khtml-user-select: none; /* Konqueror HTML */
  -moz-user-select: none; /* Firefox */
  -ms-user-select: none; /* Internet Explorer/Edge */
  user-select: none; /* Нестандартное свойство */
}

svg path{
  transition: fill 0.2s ease-in-out;
}

.swiper-button-next:hover svg path, .swiper-button-prev:hover svg path{
  fill: #DD1D1D;
}

.swiper-button-next:after, .swiper-button-prev:after {
  content: none;
}
.swiper-button-next:after, .swiper-button-prev:after {
  font-family: none;
  font-size: none;
  text-transform: none!important;
  letter-spacing: 0;
  font-variant: initial;
  line-height: 1;
}

.swiper-pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 4px;
  position: inherit;
}

.swiper-pagination-bullets.swiper-pagination-horizontal{
  width: inherit;
}

.review-card {
  height: 400px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 8px; /* Добавьте закругленные края для карточки */
  overflow: hidden; /* Обрежьте содержимое, выходящее за границы карточки */
}

.review-video {
  position: relative;
  width: 100%;
  height: 100%;
  cursor: pointer;
}

.review-preview-icon {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 1;
}

svg path{
  transition: fill 0.2s ease-in-out;
}

svg:hover path{
  fill: #EB7777;
}

.review-preview-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

@media screen and (max-width: 990px){
  .review-card{
    height: 500px;
  }

  /* TODO delete when 4 video review */
  .swiper-controls{
    display: flex;
  }

}

@media screen and (max-width: 640px){
  .review-card{
    height: 300px;
  }

  .swiper-controls{
    gap: 10px;
  }
}
</style>