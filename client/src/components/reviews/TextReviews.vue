<template>
  <swiper
    :modules="modules"
    :slides-per-view="3"
    :space-between="16"
    :navigation="{ nextEl: '.swiper-button-next-1', prevEl: '.swiper-button-prev-1' }"
    :pagination="{ el: '.swiper-pagination-1', clickable: true, bulletClass: 'swiper-pagination-bullet', bulletActiveClass: 'swiper-pagination-bullet-active' }"
  >
    <swiper-slide
        v-for="(review, index) in this.reviewTextArr"
        :key="index"
        class="review-card"
    >
      <div class="review-head">
        <div class="review-author-photo">
          <img
              v-if="review.author_photo"
              :src="`${this.backendURL}${review.author_photo}`"
              :alt="review.author_name" />
        </div>
        <div class="review-author-name" v-html="review.author_name"></div>
      </div>

      <div class="review-text" v-html="review.review_text"></div>
      <div class="review-link" v-if="review.review_link">
        <a :href="`${this.backendURL}${review.review_link}`" target="_blank">Оригинал отзыва</a>
      </div>
    </swiper-slide>
  </swiper>
  <div class="swiper-controls">
    <div class="swiper-button-prev swiper-button-prev-1">
      <img src="src/assets/icons/icon-arrow-left.svg">
    </div>
    <div class="swiper-pagination swiper-pagination-1"></div>
    <div class="swiper-button-next swiper-button-next-1">
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
  name: "TextReviews",
  components: {
    Swiper,
    SwiperSlide,
  },
  inject: ['backendURL'],
  props: [
    'reviewTextArr'
  ],
  setup() {
    return {
      modules: [Navigation, Pagination, A11y],
    };
  },
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
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #fff;
  border-radius: 16px;
  border: 1px solid #ccc;
  height: 400px;
  box-sizing: border-box;
  padding: 20px;
}

.review-head{
  height: 20%;
  flex-basis: 25%;
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 16px;
}

.review-author-photo{
  width: 60px;
}

.review-author-photo img{
  height: 60px;
  width: 60px;
  border-radius: 50%;
  object-fit: cover;
}

.review-author-name{
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 22px;
  line-height: 31px;
  flex: 1;
}

.review-text{
  flex: 1;
  font-size: 15px;
  line-height: 1.4;
  color: #000000;
}

.review-link{
  height: 15%;
  flex-basis: 15%;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  width: 100%;
}

.review-link a{
  color: #DD1D1D;
  font-size: 15px;
  line-height: 23px;
  text-decoration: none;
}
</style>