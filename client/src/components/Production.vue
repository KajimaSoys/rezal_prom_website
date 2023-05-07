<template>
  <div class="production">
    <div class="production-max">
      <div class="production-background"> </div>

      <div class="production-content">
        <div class="production-video">
          <img
              :src="`${this.backendURL}${this.production.video_preview}`"
              alt=""
              width="450"
              height="620"
              class="production-preview-image"
          >
          <img
              src="src/assets/icons/icon-play.svg"
              alt=""
              width="60"
              height="60"
              class="production-preview-icon"
          >
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
  inject: ['backendURL'],
  props: [
    'production',
  ],
}
</script>

<style scoped>
.production{
  width: 100%;
    /*height: 88vh;*/
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 100px;
  padding-bottom: 150px;
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
}

.production-preview-icon{
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 1;
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