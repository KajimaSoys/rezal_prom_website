<template>
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
</template>

<script>
export default {
  name: "Main",
  inject: ['backendURL'],
  props: [
    'main',
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
</style>