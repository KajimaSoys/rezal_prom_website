<template>
  <div class="projects" id="projects">
    <div class="projects-max">
      <h2 class="projects-title" v-html="this.projects.title"></h2>

      <div class="projects-content">
        <div class="projects-content-left">
          <div class="projects-item">
            <div class="projects-item-preview-first" @click="showVideoWrapper(this.projects.video_link_first)">
              <img
                  :src="`${this.backendURL}${this.projects.image_first}`"
              >
              <div class="projects-item-preview-icon">
                <svg width="36" height="36" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="30" cy="30" r="30" fill="white"/>
                  <path d="M39.8623 27.8782C41.1956 28.648 41.1956 30.5725 39.8623 31.3424L26.1748 39.2448C24.8415 40.0146 23.1748 39.0524 23.1748 37.5128L23.1748 21.7078C23.1748 20.1682 24.8415 19.206 26.1748 19.9758L39.8623 27.8782Z" fill="#DD1D1D"/>
                </svg>
              </div>
              <div class="projects-item-preview-text">
                Смотреть видеообзор
              </div>
            </div>
            <h3 class="projects-item-title" v-html="this.projects.title_first"></h3>
            <div class="projects-item-description" v-html="this.projects.description_first"></div>
          </div>

          <div class="projects-item">
            <div class="projects-item-preview-second" @click="showVideoWrapper(this.projects.video_link_second)">
              <img
                  :src="`${this.backendURL}${this.projects.image_second}`"
              >
              <div class="projects-item-preview-icon">
                <svg width="36" height="36" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="30" cy="30" r="30" fill="white"/>
                  <path d="M39.8623 27.8782C41.1956 28.648 41.1956 30.5725 39.8623 31.3424L26.1748 39.2448C24.8415 40.0146 23.1748 39.0524 23.1748 37.5128L23.1748 21.7078C23.1748 20.1682 24.8415 19.206 26.1748 19.9758L39.8623 27.8782Z" fill="#DD1D1D"/>
                </svg>
              </div>
              <div class="projects-item-preview-text">
                Смотреть видеообзор
              </div>
            </div>
            <h3 class="projects-item-title" v-html="this.projects.title_second"></h3>
            <div class="projects-item-description" v-html="this.projects.description_second"></div>
          </div>
        </div>

        <div class="projects-content-right">
          <div class="projects-item">
            <div class="projects-item-preview-third" @click="showVideoWrapper(this.projects.video_link_third)">
              <img
                  :src="`${this.backendURL}${this.projects.image_third}`"
              >
              <div class="projects-item-preview-icon">
                <svg width="36" height="36" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="30" cy="30" r="30" fill="white"/>
                  <path d="M39.8623 27.8782C41.1956 28.648 41.1956 30.5725 39.8623 31.3424L26.1748 39.2448C24.8415 40.0146 23.1748 39.0524 23.1748 37.5128L23.1748 21.7078C23.1748 20.1682 24.8415 19.206 26.1748 19.9758L39.8623 27.8782Z" fill="#DD1D1D"/>
                </svg>
              </div>
              <div class="projects-item-preview-text">
                Смотреть видеообзор
              </div>
            </div>
            <h3 class="projects-item-title" v-html="this.projects.title_third"></h3>
            <div class="projects-item-description" v-html="this.projects.description_third"></div>
          </div>
          <div class="projects-button">
            <a class="projects-portfolio-button" href="https://mebel-rezal.clients.site/" target="_blank">
              Смотреть все проекты
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "Projects",
  inject: ['backendURL', 'showVideo'],
  props: [
    'projects',
  ],
  components: {

  },
  data() {
    return {

    }
  },
  methods: {
    showVideoWrapper(video_link) {
      const videoId = video_link.split('/')[video_link.split('/').length - 1];
      this.showVideo(videoId);
    },
  },
}
</script>

<style scoped>
.projects{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 150px;
  padding-bottom: 75px;
}

.projects-max{
  max-width: 67rem;
  margin: 0 2rem;
}

.projects-title{
  color: #000000;
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 36px;
  line-height: 54px;
  margin-bottom: 80px;
}

.projects-content{
  display: flex;
  justify-content: space-between;
}

.projects-content-left{
  width: 55%;
  flex-basis: 55%;
  display: flex;
  flex-direction: column;
  gap: 170px;
}

.projects-content-right{
  width: 40%;
  flex-basis: 40%;
  display: flex;
  align-items: flex-start;
  flex-direction: column;
  justify-content: center;
}

.projects-item{

}

.projects-item-preview-first, .projects-item-preview-second, .projects-item-preview-third {
  position: relative;
  cursor: pointer;
}

.projects-item-preview-first img {
  display: block;
  width: 90%;
}

.projects-item-preview-second img {
  display: block;
  width: 80%;
}

.projects-item-preview-third img {
  display: block;
  width: 100%;
}

.projects-item-preview-icon {
  position: absolute;
  bottom: 0;
  left: 0;
  margin: 20px;
}

svg path{
  transition: fill 0.2s ease-in-out;
}

svg:hover path{
  fill: #EB7777;
}

.projects-item-preview-text {
  position: absolute;
  bottom: 10px;
  left: 45px;
  margin: 20px;
  color: #ffffff;
}

.projects-item-title{
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 22px;
  line-height: 31px;
  color: #222222;
  padding-top: 20px;
  padding-bottom: 20px;
}

.projects-item-description{
  color: #686868;
  width: 90%;
}

.projects-button{
  padding-top: 5rem;
}

.projects-portfolio-button{
  padding: 15px 25px;
  color: #FFFFFF;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  background: #DD1D1D;
  border-radius: 14px;
  font-size: 14px;
  cursor: pointer;
  transition: all .1s ease-in-out;
  text-decoration: none;
}

.projects-portfolio-button:hover{
  background-color: #C20D0D;
}

@media screen and (max-width: 990px){
  .projects-content{
    flex-direction: column;
    gap: 4rem;
  }

  .projects-content-left {
    width: 100%;
    flex-basis: 100%;
    gap: 4rem;
  }
  .projects-item-preview-first img{
    width: 80%;
  }

  .projects-item-preview-second img{
    width: 100%;
  }

  .projects-content-left > div:nth-child(2){
    margin-left: 30%;
  }

  .projects-content-right {
    width: 80%;
  }
}



@media screen and (max-width: 640px){
  .projects-title{
    line-height: 38px;
    font-size: 30px;
  }

  .projects-item-preview-first img{
    width: 100%;
  }

  .projects-item-preview-second img{
    width: 100%;
  }

  .projects-content-left > div:nth-child(2){
    margin-left: 0;
  }

  .projects-content-right {
    width: 100%;
  }

  .projects-button{
    width: 100%;
  }
}

@media screen and (max-width: 360px){

}
</style>