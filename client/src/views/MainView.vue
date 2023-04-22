<template>
ебать дела
</template>

<script>
import axios from "axios";

export default {
  name: "MainView",
  data(){
    return {
      stagesArr: [],
      staffArr: [],
      questionsArr: [],
      reviewTextArr: [],
      reviewVideoArr: [],

      headers: {},
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
                this.headers = block.data
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

</style>