<template>

  <div class="request" v-if="this.requestNum==1">
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

  <div class="request" v-if="this.requestNum==2">
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

  <div class="request" v-if="this.requestNum==3">
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
</template>

<script>
import axios from "axios";

export default {
  name: "Request",
  props: [
    'requestNum',
  ],
  data(){
    return {
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
  },
}
</script>

<style scoped>
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
  cursor: pointer;
  transition: all .1s ease-in-out;
}

.request-form-submit:hover{
  background-color: #C20D0D;
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
</style>