<template>
  <div class="services">
    <div class="services-max">
      <div class="services-title">
        <h2>
          <div v-html="this.services.title"></div>
        </h2>
      </div>
      <div class="services-items">
        <div class="services-item">
          <div class="services-item-icon">
            <img
                src="/icons/icon-cabinet.svg"
                alt=""
                width="36"
                height="36"
                loading="lazy"
            >
          </div>
          <div class="services-item-title">
            <h3>
              <div v-html="this.services.title_first"></div>
            </h3>
          </div>
        </div>

        <div class="services-item">
          <div class="services-item-icon">
            <img
                src="/icons/icon-measure.svg"
                alt=""
                width="36"
                height="36"
                loading="lazy"
            >
          </div>
          <div class="services-item-title">
            <h3>
              <div v-html="this.services.title_second"></div>
            </h3>
          </div>
        </div>

        <div class="services-item">
          <div class="services-item-icon">
            <img
                src="/icons/icon-pencil.svg"
                alt=""
                width="36"
                height="36"
                loading="lazy"
            >
          </div>
          <div class="services-item-title">
            <h3>
              <div v-html="this.services.title_third"></div>
            </h3>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Services",
  inject: ['backendURL'],
  props: [
    'services',
  ],
}
</script>

<style scoped>
.services{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 75px;
}

.services-max{
  max-width: 67rem;
  margin: 0 2rem;
}

.services-title{
  color: #000000;
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 36px;
  line-height: 54px;
  margin-bottom: 80px;
}

.services-items{
 display: flex;
  flex-direction: row;
  gap: 16px;
}

.services-item{
  flex: 1;
  height: 200px;
  border: 1px solid #BDBDBD;
  border-radius: 30px;
  padding: 25px 35px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.services-item-icon{
  width: 67px;
  height: 54px;
  background: #DD1D1D;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.services-item-title{
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 22px;
  line-height: 31px;
  color: #222222;
  width: 80%;
}

@media screen and (max-width: 990px){
  .services-items{
    flex-direction: column;
  }

  .services-item{
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    gap: 2rem;
  }

}

@media screen and (max-width: 640px){
  .services{
    max-width: 100%;
    margin: 0 2rem;
    width: auto;
  }

  .services-max{
    max-width: 100%;
    margin: 0;
  }

  .services-title{
    line-height: 38px;
    font-size: 30px;
  }
}
</style>