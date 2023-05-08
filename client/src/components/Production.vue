<template>
  <div class="production">
    <div class="production-max">
      <div class="production-background"> </div>

      <div class="production-content">
        <div class="production-video" @click="showVideoWrapper">
          <img
              :src="`${this.backendURL}${this.production.video_preview}`"
              alt=""
              width="450"
              height="620"
              class="production-preview-image"
          >
          <svg width="60" height="60" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg" class="production-preview-icon">
            <circle cx="30" cy="30" r="30" fill="white"/>
            <path d="M39.8623 27.8782C41.1956 28.648 41.1956 30.5725 39.8623 31.3424L26.1748 39.2448C24.8415 40.0146 23.1748 39.0524 23.1748 37.5128L23.1748 21.7078C23.1748 20.1682 24.8415 19.206 26.1748 19.9758L39.8623 27.8782Z" fill="#DD1D1D"/>
          </svg>
        </div>

        <div class="production-subcontent">
          <div class="production-text">
            <div class="production-title">
              <h2>
                <div v-html="this.production.title"></div>
              </h2>
            </div>
            <div class="production-description">
              <div v-html="this.production.description"></div>
            </div>
          </div>

          <div class="production-photo">
            <img
              :src="`${this.backendURL}${this.production.image_one}`"
              alt=""
              width="160"
              height="160"
              class="production-image"
          >
            <img
              :src="`${this.backendURL}${this.production.image_two}`"
              alt=""
              width="160"
              height="160"
              class="production-image"
          >
            <img
              :src="`${this.backendURL}${this.production.image_three}`"
              alt=""
              width="160"
              height="160"
              class="production-image"
          >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "Production",
  inject: ['backendURL', 'showVideo'],
  props: [
    'production',
  ],
  components: {

  },
  data() {
    return {

    }
  },
  methods: {
    showVideoWrapper() {
      const videoId = this.production.video_link.split('/')[this.production.video_link.split('/').length - 1];
      this.showVideo(videoId);
    },
  },
}
</script>

<style scoped>
.production{
  width: 100%;
    /*height: 88vh;*/
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 150px;
  padding-bottom: 75px;
}

.production-max{
  width: 90rem;
  height: 90%;
  border-radius: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.production-background{
  background: linear-gradient(106.5deg, #1F1F1F 12.53%, #353535 105.97%);
  border-radius: 30px;
  height: 38rem;
  width: 90rem;
  position: absolute;
  z-index: -1;
  transform: translateY(-10%);
}

.production-content{
  width: 67rem;
  display: flex;
  flex-direction: row;
  gap: 90px;
}

.production-video{
  position: relative;
  height: 620px;
  cursor: pointer;
}

.production-preview-icon{
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 1;
}

.production-preview-icon path{
  transition: fill 0.2s ease-in-out;
}

.production-preview-icon:hover path{
  fill: #EB7777;
}

.production-subcontent{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.production-text{
  color: #FFFFFF;
}

.production-title{
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 38px;
  line-height: 53.55px;
  margin-block-start: 0.83em;
  margin-block-end: 0.83em;
}

.production-description {
  font-size: 16px;
  width: 90%;
}

.production-photo{
  display: flex;
  flex-direction: row;
  gap: 16px;
}
</style>