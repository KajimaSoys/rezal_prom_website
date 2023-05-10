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
        <div class="request-form" v-if="!request1.isSubmitted">
          <div class="request-form-item">
            <div class="request-form-label">
              Ваше имя<span style="color: #DD1D1D; font-size: 24px">*</span>
            </div>
            <div class="request-form-input">
              <input
                  v-model="this.request1.name"
                  type="text"
                  name="input1"
                  placeholder="Введите имя"
                  required
              >
            </div>
          </div>

          <div class="request-form-item">
            <div class="request-form-label">
              Куда позвонить?<span style="color: #DD1D1D; font-size: 24px">*</span>
            </div>
            <div class="request-form-input">
              <input
                  type="text"
                  name="input1"
                  placeholder="+7 (___) ___-__-__"
                  v-mask="'+7 (###) ###-##-##'"
                  required
                  v-model="this.request1.phone"
              >
            </div>
          </div>

          <div class="request-form-item">
            <div class="request-form-label">
              Какая мебель нужна?
            </div>
            <div class="request-form-input">
              <input
                  v-model="this.request1.message"
                  type="text"
                  name="input1"
                  placeholder="Расскажите, что Вас интересует"
              >
            </div>
          </div>

          <div class="request-form-item">
            <div class="request-form-label">

            </div>
            <div class="request-form-submit" :class="{ 'pending': request1.pending}" @click="this.sendRequest(this.request1)">
              {{ this.request1.sendButton }}
            </div>
          </div>
        </div>

        <div class="request-error" v-if="request1.nameError || request1.phoneError">
          Пожалуйста, заполните обязательные поля
        </div>

        <div class="request-acceptance" v-if="!request1.isSubmitted">
          Нажимая кнопку «Оставить заявку» вы даете согласие на обработку персональных данных и принимаете условия <router-link to="policy" class="request-link">политики конфиденциальности</router-link>
        </div>
        <div class="request-success" v-else>
          <div class="request-success-title">Ваша заявка <span style="color: #DD1D1D">принята!</span></div>
          <div class="request-success-description">Наш менеджер позвонит вам в ближайшее время для уточнения деталей</div>
        </div>
      </div>

    </div>
  </div>

  <div class="request" v-if="this.requestNum==2">
    <div class="request-max">
      <div class="request-background"></div>

      <div class="request-content">
        <div class="request-icon">
          <img src="/icons/icon-calculator.svg">
        </div>
        <div class="request-title">
          Получите расчёт стоимости
        </div>
        <div class="request-description">
          Оставьте заявку и получите предварительный расчёт стоимости вашей будущей мебели
        </div>
        <div class="request-form" v-if="!request2.isSubmitted">
          <div class="request-form-item">
            <div class="request-form-label">
              Ваше имя<span style="color: #DD1D1D; font-size: 24px">*</span>
            </div>
            <div class="request-form-input">
              <input
                  v-model="this.request2.name"
                  type="text"
                  name="input1"
                  placeholder="Введите имя"
              >
            </div>
          </div>

          <div class="request-form-item">
            <div class="request-form-label">
              Куда позвонить?<span style="color: #DD1D1D; font-size: 24px">*</span>
            </div>
            <div class="request-form-input">
              <input
                  v-model="this.request2.phone"
                  type="tel"
                  name="input1"
                  placeholder="+7 (___) ___-__-__"
                  v-mask="'+7 (###) ###-##-##'"
              >
            </div>
          </div>

          <div class="request-form-item">
            <div class="request-form-label">
              Какая мебель нужна?
            </div>
            <div class="request-form-input">
              <input
                  v-model="this.request2.message"
                  type="text"
                  name="input1"
                  placeholder="Расскажите, что Вас интересует"
              >
            </div>
          </div>

          <div class="request-form-item">
            <div class="request-form-label">

            </div>
            <div class="request-form-submit" :class="{ 'pending': request2.pending}" @click="this.sendRequest(this.request2)">
              {{ this.request2.sendButton }}
            </div>
          </div>
        </div>

        <div class="request-error" v-if="request2.nameError || request2.phoneError">
          Пожалуйста, заполните обязательные поля
        </div>

        <div class="request-acceptance" v-if="!request2.isSubmitted">
          Нажимая кнопку «Оставить заявку» вы даете согласие на обработку персональных данных и принимаете условия <router-link to="policy" class="request-link">политики конфиденциальности</router-link>
        </div>
        <div class="request-success" v-else>
          <div class="request-success-title">Ваша заявка <span style="color: #DD1D1D">принята!</span></div>
          <div class="request-success-description">Наш менеджер позвонит вам в ближайшее время для уточнения деталей</div>
        </div>
      </div>

    </div>
  </div>

  <div class="request" v-if="this.requestNum==3" id="request-time">
    <div class="request-max">
      <div class="request-background"></div>

      <div class="request-content">
        <div class="request-icon">
          <img src="/icons/icon-placeholder.svg">
        </div>
        <div class="request-title">
          Остались вопросы? <br> Приезжайте к нам в офис!
        </div>
        <div class="request-description">
          Вы сможете задать все вопросы нам лично и посмотреть выставочные образцы
        </div>
        <div class="request-form" v-if="!request3.isSubmitted">
          <div class="request-form-item">
            <div class="request-form-label">
              Ваше имя<span style="color: #DD1D1D; font-size: 24px">*</span>
            </div>
            <div class="request-form-input">
              <input
                  v-model="this.request3.name"
                  type="text"
                  name="input1"
                  placeholder="Введите имя"
              >
            </div>
          </div>

          <div class="request-form-item">
            <div class="request-form-label">
              Куда позвонить?<span style="color: #DD1D1D; font-size: 24px">*</span>
            </div>
            <div class="request-form-input">
              <input
                  v-model="this.request3.phone"
                  type="tel"
                  name="input1"
                  placeholder="+7 (___) ___-__-__"
                  v-mask="'+7 (###) ###-##-##'"
              >
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
            <div class="request-form-submit" :class="{ 'pending': request3.pending}" @click="this.sendRequest(this.request3)">
              {{ this.request3.sendButton }}
            </div>
          </div>
        </div>

        <div class="request-error" v-if="request3.nameError || request3.phoneError">
          Пожалуйста, заполните обязательные поля
        </div>

        <div class="request-acceptance" v-if="!request3.isSubmitted">
          Нажимая кнопку «Записаться на встречу» вы даете согласие на обработку персональных данных и принимаете условия <router-link to="policy" class="request-link">политики конфиденциальности</router-link>
        </div>
        <div class="request-success" v-else>
          <div class="request-success-title">Ваша заявка <span style="color: #DD1D1D">принята!</span></div>
          <div class="request-success-description">Наш менеджер позвонит вам в ближайшее время для уточнения деталей</div>
        </div>

        <div class="request-additional">
          <img src="/image/image-office-1.png" alt="" width="160" height="160" class="request-image">
          <img src="/image/image-office-2.png" alt="" width="160" height="160" class="request-image">
          <img src="/image/image-office-3.png" alt="" width="160" height="160" class="request-image">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {mask} from 'vue-the-mask'

export default {
  name: "Request",
  props: [
    'requestNum',
  ],

  directives: {mask},

  data(){
    return {
      request1: {
        name: '',
        phone: '',
        message: '',
        nameError: false,
        phoneError: false,
        isSubmitted: false,
        sendButton: 'Оставить заявку',
        pending: false,
      },

      request2: {
        name: '',
        phone: '',
        message: '',
        nameError: false,
        phoneError: false,
        isSubmitted: false,
        sendButton: 'Оставить заявку',
        pending: false,
      },

      request3: {
        name: '',
        phone: '',
        selectedTime: '',
        nameError: false,
        phoneError: false,
        isSubmitted: false,
        sendButton: 'Записаться на встречу',
        pending: false,
      },
    }
  },

  methods: {
    async sendRequest(request){
      request.nameError = false;
      request.phoneError = false;

      if (request.name.length < 3) {
        request.nameError = true;
      }

      if (request.phone.length !== 18) {
        request.phoneError = true;
      }

      if (!request.nameError && !request.phoneError) {
        request.sendButton = 'Пожалуйста, подождите..'
        request.pending = true

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
        await axios
            .post('api/v1/send_request/', body)
            .then(response => {
              request.pending = false
              console.log(response)
            })
            .catch(error => {
              console.log(error)
            })

        request.isSubmitted = true;
      }
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
  padding-top: 75px;
  padding-bottom: 75px;
}

.request-max{
  width: 90rem;
  height: 90%;
  border-radius: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0 2rem;
}

.request-background{
  background: linear-gradient(106.5deg, #1F1F1F 12.53%, #353535 105.97%);
  border-radius: 30px;
  height: 35rem;
  width: 100%;
  max-width: 90rem;
  padding: 0 2rem;
  position: absolute;
  z-index: -1;
  transform: translateY(5%);
}

#request-time > div > div.request-background{
  height: 38rem;
}

.request-content{
  max-width: 67rem;
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 60px;
  /*height: 500px;*/
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
  width: 70%;
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
  border-color: #DD1D1D;
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

.pending{
  pointer-events: none;
}

.request-error {
    margin-bottom: -50px;
    color: #DD1D1D;
}

.request-success {
  color: #FFFFFF;
}

.request-success-title{
  text-align: center;
  font-family: 'OnestMedium', Inter, sans-serif;
  font-size: 28px;
  padding-top: 40px;
}

.request-success-description{
  text-align: center;
  padding-top: 20px;
}


.request-acceptance {
  color: #888888;
  font-size: 14px;
  line-height: 1.4;
}

.request-acceptance a{
  color: #DEDEDE;
  position: relative;
  text-decoration: none;
}

.request-acceptance a:before {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  right: 50%;
  background: #DEDEDE;
  height: 1px;
  transition: all .4s ease;
}

.request-acceptance a:hover:before {
  left: 0;
  right: 0;
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

@media screen and (max-width: 990px){
  .request-background{
    height: 51rem;

    padding: 0;
    margin: 0 2rem;
    border-radius: 0;
  }

  #request-time > div > div.request-background{
    height: 54rem;
  }

  .request-icon{
    width: 12%;
  }

  .request-title {
    font-size: 36px;
    line-height: 40px;
}

  .request-description{
    margin-bottom: -40px;
    font-size: 16px;
  }

  .request-form{
    flex-direction: column;
    width: 40%;
  }

  .request-acceptance{
    width: 90%;
  }

  .request-form-submit{
    width: 75%;
    margin: 1rem auto auto;
  }

  input[type="text"], input[type="tel"]{
    width: 90%;
  }

  .el-select{
    width: 100%;
  }

  .request-additional{
    visibility: hidden;
  }

  .request-success {
    padding-bottom: 18rem;
  }
}

@media screen and (max-width: 640px){
  .request-background{
    height: 53rem;
  }

  #request-time > div > div.request-background{
    height: 57rem;
  }

  .request-icon{
    width: 20%;
  }

  .request-title{
    font-size: 32px;
    line-height: 40px;
}

  .request-description{
    width: 100%;
    font-size: 14px;
  }

  .request-form{
    width: 100%;
  }

  .request-acceptance{
    width: 100%;
    font-size: 12px;
  }
}
</style>