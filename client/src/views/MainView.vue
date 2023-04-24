<template>
  <div class="content">

    <div class="header">
      <div class="header-max">
        <div class="logo">
          <img :src="`${this.backendURL}${this.header.logo}`" alt="РезАль - Мебельная компания. Логотип." width="138" height="34" />
        </div>

        <div class="menu">
          <div class="menu-item">
            О компании
          </div>
          <div class="menu-item">
            Портфолио
          </div>
          <div class="menu-item">
            Доставка и оплата
          </div>
          <div class="menu-item">
            Отзывы
          </div>
          <div class="menu-item">
            Контакты
          </div>
        </div>


        <div class="call-block">
          <div class="phone-number">
            <img src="src/assets/icons/phone.svg" alt="" width="16" height="16" />
            {{ this.header.number }}
          </div>

          <div class="phone-text">
            Заказать звонок
          </div>
        </div>

      </div>
    </div>

    <div class="main">
      <div class="main-max"
           :style="{ 'background-image': `linear-gradient(180deg, rgba(0, 0, 0, 0.7) 0%, rgba(0, 0, 0, 0.4) 48.37%, rgba(0, 0, 0, 0.8) 100%), url(${this.backendURL}${this.main.image})`, 'background-size': 'cover', 'background-position': 'center center', 'transform': 'scale(1)' }">
        <div class="main-title">
          <h1>{{ this.main.title }}</h1>
        </div>
        <div class="main-secondary">
          <div class="main-description">
            {{ this.main.description }}
          </div>

          <div class="main-buttons">
            <div class="main-request-button">
              Оставить заявку
            </div>

            <div class="main-count-button">
              Рассчитать стоимость
            </div>
          </div>

        </div>
      </div>
    </div>

    <div class="about">
      <div class="about-max">
        <div class="about-head">
          <div class="about-image-container">
            <img src="src/assets/images/image-about-1.png" class="about-image-1">
          </div>
          <div class="about-image-container">
            <img src="src/assets/images/image-about-2.png" class="about-image-2">
          </div>
          <div class="about-description">
            <div v-html="this.about.description"></div>
          </div>
          <div class="about-image-container">
            <img src="src/assets/images/image-about-3.png" class="about-image-3">
          </div>
        </div>

        <div class="about-content">
          <div class="about-content-row">
            <div class="about-thick">
              <div class="about-card-title">
                <h3>
                  <div v-html="this.about.title_first"></div>
                </h3>
              </div>
              <div class="about-card-description">
                <div v-html="this.about.description_first"></div>
              </div>
            </div>
            <div class="about-thin">
              <div class="about-card-title">
                <h3>
                  <div v-html="this.about.title_second"></div>
                </h3>
              </div>
              <div class="about-card-description">
                <div v-html="this.about.description_second"></div>
              </div>
            </div>
          </div>

          <div class="about-content-row">
            <div class="about-thin">
              <div class="about-card-title">
                <h3>
                  <div v-html="this.about.title_third"></div>
                </h3>
              </div>
              <div class="about-card-description">
                <div v-html="this.about.description_third"></div>
              </div>
            </div>
            <div class="about-thick">
              <div class="about-card-title">
                <h3>
                  <div v-html="this.about.title_fourth"></div>
                </h3>
              </div>
              <div class="about-card-description">
                <div v-html="this.about.description_fourth"></div>
              </div>
            </div>
          </div>

          <div class="about-content-row">
            <div class="about-thick">
              <div class="about-card-title">
                <h3>
                  <div v-html="this.about.title_fifth"></div>
                </h3>
              </div>
              <div class="about-card-description">
                <div v-html="this.about.description_fifth"></div>
              </div>
            </div>
            <div class="about-thin">
              <div class="about-card-title">
                <h3>
                  <div v-html="this.about.title_sixth"></div>
                </h3>
              </div>
              <div class="about-card-description">
                <div v-html="this.about.description_sixth"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

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

    <div class="services">
      <div class="services-max">
        <div class="services-title">
          <h2>
            <div v-html="this.services.title"></div>
          </h2>
        </div>
        <div class="services-items">
          <div class="services-item">
            <div class="services-item-icon">
              <img
                  src="src/assets/icons/icon-cabinet.svg"
                  alt=""
                  width="36"
                  height="36"
              >
            </div>
            <div class="services-item-title">
              <h3>
                <div v-html="this.services.title_first"></div>
              </h3>
            </div>
          </div>

          <div class="services-item">
            <div class="services-item-icon">
              <img
                  src="src/assets/icons/icon-measure.svg"
                  alt=""
                  width="36"
                  height="36"
              >
            </div>
            <div class="services-item-title">
              <h3>
                <div v-html="this.services.title_second"></div>
              </h3>
            </div>
          </div>

          <div class="services-item">
            <div class="services-item-icon">
              <img
                  src="src/assets/icons/icon-pencil.svg"
                  alt=""
                  width="36"
                  height="36"
              >
            </div>
            <div class="services-item-title">
              <h3>
                <div v-html="this.services.title_third"></div>
              </h3>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="projects">
      <div class="projects-max">
        <h2 class="projects-title" v-html="this.projects.title"></h2>

        <div class="projects-content">
          <div class="projects-content-left">
            <div class="projects-item">
              <div class="projects-item-preview-first">
                <img
                    :src="`${this.backendURL}${this.projects.image_first}`"
                >
                <div class="projects-item-preview-icon">
                  <img src="src/assets/icons/icon-play.svg" width="36" height="36">
                </div>
                <div class="projects-item-preview-text">
                  Смотреть видеоотзыв
                </div>
              </div>
              <h3 class="projects-item-title" v-html="this.projects.title_first"></h3>
              <div class="projects-item-description" v-html="this.projects.description_first"></div>
            </div>

            <div class="projects-item">
              <div class="projects-item-preview-second">
                <img
                    :src="`${this.backendURL}${this.projects.image_second}`"
                >
                <div class="projects-item-preview-icon">
                  <img src="src/assets/icons/icon-play.svg" width="36" height="36">
                </div>
                <div class="projects-item-preview-text">
                  Смотреть видеоотзыв
                </div>
              </div>
              <h3 class="projects-item-title" v-html="this.projects.title_second"></h3>
              <div class="projects-item-description" v-html="this.projects.description_second"></div>
            </div>
          </div>

          <div class="projects-content-right">
            <div class="projects-item">
              <div class="projects-item-preview-third">
                <img
                    :src="`${this.backendURL}${this.projects.image_third}`"
                >
                <div class="projects-item-preview-icon">
                  <img src="src/assets/icons/icon-play.svg" width="36" height="36">
                </div>
                <div class="projects-item-preview-text">
                  Смотреть видеоотзыв
                </div>
              </div>
              <h3 class="projects-item-title" v-html="this.projects.title_third"></h3>
              <div class="projects-item-description" v-html="this.projects.description_third"></div>
            </div>
            <div class="projects-button">
              <div class="projects-portfolio-button">
                Смотреть все проекты
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="stages">
      stages
    </div>

    <div class="team">
      team
    </div>

    <div class="questions">
      questions
    </div>

    <div class="reviews">
      reviews
    </div>

    <div class="contacts">
      contacts
    </div>

    <div class="footer">
      footer
    </div>



  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "MainView",
  inject: ['backendURL'],
  data(){
    return {
      stagesArr: [],
      staffArr: [],
      questionsArr: [],
      reviewTextArr: [],
      reviewVideoArr: [],

      header: {},
      main: {},
      about: {},
      production: {},
      services: {},
      projects: {},
      stages: {},
      team: {},
      questions: {},
      reviews: {},
      contacts: {},
      footer: {},
    }
  },

  methods: {
    async getPageData(){
      await axios
          .get('api/v1/all_blocks/')
          .then( response => {
            let receivedData = response.data

            receivedData.forEach(block => {
              if (block.type === 'HeaderBlock') {
                this.header = block.data
              } else if (block.type === 'MainBlock') {
                this.main = block.data
              } else if (block.type === 'AboutBlock') {
                this.about = block.data
              } else if (block.type === 'ProductionBlock') {
                this.production = block.data
              } else if (block.type === 'ServicesBlock') {
                this.services = block.data
              } else if (block.type === 'ProjectsBlock') {
                this.projects = block.data
              } else if (block.type === 'StagesBlock') {
                this.stages = block.data
              } else if (block.type === 'TeamBlock') {
                this.team = block.data
              } else if (block.type === 'QuestionsBlock') {
                this.questions = block.data
              } else if (block.type === 'ReviewsBlock') {
                this.reviews = block.data
              } else if (block.type === 'ContactsBlock') {
                this.contacts = block.data
              } else if (block.type === 'FooterBlock') {
                this.footer = block.data
              }
            });

            console.log(response.data)
          })
          .catch( error => {
            console.log('An error occurred: ', error)
          })
    },

    async getObjectsData(){
      await axios
          .get('api/v1/core_objects/')
          .then( response => {
            let receivedData = response.data
            receivedData.forEach( block => {
              if (block.type === 'Stages') {
                this.stagesArr.push(block.data)
              } else if (block.type === 'Staff') {
                this.staffArr.push(block.data)
              } else if (block.type === 'Questions') {
                this.questionsArr.push(block.data)
              } else if (block.type === 'ReviewText') {
                this.reviewTextArr.push(block.data)
              } else if (block.type === 'ReviewVideo') {
                this.reviewVideoArr.push(block.data)
              }
            });

            console.log(response.data)
          })
          .catch( error => {
            console.log('An error occurred: ', error)
          })
    },
  },

  beforeMount() {
    this.getPageData()
    this.getObjectsData()
  }

}
</script>

<style scoped>


.header{
  height: 12vh;
  width: 100%;
  display: flex;
  justify-content: center;
}

.header-max{
  width: 85rem;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
}

.logo{
  width: 20%;
  flex-basis: 20%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.menu{
  flex: 1;
  display: flex;
  gap: 30px;
}

.menu-item{
  font-size: 18px;
}

.call-block{
  width: 15%;
  flex-basis: 15%;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  cursor: pointer;
}

.phone-number{
  display: flex;
  align-items: center;
  gap: 10px;
}

.phone-text{
  color: #DD1D1D;
}

.main{
  width: 100%;
  height: 88vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.main-max{
  width: 90rem;
  height: 90%;
  border-radius: 30px;
  display: flex;
  flex-direction: column;
}

.main-title{
  padding: 100px 175px 0 175px;
  flex: 1;
  width: 65%;
}

.main-title h1{
  color: white;
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 44px;
  line-height: 60px;
}

.main-secondary{
  padding: 0 175px 100px 175px;
  height: 20%;
  flex-basis: 20%;
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  justify-content: space-between;
}

.main-description{
  color: white;
  font-size: 22px;
  line-height: 33.6px;
  max-width: 50%;
  flex-basis: 50%;
}

.main-buttons{
  width: 50%;
  flex-basis: 50%;
  display: flex;
  flex-direction: row;
  gap: 16px;
  height: 35%;
  justify-content: flex-end;
}

.main-request-button{
  width: 40%;
  flex-basis: 40%;
  color: #FFFFFF;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  background: #DD1D1D;
  border-radius: 14px;
}

.main-count-button{
  width: 50%;
  flex-basis: 50%;
  color: #FFFFFF;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  border: 2px solid #B4B4B4;
  border-radius: 14px;
}

.about{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 150px;
  padding-bottom: 150px;
}

.about-max{
  width: 67rem;
  /*height: 90%;*/
  /*border-radius: 30px;*/
  display: flex;
  flex-direction: column;
  gap: 5rem;
}

.about-head{
  display: flex;
  flex-direction: row;
  gap: 16px;
  align-items: center;
}

.about-image-container{
  border-radius: 15px;
  height: 160px;
  width: 160px;
}

.about-image-1, .about-image-2, .about-image-3 {
  max-width: 100%;
  height: 100%;
  object-fit: cover;
}

.about-description{
  flex: 1;
  font-size: 16px;
  line-height: 25.2px;
  margin: 0 5%;
  color: #000000;
}

.about-content{
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.about-content-row{
  display: flex;
  flex-direction: row;
  gap: 16px;
}

.about-thick{
  width: 60%;
  flex-basis: 60%;
  height: 200px;
  border: 1px solid #BDBDBD;
  border-radius: 30px;
  padding: 25px 35px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.about-thin{
  width: 40%;
  flex-basis: 40%;
  height: 200px;
  border: 1px solid #BDBDBD;
  border-radius: 30px;
  padding: 25px 35px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.about-card-title{
  color: #222222;
  font-family: 'OnestMedium', Inter, sans-serif;
  font-style: normal;
  font-weight: 500;
  font-size: 22px;
  line-height: 36px;
}

/*.about-card-title > h3{*/
/*  margin-block-start: 0;*/
/*  margin-block-end: 0;*/
/*}*/

.about-card-description{
 color: #686868;
}

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

.services{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.services-max{
  width: 67rem;
}

.services-title{
  color: #000000;
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 36px;
  line-height: 54px;
  margin-bottom: 60px;
}

.services-items{
 display: flex;
  flex-direction: row;
  gap: 16px;
}

.services-item{
  flex: 1;
  height: 200px;
  border: 1px solid #BDBDBD;
  border-radius: 30px;
  padding: 25px 35px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.services-item-icon{
  width: 67px;
  height: 54px;
  background: #DD1D1D;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.services-item-title{
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 22px;
  line-height: 31px;
  color: #222222;
  width: 80%;
}

.projects{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 150px;
  padding-bottom: 150px;
}

.projects-max{
  width: 67rem;
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

.projects-item-preview-text {
  position: absolute;
  bottom: 4px;
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
}

.stages{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.team{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.questions{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.reviews{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.contacts{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.footer{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>