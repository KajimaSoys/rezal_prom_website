<template>
  <transition name="fade">
    <div v-if="visible" class="popup-background" @click.self="close">
      <div class="popup">
        <div class="popup-max">
          <div class="popup-content">
            <div class="popup-title" v-if="!popup.isSubmitted">
              Оставить заявку
            </div>
            <div class="popup-form" v-if="!popup.isSubmitted">
              <div class="popup-form-item">
                <div class="popup-form-label">
                  Ваше имя<span style="color: #DD1D1D; font-size: 24px">*</span>
                </div>
                <div class="popup-form-input">
                  <input
                      v-model="this.popup.name"
                      type="text"
                      name="input1"
                      placeholder="Введите имя"
                      required
                  >
                </div>
              </div>

              <div class="popup-form-item">
                <div class="popup-form-label">
                  Куда позвонить?<span style="color: #DD1D1D; font-size: 24px">*</span>
                </div>
                <div class="popup-form-input">
                  <input
                      type="text"
                      name="input1"
                      placeholder="+7 (___) ___-__-__"
                      v-mask="'+7 (###) ###-##-##'"
                      required
                      v-model="this.popup.phone"
                  >
                </div>
              </div>

              <div class="popup-form-item">
                <div class="popup-form-label">
                  Какая мебель нужна?
                </div>
                <div class="popup-form-input">
                  <input
                      v-model="this.popup.message"
                      type="text"
                      name="input1"
                      placeholder="Расскажите, что Вас интересует"
                  >
                </div>
              </div>

              <div class="popup-form-item">
                <div class="popup-form-label">

                </div>
                <div class="popup-form-submit" :class="{ 'pending': pending}" @click="this.sendPopUp(this.popup)">
                  {{ this.sendButton }}
                </div>
              </div>
            </div>

            <div class="popup-error" v-if="popup.nameError || popup.phoneError">
              Пожалуйста, заполните обязательные поля
            </div>

            <div class="popup-acceptance" v-if="!popup.isSubmitted">
              Нажимая кнопку «Оставить заявку» вы даете согласие на обработку персональных данных и принимаете условия <router-link to="policy" class="popup-link">политики конфиденциальности</router-link>
            </div>
            <div class="popup-success" v-else>
              <div class="popup-success-title">Ваша заявка <span style="color: #DD1D1D">принята!</span></div>
              <div class="popup-success-description">Наш менеджер позвонит вам в ближайшее время для уточнения деталей</div>
              <div class="popup-form-submit" @click="close">
                Закрыть
              </div>
            </div>
          </div>
        </div>

        <button class="close-btn" @click="close" ref="closePopUp">
          <span>&times;</span>
        </button>
      </div>


    </div>
  </transition>
</template>

<script>
import {mask} from "vue-the-mask";
import axios from "axios";
import { useYandexMetrika } from 'yandex-metrika-vue3'

export default {
  name: "PopUp",
  directives: {mask},
  props: {
    visible: {
      type: Boolean,
      default: false,
    },
  },
  data(){
    return {
      popup: {
        name: '',
        phone: '',
        message: '',
        nameError: false,
        phoneError: false,
        isSubmitted: false,
      },
      sendButton: 'Оставить заявку',
      pending: false,
    }
  },

  methods: {
    async sendPopUp(popup){
      popup.nameError = false;
      popup.phoneError = false;

      if (popup.name.length < 3) {
        popup.nameError = true;
      }

      if (popup.phone.length !== 18) {
        popup.phoneError = true;
      }

      if (!popup.nameError && !popup.phoneError) {
        this.sendButton = 'Пожалуйста, подождите..'
        this.pending = true

        let body = {
          request: {
            name: popup.name,
            number: popup.phone,
            message: popup.message || '',
            comfortable_time: popup.selectedTime || '',
            project_version: this.$projectVersion,
            user_agent: navigator.userAgent,
            screen_resolution: `${window.screen.width}x${window.screen.height}`,
            browser_language: navigator.language,
            timezone: new Date().getTimezoneOffset(),
            cookie: document.cookie
          }
        }

        const yandexMetrika = useYandexMetrika()
        yandexMetrika.reachGoal('Заявка отправлена (всплывающее окно)')

        await axios
            .post('api/v1/send_request/', body)
            .then(response => {
              this.pending = false
              console.log(response)
            })
            .catch(error => {
              console.log(error)
            })

        popup.isSubmitted = true;
      }
    },

    close() {
      this.$emit('close');
    },
  },
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

.popup-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1010;
}

.popup {
  background-color: white;
  border-radius: 28px;
  padding: 3rem;
  position: relative;
  z-index: 1011;
}

.close-btn {
  position: absolute;
  /*top: 10px;*/
  /*right: 10px;*/
  /*color: white;*/
  /*font-size: 24px;*/
  /*cursor: pointer;*/
  z-index: 1001;
  top: -50px;
  right: -95px;
  background: transparent;
  border: none;
  color: rgba(255, 255, 255, 0.7);
  font-size: 3rem;
  cursor: pointer;
  padding: 5px 10px;
  transition: color 0.1s ease-in-out;
}

.close-btn:hover {
  color: rgba(255, 255, 255, 1);
}

.popup-content{
  max-width: 24rem;
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 16px;
  /*height: 500px;*/
  position: relative;
  align-items: center;
}

.popup-title{
  color: #000;
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 42px;
  line-height: 54px;
}

.popup-form{
  display: flex;
  flex-direction: column;
  gap: 16px;
  width: 100%;
}

.popup-form-item{
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 8px;
}

.popup-form-label{
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
  width: 92%;
}

input[type="text"]:focus, input[type="tel"]:focus {
  border-color: #DD1D1D;
}

.popup-form-submit{
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

.popup-form-submit:hover{
  background-color: #C20D0D;
}

.pending{
  pointer-events: none;
}

.popup-error {
    color: #DD1D1D;
}

.popup-success {
  color: #000000;
}

.popup-success-title{
  text-align: center;
  font-family: 'OnestMedium', Inter, sans-serif;
  font-size: 28px;
  /*padding-top: 40px;*/
}

.popup-success-description{
  text-align: center;
  padding: 30px 0;
  width: 80%;
  margin: auto;
}


.popup-acceptance {
  color: #888888;
  font-size: 14px;
  line-height: 1.4;
}

.popup-acceptance a{
  color: #3a3a3a;
  position: relative;
  text-decoration: none;
}

.popup-acceptance a:before {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  right: 50%;
  background: #3a3a3a;
  height: 1px;
  transition: all .4s ease;
}

.popup-acceptance a:hover:before {
  left: 0;
  right: 0;
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

@media screen and (max-width: 990px){
  .popup-title{
    font-size: 36px;
    line-height: 40px;
  }

  .close-btn{
    top: -70px;
    right: -60px;
  }
}

@media screen and (max-width: 640px){
  .popup{
    margin: 0 2rem;
  }

  .popup-title{
    font-size: 26px;
    line-height: 30px;
  }

  .close-btn{
    top: -70px;
    right: -40px;
  }

  .popup-form{
    width: 100%;
    gap: 10px;
  }

  .popup-form-label{
    font-size: 14px;
  }

  .popup-acceptance{
    width: 100%;
    font-size: 12px;
  }
}
</style>