<template>
  <div class="main">
    <div class="main-max"
         :style="{ 'background-image': `linear-gradient(180deg, rgba(0, 0, 0, 0.7) 0%, rgba(0, 0, 0, 0.6) 48.37%, rgba(0, 0, 0, 0.8) 100%), url(${this.backendURL}${this.main.image})`, 'background-size': 'cover', 'background-position': 'center center', 'transform': 'scale(1)' }">
      <div class="main-title">
        <h1>{{ this.main.title }}</h1>
      </div>
      <div class="main-secondary">
        <div class="main-description">
          {{ this.main.description }}
        </div>

        <div class="main-buttons">
          <div class="main-request-button" @click="this.$emit('popUpCall')">
            Оставить заявку
          </div>

          <div class="main-count-button" @click="this.$emit('popUpCall')">
            Рассчитать стоимость
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Main",
  inject: ['backendURL'],
  props: [
    'main',
  ],
  emits: [
    'popUpCall'
  ],
}
</script>

<style scoped>
.main{
  width: 100%;
  height: 88vh;
  display: flex;
  justify-content: center;
  align-items: center;
  /*padding-bottom: 75px;*/
  margin-top: 10vh;
}

.main-max{
  max-width: 90rem;
  height: 95%;
  border-radius: 30px;
  display: flex;
  flex-direction: column;
  margin: 0 2rem;
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
  font-size: 40px;
  line-height: 55px;
}

.main-secondary{
  padding: 0 175px 100px 175px;
  height: 20%;
  flex-basis: 20%;
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  justify-content: space-evenly;
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
  cursor: pointer;
  transition: all .1s ease-in-out;
}

.main-request-button:hover{
  background-color: #C20D0D;
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
  cursor: pointer;
  transition: all .2s ease-in-out;
}

.main-count-button:hover{
  border-color: #FFFFFF;
  background-color: #FFFFFF;
  color: #000000;
}

@media screen and (max-width: 1200px){
  .main-title{
    padding: 100px 100px 0 100px;
    font-size: 40px;
  }

  .main-title h1{
    font-size: 36px;
  }

  .main-secondary{
    padding: 0 100px 100px 100px;
  }

  .main-description{
    font-size: 16px;
  }

  .main-buttons {
    /*width: 60%;*/
    font-size: 14px;
  }

}
@media screen and (max-width: 990px) {
  .main-title {
    padding: 100px 50px 0 50px;
    font-size: 30px;
  }

  .main-title h1 {
    font-size: 30px;
    line-height: 40px;
  }

  .main-secondary {
    padding: 0 50px 100px 50px;
    flex-direction: column;
  }

  .main-description {
    font-size: 16px;
    max-width: 100%;
    flex-basis: auto;
    margin-bottom: 16px;
  }

  .main-buttons {
    width: 100%;
    flex-basis: auto;
    flex-direction: row;
    gap: 10px;
    height: auto;
    justify-content: center;
  }

  .main-request-button,
  .main-count-button {
    width: 100%;
    flex-basis: auto;
    padding: 10px 0;
  }
}

@media screen and (max-width: 640px) {
  .main-max {
    border-radius: 0;
    padding: 0;
    margin: 0;
    gap: 10%;
  }

  .main-title {
    padding: 75px 25px 0 25px;
    width: 85%;
  }

  .main-title h1 {
    font-size: 22px;
    line-height: 32px;
  }

  .main-secondary {
    padding: 0 25px 75px 25px;
    align-items: center;
    flex: 1;
  }

  .main-description {
    font-size: 15px;
    line-height: 24px;
  }

  .main-buttons {
    flex-direction: column;
    /*width: 60%;*/
    font-size: 12px;
  }
}

@media screen and (max-width: 360px) {
  .main-max {
    gap: 5%;
  }
  .main-title[data-v-3fa90f43] {
      padding: 50px 25px 0 25px;
  }
}
</style>