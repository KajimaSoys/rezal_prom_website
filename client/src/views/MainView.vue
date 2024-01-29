<template>
  <div class="content">

    <Header :header="header" @popUpCall="popUpCall()"/>

    <Main :main="main" @popUpCall="popUpCall()"/>

    <About :about="about"/>

    <Production :production="production"/>

    <Services :services="services"/>

    <Projects :projects="projects"/>

    <Request requestNum="1"/>

    <Stages :stages="stages" :stagesArr="stagesArr"/>

    <Team :team="team" :staffArr="staffArr"/>

    <Request requestNum="2"/>

    <Questions :questions="questions" :questionsArr="questionsArr"/>

    <Reviews :reviews="reviews" :reviewTextArr="reviewTextArr" :reviewVideoArr="reviewVideoArr"/>

    <Request requestNum="3"/>

    <Contacts :contacts="contacts"/>

    <Footer :header="header" :meta="true" @popUpCall="popUpCall()"/>

    <VideoPlayer :visible="videoVisible" :videoId="videoId" @close="hideVideo"/>

    <PopUp :visible="popUpVisible" @close="hidePopUp"/>

  </div>
</template>

<script>
import axios from "axios";
import provideVideoPlayer from '../mixins/provideVideoPlayer.js';

import Header from "../components/Header.vue";
import Main from "../components/Main.vue";
import About from "../components/About.vue";
import Production from "../components/Production.vue";
import Services from "../components/Services.vue";
import Projects from "../components/Projects.vue";
import Request from "../components/Request.vue";
import Stages from "../components/Stages.vue";
import Team from "../components/Team.vue";
import Questions from "../components/Questions.vue";
import Reviews from "../components/Reviews.vue";
import Contacts from "../components/Contacts.vue";
import Footer from "../components/Footer.vue";
import VideoPlayer from '../components/VideoPlayer.vue';
import PopUp from "../components/PopUp.vue";


export default {
  name: "MainView",
  inject: ['backendURL'],
  components: {
    Header,
    Main,
    About,
    Production,
    Services,
    Projects,
    Request,
    Stages,
    Team,
    Questions,
    Reviews,
    Contacts,
    Footer,
    VideoPlayer,
    PopUp
  },
  mixins: [provideVideoPlayer],

  data() {
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

      videoVisible: false,
      videoId: '',
      popUpVisible: false,
    }
  },

  methods: {
    async getPageData() {
      await axios
          .get('api/v1/all_blocks/')
          .then(response => {
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
              }
            });

            // console.log(response.data)
          })
          .catch(error => {
            console.log('An error occurred: ', error)
          })
    },

    async getObjectsData() {
      await axios
          .get('api/v1/core_objects/')
          .then(response => {
            let receivedData = response.data
            receivedData.forEach(block => {
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

            // console.log(response.data)
          })
          .catch(error => {
            console.log('An error occurred: ', error)
          })
    },

    popUpCall() {
      this.popUpVisible = true;
      document.body.style.overflow = "hidden";
    },
    hidePopUp() {
      this.popUpVisible = false;
      document.body.style.overflow = "";
    },

  },

  beforeMount() {
    this.getPageData()
    this.getObjectsData()
  },

}
</script>

<style scoped>

</style>