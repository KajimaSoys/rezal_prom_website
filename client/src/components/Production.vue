<template>
  <div class="production">
    <div class="production-max">
      <div class="production-background"></div>

      <div class="production-content">
        <div class="production-video" @click="showVideoWrapper">
          <img
              :src="`${backendURL}${production.video_preview}`"
              alt=""
              height="580"
              width="420"
              class="production-preview-image"
              loading="lazy"
          >
          <svg width="60" height="60" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg"
               class="production-preview-icon">
            <circle cx="30" cy="30" r="30" fill="white"/>
            <path
                d="M39.8623 27.8782C41.1956 28.648 41.1956 30.5725 39.8623 31.3424L26.1748 39.2448C24.8415 40.0146 23.1748 39.0524 23.1748 37.5128L23.1748 21.7078C23.1748 20.1682 24.8415 19.206 26.1748 19.9758L39.8623 27.8782Z"
                fill="#DD1D1D"/>
          </svg>
        </div>

        <div class="production-subcontent">
          <div class="production-text">
            <div class="production-title">
              <h2>
                <div v-html="production.title"></div>
              </h2>
            </div>
            <div class="production-description">
              <div v-html="production.description"></div>
            </div>
          </div>

          <div class="production-photo">
            <img
                :src="`${backendURL}${production.image_one}`"
                alt=""
                width="160"
                height="160"
                class="production-image"
                loading="lazy"
            >
            <img
                :src="`${backendURL}${production.image_two}`"
                alt=""
                width="160"
                height="160"
                class="production-image"
                loading="lazy"
            >
            <img
                :src="`${backendURL}${production.image_three}`"
                alt=""
                width="160"
                height="160"
                class="production-image"
                loading="lazy"
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
  components: {},
  data() {
    return {}
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
.production {
  width: 100%;
  /*height: 88vh;*/
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 150px;
  padding-bottom: 75px;
}

.production-max {
  width: 90rem;
  height: 90%;
  border-radius: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0 2rem;
}

.production-background {
  background: linear-gradient(106.5deg, #1F1F1F 12.53%, #353535 105.97%);
  border-radius: 30px;
  height: 35rem;
  width: 100%;
  max-width: 90rem;
  padding: 0 2rem;
  position: absolute;
  z-index: -1;
  transform: translateY(-10%);
}

.production-content {
  max-width: 67rem;
  display: flex;
  flex-direction: row;
  gap: 90px;
}

.production-video {
  position: relative;
  /*width: 50%;*/
  /*flex-basis: 50%;*/
  cursor: pointer;
}

.production-preview-icon {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 1;
}

.production-preview-icon path {
  transition: fill 0.2s ease-in-out;
}

.production-preview-icon:hover path {
  fill: #EB7777;
}

.production-subcontent {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 50%;
  flex-basis: 50%;
}

.production-text {
  color: #FFFFFF;
}

.production-title {
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 35px;
  line-height: 53.55px;
  margin-block-start: 0.83em;
  margin-block-end: 0.83em;
}

.production-description {
  font-size: 16px;
  width: 90%;
}

.production-photo {
  /*display: flex;*/
  /*flex-direction: row;*/
  /*gap: 16px;*/
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

.production-photo img, .production-video img {
  max-width: 100%;
  height: auto;
}

@media screen and (max-width: 1200px) {
  .production-title {
    font-size: 32px;
    line-height: 43.55px;
  }
}

@media screen and (max-width: 990px) {
  .production {
    padding-bottom: 42rem;
  }

  .production-background {
    height: 50rem;
    padding: 0;
    margin: 0 2rem;
    border-radius: 0;
  }

  .production-content {
    position: relative;
  }

  .production-video {
    position: absolute;
    top: 17rem;
    width: 50%;
    flex-basis: 50%;
  }

  .production-subcontent {
    width: 100%;
    flex-basis: 100%;
  }

  .production-photo {
    grid-template-columns: repeat(1, 1fr);
    position: absolute;
    top: 17rem;
    left: 48vw;
  }
}

@media screen and (max-width: 640px) {
  .production-video {
    top: 23rem;
  }

  .production-photo {
    top: 23rem;
  }

  .production-title {
    font-size: 30px;
    line-height: 38px;
  }

  .production-description {
    width: 100%;
    font-size: 14px;
  }
}

@media screen and (max-width: 385px) {
  .production-video {
    top: 25rem;
  }

  .production-photo {
    top: 25rem;
  }
}
</style>