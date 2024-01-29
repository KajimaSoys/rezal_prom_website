<template>
  <div class="not-found-view">
    <Header :header="header" @popUpCall="popUpCall()"/>

    <div class="not-found-component">
      <h1>Страница не найдена</h1>
    </div>

    <Footer :header="header" :meta="false" @popUpCall="popUpCall()"/>
  </div>

  <PopUp :visible="popUpVisible" @close="hidePopUp"/>
</template>

<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import PopUp from "../components/PopUp.vue";
import axios from "axios";

export default {
  name: "NotFoundView.vue",
  components: {
    Header,
    Footer,
    PopUp,
  },
  data() {
    return {
      header: '',
      popUpVisible: false,
    }
  },

  methods: {
    async getHeaderData() {
      await axios
          .get('api/v1/blocks/header/')
          .then(response => {
            this.header = response.data[0]
            let logo = this.header.logo
            const parts = logo.split('/'); // Разделить строку на массив с помощью разделителя '/'
            parts.splice(0, 3); // Удалить первые три элемента массива (http:, '', 127.0.0.1:8000)
            this.header.logo = '/' + parts.join('/');
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
    this.getHeaderData()
  },
  mounted() {
    document.body.style.overflow = "";
    document.documentElement.scrollTop = 0;
  },
}
</script>

<style scoped>

.not-found-view {
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.not-found-component {
  max-width: 80rem;
  margin-left: auto;
  margin-right: auto;
  padding: 2rem 2rem 6rem;
  margin-top: 10vh;
  flex: 1;
}

h1 {
  text-align: center;
  padding-top: 2rem;
  padding-bottom: 2rem;
  font-family: OnestMedium, Inter, sans-serif;
  font-size: 2rem;
}

@media screen and (max-width: 640px) {
  h1 {
    font-size: 1.5rem;
  }
}

</style>
