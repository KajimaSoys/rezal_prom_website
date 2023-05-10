<template>
  <div class="about" id="about">
    <div class="about-max">
      <div class="about-head">
        <div class="about-image-container">
          <img src="/image/image-about-1.png" class="about-image-1">
        </div>
        <div class="about-image-container">
          <img src="/image/image-about-2.png" class="about-image-2">
        </div>
        <div class="about-description">
          <div v-html="this.about.description"></div>
        </div>
        <div class="about-image-container">
          <img src="/image/image-about-3.png" class="about-image-3">
        </div>
      </div>

      <div class="about-content">
        <div class="about-content-row">
          <div class="about-thick">
            <div class="about-card-title">
              <h3>
                <div v-html="this.about.title_first"></div>
              </h3>
            </div>
            <div class="about-card-description">
              <div v-html="this.about.description_first"></div>
            </div>
          </div>
          <div class="about-thin">
            <div class="about-card-title">
              <h3>
                <div v-html="this.about.title_second"></div>
              </h3>
            </div>
            <div class="about-card-description">
              <div v-html="this.about.description_second"></div>
            </div>
          </div>
        </div>

        <div class="about-content-row">
          <div class="about-thin">
            <div class="about-card-title">
              <h3>
                <div v-html="this.about.title_third"></div>
              </h3>
            </div>
            <div class="about-card-description">
              <div v-html="this.about.description_third"></div>
            </div>
          </div>
          <div class="about-thick">
            <div class="about-card-title">
              <h3>
                <div v-html="this.about.title_fourth"></div>
              </h3>
            </div>
            <div class="about-card-description">
              <div v-html="this.about.description_fourth"></div>
            </div>
          </div>
        </div>

        <div class="about-content-row">
          <div class="about-thick">
            <div class="about-card-title">
              <h3>
                <div v-html="this.about.title_fifth"></div>
              </h3>
            </div>
            <div class="about-card-description">
              <div v-html="this.about.description_fifth"></div>
            </div>
          </div>
          <div class="about-thin">
            <div class="about-card-title">
              <h3>
                <div v-html="this.about.title_sixth"></div>
              </h3>
            </div>
            <div class="about-card-description">
              <div v-html="this.about.description_sixth"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "About",
  inject: ['backendURL'],
  props: [
    'about',
  ],
}
</script>

<style scoped>
.about{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 150px;
  padding-bottom: 75px;
}

.about-max{
  max-width: 67rem;
  /*height: 90%;*/
  /*border-radius: 30px;*/
  display: flex;
  flex-direction: column;
  gap: 5rem;
  margin: 0 2rem;
}

.about-head{
  display: flex;
  flex-direction: row;
  gap: 16px;
  align-items: center;
}

.about-image-container{
  border-radius: 15px;
  height: 160px;
  width: 160px;
}

.about-image-1, .about-image-2, .about-image-3 {
  max-width: 100%;
  height: 100%;
  object-fit: cover;
}

.about-description{
  flex: 1;
  font-size: 16px;
  line-height: 25.2px;
  margin: 0 5%;
  color: #000000;
}

.about-content{
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.about-content-row{
  display: flex;
  flex-direction: row;
  gap: 16px;
}

.about-thick{
  width: 60%;
  flex-basis: 60%;
  height: 200px;
  border: 1px solid #BDBDBD;
  border-radius: 30px;
  padding: 25px 35px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.about-thin{
  width: 40%;
  flex-basis: 40%;
  height: 200px;
  border: 1px solid #BDBDBD;
  border-radius: 30px;
  padding: 25px 35px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.about-card-title{
  color: #222222;
  font-family: 'OnestMedium', Inter, sans-serif;
  font-style: normal;
  font-weight: 500;
  font-size: 22px;
  line-height: 36px;
}

/*.about-card-title > h3{*/
/*  margin-block-start: 0;*/
/*  margin-block-end: 0;*/
/*}*/

.about-card-description{
 color: #686868;
}

@media screen and (max-width: 990px) {
  .about-max{
    gap: 13rem;
  }
  
  .about-head{
    flex-direction: row;
    align-items: center;
    position: relative;
  }

  .about-description{
    position: absolute;
    top: 190px;
    margin: 0;
    width: 75%;
  }

  .about-content-row {
    flex-direction: column;
    align-items: center;
  }

  .about-thick,
  .about-thin {
    width: auto;
    flex-basis: 100%;
  }

  .about-image-container {
    height: 150px;
    width: 150px;
  }

  .about-head > div:nth-child(2){
    flex: 1;
  }
}

@media screen and (max-width: 640px){
  .about-max{
    gap: 17rem;
  }
  .about-description{
    top: 130px;
    width: 100%;
  }

  .about-image-container {
    height: 80px;
    width: 80px;
  }
}

@media screen and (max-width: 360px){

}
</style>