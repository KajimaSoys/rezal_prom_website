<template>
  <div class="contacts" id="contacts">
    <div class="contacts-max">
      <div class="contacts-content">
        <h2 class="contacts-title" v-html="this.contacts.title"></h2>
        <div class="contacts-info">
          <div class="contacts-info-item">
            <div class="contacts-info-icon">
              <img src="src/assets/icons/icon-location.svg">
            </div>

            <div v-html="this.contacts.address"></div>
          </div>

          <div class="contacts-info-item">
            <div class="contacts-info-icon">
              <img src="src/assets/icons/icon-clock.svg">
            </div>

            <div v-html="this.contacts.schedule"></div>
          </div>

          <div class="contacts-info-item">
            <div class="contacts-info-icon">
              <img src="src/assets/icons/phone.svg" width="16" height="16">
            </div>

            <div v-html="this.contacts.number"></div>
          </div>

          <div class="contacts-info-links">
            <a class="contacts-link" :href="this.contacts.inst_link" target="_blank">Instagram*</a>

            <a class="contacts-link" :href="this.contacts.vk_link" target="_blank">ВКонтакте</a>
          </div>

        </div>
        <div class="contacts-photo">
          <img src="src/assets/images/image-contacts-1.png" width="160" height="160">
          <img src="src/assets/images/image-contacts-2.png" width="160" height="160">
        </div>
      </div>
      <div class="contacts-map">
         <GMapMap :center="center" :zoom="18" style="height: 600px">
           <GMapMarker :key="marker.id" v-for="marker in markers" :position="marker.position" />
         </GMapMap>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Contacts",
  inject: ['backendURL'],
  props: [
    'contacts',
  ],
  data() {
    return {
      center: { lat: 55.767724482181045, lng: 49.1041059787604 },
      markers: [
        {
          id: 'dfsldjl3r',
          position: {
            lat: 55.767724482181045,
            lng: 49.1041059787604,
          },
        },
      ],
    }
  },
}
</script>

<style scoped>
.contacts{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 75px;
  padding-bottom: 150px;
  margin-top: 75px;
}

.contacts-max{
  width: 67rem;
  margin: 0 2rem;
  display: flex;
  flex-direction: row;
}

.contacts-content{
  display: flex;
  flex-direction: column;
  width: 40%;
  flex-basis: 40%;
}

.contacts-title{
  color: #000000;
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 36px;
  line-height: 54px;
  margin-bottom: 80px;
}

.contacts-info{
  display: flex;
  flex-direction: column;
  gap: 16px;
  flex: 1;
}

.contacts-info-item{
  display: flex;
  flex-direction: row;
  gap: 8px;
  color: black;
  line-height: 1.4;
  font-size: 16px;
}

.contacts-info-icon{
  display: flex;
  width: 24px;
  justify-content: center;
  align-items: center;
}

.contacts-info-links{
  display: flex;
  flex-direction: row;
  gap: 16px;
}

.contacts-info-links a{
  color: #DD1D1D;
  text-decoration: none;
  transition: color 0.3s ease-in-out;
}

.contacts-info-links a:hover{
  color: #EB7777;
}

.contacts-photo{
  display: flex;
  flex-direction: row;
  gap: 16px;
}

.contacts-map{
  width: 60%;
  flex-basis: 60%;
  height: 600px;
}

@media screen and (max-width: 990px){
  .contacts{
    padding-bottom: 17rem;
  }

  .contacts-max{
    flex-direction: column;
    gap: 3rem;
  }

  .contacts-map {
    width: 100%;
    flex-basis: 100%;
  }
  
  .contacts-content{
    position: relative;
    width: auto;
  }

  .contacts-title{
    margin-bottom: 2rem;
  }

  .contacts-photo{
    position: absolute;
    bottom: -54rem;
  }
}

@media screen and (max-width: 640px){
  .contacts-title{
    line-height: 38px;
    font-size: 30px;
  }
}
</style>