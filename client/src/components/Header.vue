<template>
  <div class="header">
    <div class="header-max">
      <a class="logo" href="#">
        <img :src="`${this.backendURL}${this.header.logo}`" alt="РезАль - Мебельная компания. Логотип." width="170" height="60" />
      </a>

      <div class="menu">
        <a class="menu-item" @click="this.scrollToElement('about')">
          О компании
        </a>
        <a class="menu-item" @click="this.scrollToElement('projects')">
          Портфолио
        </a>
        <a class="menu-item" @click="this.scrollToElement('delivery')">
          Доставка и оплата
        </a>
        <a class="menu-item" @click="this.scrollToElement('reviews')">
          Отзывы
        </a>
        <a class="menu-item" @click="this.scrollToElement('contacts')">
          Контакты
        </a>
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
</template>

<script>
export default {
  name: "Header",
  inject: ['backendURL'],
  props: [
    'header',
  ],
  methods: {
    scrollToElement(elementId) {
      const element = document.getElementById(elementId);
      element.scrollIntoView({ behavior: "smooth" });
    },
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
  text-decoration: none;
  color: black;
  cursor: pointer;
  position: relative;
  transition: color 0.4s ease;
}

.menu-item:hover{
  color: #DD1D1D;
}

.menu-item:before {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  right: 50%;
  background: #DD1D1D;
  height: 2px;
  transition: all .4s ease;
}

.menu-item:hover:before {
  left: 0;
  right: 0;
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
  transition: color 0.2s ease-in-out;
}

.phone-text:hover{
  color: #C20D0D;;
}
</style>