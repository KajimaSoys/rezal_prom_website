<template>
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
</template>

<script>
export default {
  name: "Footer",
  inject: ['backendURL'],
  props: [
    'header',
  ],
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