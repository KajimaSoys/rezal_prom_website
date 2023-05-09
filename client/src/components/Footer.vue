<template>
  <div class="footer">
    <div class="footer-max">
      <div class="footer-left">
        <a class="footer-logo" href="/">
          <img :src="`${this.backendURL}${this.header.logo}`" alt="РезАль - Мебельная компания. Логотип." width="170" height="60" />
        </a>

        <div class="footer-left-content" v-if="this.meta">
          *организация «Meta» признана экстремистской и запрещена на территории России
        </div>
      </div>

      <div class="footer-center">
        <a class="footer-menu-item" @click="this.scrollToElement('about')">
          О компании
        </a>
        <a class="footer-menu-item" @click="this.scrollToElement('projects')">
          Отзывы
        </a>
        <a class="footer-menu-item" @click="this.scrollToElement('delivery')">
          Доставка и оплата
        </a>
        <a class="footer-menu-item" @click="this.scrollToElement('reviews')">
          Портфолио
        </a>
        <a class="footer-menu-item" @click="this.scrollToElement('contacts')">
          Контакты
        </a>
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

        <router-link to="policy" class="footer-privacy">
          Политика конфиденциальности
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Footer",
  inject: ['backendURL'],
  props: [
    'header',
    'meta',
  ],
  methods: {
    scrollToElement(elementId) {
      const element = document.getElementById(elementId);

      if (this.$route.path === "/"){
        element.scrollIntoView({ behavior: "smooth" });
      } else {
        this.$router.push({ path: "/", hash: `#${elementId}` });
      }
    },
  }
}
</script>

<style scoped>
.footer{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-bottom: 60px;
}

.footer-max {
  width: 67rem;
  margin: 0 2rem;
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
  text-decoration: none;
  transition: color 0.2s ease-in-out;
  cursor: pointer;
}

.footer-menu-item:hover{
  color: #7A7A7A;
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

.phone-text{
  color: #DD1D1D;
  transition: color 0.2s ease-in-out;
}

.phone-text:hover{
  color: #C20D0D;
}

.footer-privacy{
  color: #BBBBBB;
  font-size: 14px;
  line-height: 20px;
  text-decoration: none;
  transition: color 0.3s ease-in-out;
}

.footer-privacy:hover{
  color: #888888;
}

@media screen and (max-width: 990px) {
  .footer-max {
    flex-direction: column;
    align-items: center;
    height: auto;
    padding-top: 30px;
  }

  .footer-left {
    width: 100%;
    flex-basis: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 20px;
  }

  .footer-center {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin-bottom: 20px;
  }

  .footer-right {
    width: 100%;
    flex-basis: auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
  }

  .footer-call-block {
    margin-bottom: 10px;
    align-items: center
  }
}

/* When the screen size is less than or equal to 640px */
@media screen and (max-width: 640px) {
  .footer-max {
    flex-direction: column;
    align-items: center;
    height: auto;
    padding-top: 30px;
  }

  .footer-left {
    width: 100%;
    flex-basis: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 20px;
  }

  .footer-left-content{
    text-align: center;
  }

  .footer-center {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 20px;
  }

  .footer-menu-item {
    margin-bottom: 10px;
  }

  .footer-right {
    width: 100%;
    flex-basis: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .footer-call-block {
    margin-bottom: 10px;
    align-items: center
  }
}
</style>