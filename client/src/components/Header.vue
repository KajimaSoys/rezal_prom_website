<template>
  <div class="header">
    <div class="header-max">

      <a class="logo" href="/">
        <img :src="`${this.backendURL}${this.header.logo}`" alt="РезАль - Мебельная компания. Логотип." width="170" height="60" />
      </a>

      <div class="menu nav-menu" :class="{ open: isBurgerMenuOpen }">
<!--        <div class="menu">-->
<!--          -->
<!--        </div>-->
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

      <div class="messenger nav-menu">
        <a id="whatsapp" href="https://wa.me/79655937000" target="_blank">
          <svg height="20" width="20" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
             viewBox="0 0 418.135 418.135" xml:space="preserve">
            <g>
              <path style="fill:#919191;" d="M198.929,0.242C88.5,5.5,1.356,97.466,1.691,208.02c0.102,33.672,8.231,65.454,22.571,93.536
                L2.245,408.429c-1.191,5.781,4.023,10.843,9.766,9.483l104.723-24.811c26.905,13.402,57.125,21.143,89.108,21.631
                c112.869,1.724,206.982-87.897,210.5-200.724C420.113,93.065,320.295-5.538,198.929,0.242z M323.886,322.197
                c-30.669,30.669-71.446,47.559-114.818,47.559c-25.396,0-49.71-5.698-72.269-16.935l-14.584-7.265l-64.206,15.212l13.515-65.607
                l-7.185-14.07c-11.711-22.935-17.649-47.736-17.649-73.713c0-43.373,16.89-84.149,47.559-114.819
                c30.395-30.395,71.837-47.56,114.822-47.56C252.443,45,293.218,61.89,323.887,92.558c30.669,30.669,47.559,71.445,47.56,114.817
                C371.446,250.361,354.281,291.803,323.886,322.197z"/>
              <path style="fill:#919191FF;" d="M309.712,252.351l-40.169-11.534c-5.281-1.516-10.968-0.018-14.816,3.903l-9.823,10.008
                c-4.142,4.22-10.427,5.576-15.909,3.358c-19.002-7.69-58.974-43.23-69.182-61.007c-2.945-5.128-2.458-11.539,1.158-16.218
                l8.576-11.095c3.36-4.347,4.069-10.185,1.847-15.21l-16.9-38.223c-4.048-9.155-15.747-11.82-23.39-5.356
                c-11.211,9.482-24.513,23.891-26.13,39.854c-2.851,28.144,9.219,63.622,54.862,106.222c52.73,49.215,94.956,55.717,122.449,49.057
                c15.594-3.777,28.056-18.919,35.921-31.317C323.568,266.34,319.334,255.114,309.712,252.351z"/>
            </g>
          </svg>
        </a>

        <a id="telegram" href="https://t.me/Mebel_RezAl_bot" target="_blank">
          <svg width="26" height="26" viewBox="0 0 192 192" xmlns="http://www.w3.org/2000/svg" fill="none"><path stroke="#919191FF" stroke-width="12" d="M23.073 88.132s65.458-26.782 88.16-36.212c8.702-3.772 38.215-15.843 38.215-15.843s13.621-5.28 12.486 7.544c-.379 5.281-3.406 23.764-6.433 43.756-4.54 28.291-9.459 59.221-9.459 59.221s-.756 8.676-7.188 10.185c-6.433 1.509-17.027-5.281-18.919-6.79-1.513-1.132-28.377-18.106-38.214-26.404-2.649-2.263-5.676-6.79.378-12.071 13.621-12.447 29.891-27.913 39.728-37.72 4.54-4.527 9.081-15.089-9.837-2.264-26.864 18.483-53.35 35.835-53.35 35.835s-6.053 3.772-17.404.377c-11.351-3.395-24.594-7.921-24.594-7.921s-9.08-5.659 6.433-11.693Z"/></svg>
        </a>
      </div>



      <div class="call-block nav-menu" @click="this.$emit('popUpCall')">
        <div class="phone-number">
          <img src="/icons/phone.svg" alt="" width="16" height="16" />
          {{ this.header.number }}
        </div>

        <div class="phone-text">
          Заказать звонок
        </div>
      </div>

      <div class="burger-menu" @click="toggleBurgerMenu" :class="{ cross: isBurgerMenuOpen }">
        <span></span>
        <span></span>
        <span></span>
      </div>

      <div :class="isBurgerMenuOpen ? 'overlay' : 'overlay-hidden'" @click="toggleBurgerMenu"></div>

      <div class="burger-menu-items" :class="{ open: isBurgerMenuOpen }">
        <div class="side-menu">
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
        <div class="side-menu-info">
          <div class="side-menu-info-item">
            г. Казань, ул. Мазита Гафури, 48, офис 206
          </div>

          <div class="side-menu-info-item">
            Пн-Вс 9:00-19:00, без выходных
          </div>

          <div class="side-menu-info-item">
            +7 (965) 593-70-00
          </div>

          <div class="side-menu-info-item">
            <a target="_blank" href="https://www.instagram.com/mebel_rezal/">Instagram*</a>  <a target="_blank" href="https://vk.com">ВКонтакте</a>
          </div>
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
  emits: [
    'popUpCall'
  ],
  data(){
    return{
      isBurgerMenuOpen: false
    }
  },
  methods: {
    scrollToElement(elementId) {
      const element = document.getElementById(elementId);

      if (this.$route.path === "/"){
        element.scrollIntoView({ behavior: "smooth" });

        this.isBurgerMenuOpen = false;
        if (this.isBurgerMenuOpen) {
          document.body.style.overflow = "hidden";
        } else {
          document.body.style.overflow = "";
        }
      } else {
        this.$router.push({ path: "/", hash: `#${elementId}` });
      }
    },

    toggleBurgerMenu() {
      this.isBurgerMenuOpen = !this.isBurgerMenuOpen;
      if (this.isBurgerMenuOpen) {
        document.body.style.overflow = "hidden";
      } else {
        document.body.style.overflow = "";
      }
    }
  }
}
</script>

<style scoped>
.header{
  height: 12vh;
  width: 100%;
  display: flex;
  justify-content: center;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1010;
  background-color: white;
  background-color: rgba(255,255,255, 0.8);
  backdrop-filter: blur(4px) brightness(100%);
}

.header-max{
  width: 85rem;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  margin: 0 2rem;
  gap: 10px;
}

.logo{
  width: 15%;
  flex-basis: 15%;
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

.messenger{
  display: flex;
  flex-direction: row;
  gap: 16px;
  align-items: center;
}

#whatsapp svg g path{
  transition: all 0.3s ease-in-out;
}

#whatsapp:hover svg g path {
  fill: #6e6e6e!important;
}

#telegram svg path{
  transition: all 0.3s ease-in-out;
}

#telegram:hover svg path[stroke] {
  stroke: #6e6e6e;
}

.call-block{
  width: 15%;
  flex-basis: 15%;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  cursor: pointer;
  min-width: 17%;
}

.phone-number{
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 14px;
}

.phone-text{
  color: #DD1D1D;
  transition: color 0.2s ease-in-out;
}

.phone-text:hover{
  color: #C20D0D;
}
.burger-menu {
  display: none;
  flex-direction: column;
  justify-content: space-around;
  width: 24px;
  height: 16px;
  cursor: pointer;
  transition: z-index 0.3s ease-in-out;
}

.burger-menu span {
  width: 100%;
  height: 2px;
  background-color: #DD1D1D;
  transition: 0.3s;
}

.burger-menu.cross{
  z-index: 1001;
}

.burger-menu.cross span{
  background-color: white;
}

.burger-menu.cross:hover span{
  background-color: #DD1D1D;
}

.burger-menu.cross span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

.burger-menu.cross span:nth-child(2) {
  opacity: 0;
}

.burger-menu.cross span:nth-child(3) {
  transform: translateY(-3px) rotate(-45deg);
}


.burger-menu-items {
  display: flex;
  position: fixed;
  top: 0;
  right: 0; /* Change from 'left: 0' to 'right: 0' */
  width: 70%;
  max-width: 300px;
  height: 100vh;
  background-color: #2d2d2d;
  flex-direction: column;
  gap: 30%;
  padding: 7rem 24px 24px;
  z-index: 1000;
  overflow-y: auto;
  transform: translateX(100%); /* Add this line */
  transition: transform 0.3s ease; /* Add this line */
}

.burger-menu-items.open {
  transform: translateX(0); /* Add this line */
}

.side-menu{
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.side-menu-info{
  width: 90%;
  gap: 16px;
  display: flex;
  flex-direction: column;
}

.side-menu-info-item{
  color: #6e6e6e;
}

.side-menu-info-item a{
  text-decoration: none;
  color: #6e6e6e;
  transition: color 0.3s ease-in-out;
}

.side-menu-info-item a:hover{
  text-decoration: none;
  color: #b4b4b4;
  transition: color 0.3s ease-in-out;
}

.overlay-hidden{
 display: none;
}

.overlay {
  display: block;
  position: fixed;
  height: 100vh;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5); /* Dark background with transparency */
  z-index: 999; /* Keep the overlay below the menu and header */
}

@media screen and (min-width: 1200px) {
  .logo{
    margin-right: 2rem;
  }
}

@media screen and (max-width: 1200px) {
  .logo img{
    width: 140px;
    height: 40px;
  }

  .menu-item {
    font-size: 16px;
  }

  .phone-number{
    font-size: 14px;
  }
}

@media screen and (max-width: 1100px){
  .menu{
    gap: 15px;
  }
}

/* Hide nav menu and show burger menu on small screens */
@media screen and (max-width: 990px) {
  .nav-menu {
    display: none;
  }

  .burger-menu {
    display: flex;
  }

  .header-max{
    justify-content: space-between;
    margin: 0 4rem;
  }

  .logo{
    min-width: 15%;
  }

  .menu-item{
    color: white;
  }
}

@media screen and (max-width: 640px){
  .header-max{
    margin-right: 2rem;
  }
}

@media screen and (max-width: 360px){

}
</style>