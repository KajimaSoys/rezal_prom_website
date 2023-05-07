<template>
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
</template>

<script>
export default {
  name: "Header",
  inject: ['backendURL'],
  props: [
    'header',
  ]
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
</style>