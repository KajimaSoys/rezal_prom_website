<template>
  <div class="reviews" id="reviews">
    <div class="reviews-max">
      <h2 class="reviews-title" v-html="this.reviews.title"></h2>
      <div class="reviews-content">

        <div class="reviews-text">
          <TextReviews :reviewTextArr="this.reviewTextArr"></TextReviews>
        </div>


        <div class="reviews-video">
          <VideoReviews :reviewVideoArr="this.reviewVideoArr"></VideoReviews>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import TextReviews from "../components/reviews/TextReviews.vue";
import VideoReviews from "../components/reviews/VideoReviews.vue";

export default {
  name: "Reviews",
  inject: ['backendURL'],
  props: [
    'reviews',
    'reviewTextArr',
    'reviewVideoArr',
  ],
  components: {
    TextReviews,
    VideoReviews,
  },
}
</script>

<style scoped>
.reviews{
  width: 100%;
  /*display: flex;*/
  /*justify-content: center;*/
  /*align-items: center;*/
  padding-top: 75px;
  padding-bottom: 75px;
}

.reviews-max{
  max-width: 67rem;
  margin: auto;
  padding: 0 2rem;
}

.reviews-title{
  color: #000000;
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 36px;
  line-height: 54px;
  margin-bottom: 40px;
}

.reviews-text {
  position: relative;
  margin-bottom: 80px;
  width: 100%;
}

.reviews-video {
  position: relative;
  margin-bottom: 80px;
  width: 100%;
}


@media screen and (max-width: 640px){
  .reviews-title{
    line-height: 38px;
    font-size: 30px;
  }
}

@media screen and (max-width: 360px){

}
</style>

<style>
.swiper-pagination-bullet {
  margin: 0;
}

.swiper-pagination-bullet.swiper-pagination-bullet-active {
  background: #DD1D1D;
}
</style>