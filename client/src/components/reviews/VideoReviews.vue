<template>
  <swiper
    :modules="modules"
    :slides-per-view="4"
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
        <img
            src="src/assets/icons/icon-play.svg"
            alt=""
            width="40"
            height="40"
            class="review-preview-icon"
        >
      </div>
    </swiper-slide>
  </swiper>
  <div class="swiper-controls">
    <div class="swiper-button-prev swiper-button-prev-2">
      <img src="src/assets/icons/icon-arrow-left.svg">
    </div>
    <div class="swiper-pagination swiper-pagination-2"></div>
    <div class="swiper-button-next swiper-button-next-2">
      <img src="src/assets/icons/icon-arrow-right.svg">
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
    return {
      modules: [Navigation, Pagination, A11y],
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
  display: flex;
  justify-content: center;
  align-items: flex-start;
  margin-top: 50px;
  flex-direction: row;
  gap: 30px;
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

.review-preview-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>