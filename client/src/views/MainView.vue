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

    <div class="request">
      <div class="request-max">
        <div class="request-background"></div>

        <div class="request-content">
          <div class="request-icon">
            -5%
          </div>
          <div class="request-title">
            Получите в подарок скидку 5%
          </div>
          <div class="request-description">
            Оставьте заявку на изготовление мебели и получите скидку 5% при заказе 3 и более элементов мебели
          </div>
          <div class="request-form">
            <div class="request-form-item">
              <div class="request-form-label">
                Ваше имя
              </div>
              <div class="request-form-input">
                <input v-model="this.request1.name" type="text" name="input1" placeholder="Введите имя">
              </div>
            </div>

            <div class="request-form-item">
              <div class="request-form-label">
                Куда позвонить?
              </div>
              <div class="request-form-input">
                <input v-model="this.request1.phone" type="tel" name="input1" placeholder="+7 ___ ___-__-__">
              </div>
            </div>

            <div class="request-form-item">
              <div class="request-form-label">
                Какая мебель нужна?
              </div>
              <div class="request-form-input">
                <input v-model="this.request1.message" type="text" name="input1" placeholder="Расскажите, что Вас интересует">
              </div>
            </div>

            <div class="request-form-item">
              <div class="request-form-label">

              </div>
              <div class="request-form-submit" @click="this.sendRequest(this.request1)">
                Оставить заявку
              </div>
            </div>
          </div>
            <div class="request-acceptance">
              Нажимая кнопку «Оставить заявку» вы даете согласие на обработку персональных данных и принимаете условия <a>политики конфиденциальности</a>
            </div>
        </div>

      </div>
    </div>

    <div class="stages">
      <div class="stages-max">
        <h2>
          <div class="stages-title" v-html="this.stages.title"></div>
        </h2>
        <div class="stages-grid">
          <div v-for="(stage, index) in this.stagesArr" :key="index" class="stage">
            <div class="stage-image">
              <div class="stage-count">{{ index + 1 }}</div>
              <img
                :src="`${this.backendURL}${stage.image}`"
                alt="stage image"
              >
            </div>

            <div class="stage-title" v-html="stage.title"></div>
          </div>
        </div>
        <div class="stages-delivery">
          <h2 class="stages-delivery-title" v-html="this.stages.delivery_title"></h2>
          <div class="stages-delivery-first" v-html="this.stages.delivery_first"></div>
          <div class="stages-delivery-second" v-html="this.stages.delivery_second"></div>
        </div>

      </div>
    </div>

    <div class="team">
      <div class="team-max">
        <div class="team-introduce">
          <div class="team-block-title">
            <h2 class="team-title" v-html="this.team.title"></h2>
            <div class="team-description" v-html="this.team.description"></div>
          </div>

          <div class="team-head-staff">
            <div class="team-staff" v-if="this.staffArr.length > 0">
              <div class="team-staff-image" v-if="this.staffArr[0].image !== null">
                <img
                    :src="`${this.backendURL}${this.staffArr[0].image}`"
                    :alt="`${this.staffArr[0].name} - ${this.staffArr[0].post}`"
                >
              </div>
              <div v-else class="team-staff-no-image">
                <img
                    src="src/assets/icons/icon-photo.svg"
                    :alt="`${this.staffArr[0].name} - ${this.staffArr[0].post}`"
                >
              </div>
              <h3 class="team-staff-title" v-html="this.staffArr[0].name"></h3>
              <div class="team-staff-post" v-html="this.staffArr[0].post"></div>
            </div>

            <div class="team-staff" v-if="this.staffArr.length > 0">
              <div class="team-staff-image" v-if="this.staffArr[1].image !== null">
                <img
                    :src="`${this.backendURL}${this.staffArr[1].image}`"
                    :alt="`${this.staffArr[1].name} - ${this.staffArr[1].post}`"
                >
              </div>
              <div v-else class="team-staff-no-image">
                <img
                    src="src/assets/icons/icon-photo.svg"
                    :alt="`${this.staffArr[1].name} - ${this.staffArr[1].post}`"
                >
              </div>
              <h3 class="team-staff-title" v-html="this.staffArr[1].name"></h3>
              <div class="team-staff-post" v-html="this.staffArr[1].post"></div>
            </div>
          </div>
        </div>

        <div class="team-grid" v-if="this.staffArr.slice(2).length > 0">
          <div class="team-staff" v-for="staff in this.staffArr.slice(2)">
              <div class="team-staff-image" v-if="staff.image !== null">
                <img
                    :src="`${this.backendURL}${staff.image}`"
                    :alt="`${staff.name} - ${staff.post}`"
                >
              </div>
              <div v-else class="team-staff-no-image">
                <img
                    src="src/assets/icons/icon-photo.svg"
                    :alt="`${staff.name} - ${staff.post}`"
                >
              </div>
              <h3 class="team-staff-title" v-html="staff.name"></h3>
              <div class="team-staff-post" v-html="staff.post"></div>
            </div>
        </div>
      </div>
    </div>

    <div class="request">
      <div class="request-max">
        <div class="request-background"></div>

        <div class="request-content">
          <div class="request-icon">
            <img src="src/assets/icons/icon-calculator.svg">
          </div>
          <div class="request-title">
            Получите расчёт стоимости
          </div>
          <div class="request-description">
            Оставьте заявку и получите предварительный расчёт стоимости вашей будущей мебели
          </div>
          <div class="request-form">
            <div class="request-form-item">
              <div class="request-form-label">
                Ваше имя
              </div>
              <div class="request-form-input">
                <input v-model="this.request2.name" type="text" name="input1" placeholder="Введите имя">
              </div>
            </div>

            <div class="request-form-item">
              <div class="request-form-label">
                Куда позвонить?
              </div>
              <div class="request-form-input">
                <input v-model="this.request2.phone" type="tel" name="input1" placeholder="+7 ___ ___-__-__">
              </div>
            </div>

            <div class="request-form-item">
              <div class="request-form-label">
                Какая мебель нужна?
              </div>
              <div class="request-form-input">
                <input v-model="this.request2.message" type="text" name="input1" placeholder="Расскажите, что Вас интересует">
              </div>
            </div>

            <div class="request-form-item">
              <div class="request-form-label">

              </div>
              <div class="request-form-submit" @click="this.sendRequest(this.request2)">
                Оставить заявку
              </div>
            </div>
          </div>
            <div class="request-acceptance">
              Нажимая кнопку «Оставить заявку» вы даете согласие на обработку персональных данных и принимаете условия <a>политики конфиденциальности</a>
            </div>
        </div>

      </div>
    </div>

    <div class="questions">
      <div class="questions-max">
        <h1 class="questions-title" v-html="this.questions.title"></h1>

        <div v-for="(question, index) in this.questionsArr" :key="question.order" class="questions-tile" @click="toggleQuestion(index)">
          <div class="questions-header">
            <div class="questions-text" v-html="question.question"></div>
            <img
                src="src/assets/icons/icon-plus.svg"
                class="toggle-icon"
                :style="question.isOpen ? 'transform: rotate(45deg);' : ''"

            >
          </div>
          <div :class="question.isOpen ? 'questions-answer-opened' : 'questions-answer-closed'" class="questions-answer" v-html="question.answer"></div>
        </div>
      </div>
    </div>

    <div class="reviews">
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

    <div class="request">
      <div class="request-max">
        <div class="request-background" style="height: 38rem;"></div>

        <div class="request-content">
          <div class="request-icon">
            <img src="src/assets/icons/icon-placeholder.svg">
          </div>
          <div class="request-title">
            Остались вопросы? <br> Приезжайте к нам в офис!
          </div>
          <div class="request-description">
            Вы сможете задать все вопросы нам лично и посмотреть выставочные образцы
          </div>
          <div class="request-form">
            <div class="request-form-item">
              <div class="request-form-label">
                Ваше имя
              </div>
              <div class="request-form-input">
                <input v-model="this.request3.name" type="text" name="input1" placeholder="Введите имя">
              </div>
            </div>

            <div class="request-form-item">
              <div class="request-form-label">
                Куда позвонить?
              </div>
              <div class="request-form-input">
                <input v-model="this.request3.phone" type="tel" name="input1" placeholder="+7 ___ ___-__-__">
              </div>
            </div>

            <div class="request-form-item">
              <div class="request-form-label">
                Выберите удобное время
              </div>
              <div class="request-form-input">
                <el-time-select
                  v-model="this.request3.selectedTime"
                  start="09:00"
                  step="00:30"
                  end="18:00"
                  placeholder="Выберите время"
                />
              </div>
            </div>

            <div class="request-form-item">
              <div class="request-form-label">

              </div>
              <div class="request-form-submit" @click="this.sendRequest(this.request3)">
                Записаться на встречу
              </div>
            </div>
          </div>
          <div class="request-acceptance">
            Нажимая кнопку «Записаться на встречу» вы даете согласие на обработку персональных данных и принимаете условия <a>политики конфиденциальности</a>
          </div>

          <div class="request-additional">
            <img src="src/assets/images/image-office-1.png" alt="" width="160" height="160" class="request-image">
            <img src="src/assets/images/image-office-2.png" alt="" width="160" height="160" class="request-image">
            <img src="src/assets/images/image-office-3.png" alt="" width="160" height="160" class="request-image">
          </div>
        </div>
      </div>
    </div>

    <div class="contacts">
      <div class="contacts-max">
        <div class="contacts-content">
          <h2 class="contacts-title" v-html="this.contacts.title"></h2>
          <div class="contacts-info">
            <div class="contacts-info-item">
              <div class="contacts-info-icon">
                <img src="src/assets/icons/icon-location.svg">
              </div>

              <div v-html="this.contacts.address"></div>
            </div>

            <div class="contacts-info-item">
              <div class="contacts-info-icon">
                <img src="src/assets/icons/icon-clock.svg">
              </div>

              <div v-html="this.contacts.schedule"></div>
            </div>

            <div class="contacts-info-item">
              <div class="contacts-info-icon">
                <img src="src/assets/icons/phone.svg" width="16" height="16">
              </div>

              <div v-html="this.contacts.number"></div>
            </div>

            <div class="contacts-info-links">
              <a class="contacts-link" :href="this.contacts.inst_link" target="_blank">Instagram*</a>

              <a class="contacts-link" :href="this.contacts.vk_link" target="_blank">ВКонтакте</a>
            </div>

          </div>
          <div class="contacts-photo">
            <img src="src/assets/images/image-contacts-1.png" width="180" height="180">
            <img src="src/assets/images/image-contacts-2.png" width="180" height="180">
          </div>
        </div>
        <div class="contacts-map">
           <GMapMap :center="center" :zoom="18" style="height: 600px">
             <GMapMarker :key="marker.id" v-for="marker in markers" :position="marker.position" />
           </GMapMap>
        </div>
      </div>
    </div>

    <div class="footer">
      <div class="footer-max">
        <div class="footer-left">
          <div class="">
            <img :src="`${this.backendURL}${this.header.logo}`" alt="РезАль - Мебельная компания. Логотип." width="138" height="34" />
          </div>

          <div class="footer-left-content">
            *организация «Meta» признана экстремистской и запрещена на территории России
          </div>
        </div>

        <div class="footer-center">
          <div class="footer-menu-item">
            О компании
          </div>
          <div class="footer-menu-item">
            Отзывы
          </div>
          <div class="footer-menu-item">
            Доставка и оплата
          </div>
          <div class="footer-menu-item">
            Портфолио
          </div>
          <div class="footer-menu-item">
            Контакты
          </div>
        </div>

        <div class="footer-right">
          <div class="footer-call-block">
            <div class="phone-number">
              <img src="src/assets/icons/phone.svg" alt="" width="16" height="16" />
              {{ this.header.number }}
            </div>

            <div class="phone-text">
              Заказать звонок
            </div>
          </div>

          <div class="footer-privacy">
            Политика конфиденциальности
          </div>
        </div>
      </div>
    </div>



  </div>
</template>

<script>
import axios from "axios";
import TextReviews from "../components/reviews/TextReviews.vue";
import VideoReviews from "../components/reviews/VideoReviews.vue";

export default {
  name: "MainView",
  inject: ['backendURL'],
  components: {
    // Swiper,
    // SwiperSlide,
    TextReviews,
    VideoReviews
  },

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

      center: { lat: 55.767724482181045, lng: 49.1041059787604 },
      markers: [
        {
          id: 'dfsldjl3r',
          position: {
            lat: 55.767724482181045,
            lng: 49.1041059787604,
          },
        },
      ],

      request1: {
        name: '',
        phone: '',
        message: '',
      },

      request2: {
        name: '',
        phone: '',
        message: '',
      },

      request3: {
        name: '',
        phone: '',
        selectedTime: '',
      },

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

    async sendRequest(request){
      let body = {
        request: {
          name: request.name,
          number: request.phone,
          message: request.message || '',
          comfortable_time: request.selectedTime || '',
          project_version: this.$projectVersion,
          user_agent: navigator.userAgent,
          screen_resolution: `${window.screen.width}x${window.screen.height}`,
          browser_language: navigator.language,
          timezone: new Date().getTimezoneOffset(),
          cookie: document.cookie
        }
      }
      console.log(body)
      await axios.post('api/v1/send_request', body)
    },

    toggleQuestion(index) {
      this.questionsArr[index].isOpen = !this.questionsArr[index].isOpen;
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

.request{
  width: 100%;
    /*height: 88vh;*/
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 100px;
  padding-bottom: 150px;
}

.request-max{
  width: 90rem;
  height: 90%;
  border-radius: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.request-background{
  background: linear-gradient(106.5deg, #1F1F1F 12.53%, #353535 105.97%);
  border-radius: 30px;
  height: 35rem;
  width: 90rem;
  position: absolute;
  z-index: -1;
  transform: translateY(5%);
}

.request-content{
  width: 67rem;
  display: flex;
  flex-direction: column;
  gap: 60px;
  height: 500px;
  position: relative;
}

.request-icon{
  color: #fff;
  background-color: #DD1D1D;
  border-radius: 20px;
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 42px;
  line-height: 54px;
  padding: 16px;
  width: 8%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.request-title{
  color: #fff;
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 42px;
  line-height: 54px;
}

.request-description{
  color: #fff;
  font-size: 18px;
  line-height: 1.4;
  width: 50%;
}

.request-form{
  display: flex;
  flex-direction: row;
  gap: 16px;
  margin-bottom: -40px;
}

.request-form-item{
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 8px;
}

.request-form-label{
  height: 25%;
  flex-basis: 25%;
  color: #888888;
}

input[type="text"], input[type="tel"] {
  border: 1px solid #ccc;
  border-radius: 13px;
  padding: 15px 15px;
  outline: none;
  font-family: OnestRegular, Inter, sans-serif;
  width: 88%;
}

input[type="text"]:focus, input[type="tel"]:focus {
  border-color: #DD1D1D;;
}

.request-form-submit{
  background-color: #DD1D1D;
  border-radius: 13px;
  color: #fff;
  font-size: 14px;
  line-height: 1.4;
  padding: 15px 15px;
  display: flex;
  justify-content: center;
}

.request-acceptance {
  color: #888888;
  font-size: 14px;
  line-height: 1.4;
}

.request-acceptance a{
  color: #DEDEDE;
  text-decoration: underline;
}

.request-additional {
  position: absolute;
  right: 0;
  display: flex;
  flex-direction: row;
  gap: 16px;
}

:deep(.el-input__wrapper) {
  padding: 10px 21px!important;
  border-radius: 13px!important;
}

:deep(.el-select .el-input.is-focus .el-input__wrapper) {
  border: 1px solid #DD1D1D;
  box-shadow: none !important;
}

:deep(.el-select .el-input__wrapper.is-focus){
  border: 1px solid #DD1D1D;
  box-shadow: none !important;
}

:deep(li.el-select-dropdown__item.selected){
  color: #DD1D1D!important;
}

select {
  border: 1px solid #ccc;
  border-radius: 13px;
  padding: 14px 15px;
  outline: none;
  font-family: OnestRegular, Inter, sans-serif;
  width: 100%;
  font-size: 14px;
}

select:focus {
  border-color: #DD1D1D;
}

.stages{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 150px;
  padding-bottom: 150px;
}

.stages-max{
  width: 67rem;
}

.stages-title{
  color: #000000;
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 36px;
  line-height: 54px;
  margin-bottom: 80px;
}

.stages-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 60px 16px;
  margin-bottom: 150px;
}

.stage {
  display: flex;
  flex-direction: column;
  gap: 30px;
  align-items: flex-start;
}

.stage-image{
  position: relative;
}

.stage-count {
  position: absolute;
  bottom: 0;
  left: 0;
  margin: 15px;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background-color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 16px;
  color: #000000;
  line-height: 0px;
}


.stage-image img {
  width: 100%;
  height: auto;
  display: block;
  /*margin-bottom: 20px;*/
}

.stage-title {
  color: #000000;
  font-size: 15px;
  line-height: 1.4;
  width: 90%;
}

.stages-delivery{
  display: flex;
  flex-direction: row;
  gap: 100px;
}

.stages-delivery-title{
  color: #000000;
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 36px;
  line-height: 54px;
  width: 16%;
  flex-basis: 16%;
}

.stages-delivery-first{
  flex: 1;
  color: #000000;
  line-height: 1.4;
  font-size: 16px;
}

.stages-delivery-second{
  flex: 1;
  color: #000000;
  line-height: 1.4;
  font-size: 16px;
}


.team{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-bottom: 150px;
}

.team-max{
  width: 67rem;
}

.team-introduce{
  display: flex;
  flex-direction: row;
  gap: 16px;
}

.team-block-title{
  width: 50%;
  flex-basis: 50%;
}

.team-title{
  color: #000000;
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 36px;
  line-height: 54px;
  margin-bottom: 30px;
}

.team-description{
  width: 80%;
  color: #000000;
  line-height: 1.4;
  font-size: 16px;
}

.team-head-staff{
  width: 50%;
  flex-basis: 50%;
  display: flex;
  flex-direction: row;
  gap: 16px;
}

.team-staff{
  /*height: 400px;*/
  width: 100%;
}

.team-staff-image{
  border-radius: 30px;
  height: 350px;
  width: 100%;
}

.team-staff-image img{
  width: 100%;
  border-radius: 30px;
  object-fit: cover;
  height: 350px;
}

.team-staff-no-image{
  background: #ECECEC;
  border-radius: 30px;
  height: 350px;
  width: 100%;
  position: relative;
}

.team-staff-no-image img{
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.team-staff-title{
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 22px;
  padding-top: 20px;
  line-height: 31px;
}

.team-staff-post{
  color: #686868;
  font-size: 16px;
  line-height: 1.4;
  padding-top: 5px;
}

.team-grid{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-gap: 60px 16px;
  margin-bottom: 150px;
  padding-top: 60px;
}

.questions{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 150px;
  padding-bottom: 150px;
}

.questions-max{
  width: 67rem;
}

.questions-title{
  color: #000000;
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 36px;
  line-height: 54px;
  margin-bottom: 80px;
}

.questions-tile{
  border: 1px solid #BDBDBD;
  border-radius: 20px;
  margin-bottom: 30px;
  padding: 25px 35px;
  transition: height 0.2s ease-in-out;
  cursor: pointer;
}

.questions-header{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

.questions-text{
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 22px;
  line-height: 31px;
}

.toggle-icon {
  /*width: 35px;*/
  /*height: 35px;*/
  padding: 8px;
  border-radius: 50%;
  border: 1px solid #BDBDBD !important;
  background-color: white;
  color: #DD1D1D;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 0.1s ease-in-out;
}

img.toggle-icon{
  height: 16px;
  width: 16px;
  fill: white;
}

.questions-answer{
  line-height: 1.4;
  font-size: 15px;
  color: #000000;
  transition: all 0.2s ease-in-out;
}

.questions-answer-closed{
  padding-top: 0;
  height: 0;
  opacity: 0;
}

.questions-answer-opened{
  padding-top: 20px;
  height: auto;
  opacity: 1;
}

.reviews{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.reviews-max{
  max-width: 67rem;
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
}

.reviews-video {
  position: relative;
  margin-bottom: 80px;
}

.contacts{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 150px;
  padding-bottom: 150px;
}

.contacts-max{
  width: 67rem;
  display: flex;
  flex-direction: row;
}

.contacts-content{
  display: flex;
  flex-direction: column;
  width: 40%;
  flex-basis: 40%;
}

.contacts-title{
  color: #000000;
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 36px;
  line-height: 54px;
  margin-bottom: 80px;
}

.contacts-info{
  display: flex;
  flex-direction: column;
  gap: 16px;
  flex: 1;
}

.contacts-info-item{
  display: flex;
  flex-direction: row;
  gap: 8px;
  color: black;
  line-height: 1.4;
  font-size: 16px;
}

.contacts-info-icon{
  display: flex;
  width: 24px;
  justify-content: center;
  align-items: center;
}

.contacts-info-links{
  display: flex;
  flex-direction: row;
  gap: 16px;
}

.contacts-info-links a{
  color: #DD1D1D;
  text-decoration: none;
}

.contacts-photo{
  display: flex;
  flex-direction: row;
  gap: 16px;
}

.contacts-map{
  width: 60%;
  flex-basis: 60%;
  height: 600px;
}

.footer{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-bottom: 60px;
}

.footer-max{
  width: 67rem;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: space-between;
  height: 150px;
}

.footer-left{
  width: 20%;
  flex-basis: 20%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.footer-left-content{
  color: #BBBBBB;
  font-size: 14px;
  line-height: 20px;
}

.footer-center{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 20px 16px;
}


.footer-menu-item{
  width: auto;
  font-color: #000;
  font-size: 16px;
  line-height: 23px;
}

.footer-right{
  width: 20%;
  flex-basis: 20%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.footer-call-block{
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  cursor: pointer;
}

.footer-privacy{
  color: #BBBBBB;
  font-size: 14px;
  line-height: 20px;
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