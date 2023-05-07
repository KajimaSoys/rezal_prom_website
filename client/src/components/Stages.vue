<template>
  <div class="stages">
    <div class="stages-max">
      <h2>
        <div class="stages-title" v-html="this.stages.title"></div>
      </h2>
      <div class="stages-grid">
        <div v-for="(stage, index) in this.stagesArr" :key="index" class="stage">
          <div class="stage-image">
            <div class="stage-count">{{ index + 1 }}</div>
            <img
              :src="`${this.backendURL}${stage.image}`"
              alt="stage image"
            >
          </div>

          <div class="stage-title" v-html="stage.title"></div>
        </div>
      </div>
      <div class="stages-delivery">
        <h2 class="stages-delivery-title" v-html="this.stages.delivery_title"></h2>
        <div class="stages-delivery-first" v-html="this.stages.delivery_first"></div>
        <div class="stages-delivery-second" v-html="this.stages.delivery_second"></div>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: "Stages",
  inject: ['backendURL'],
  props: [
    'stages',
    'stagesArr',
  ],
}
</script>

<style scoped>
.stages{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 150px;
  padding-bottom: 150px;
}

.stages-max{
  width: 67rem;
}

.stages-title{
  color: #000000;
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 36px;
  line-height: 54px;
  margin-bottom: 80px;
}

.stages-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 60px 16px;
  margin-bottom: 150px;
}

.stage {
  display: flex;
  flex-direction: column;
  gap: 30px;
  align-items: flex-start;
}

.stage-image{
  position: relative;
}

.stage-count {
  position: absolute;
  bottom: 0;
  left: 0;
  margin: 15px;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background-color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 16px;
  color: #000000;
  line-height: 0px;
}


.stage-image img {
  width: 100%;
  height: auto;
  display: block;
  /*margin-bottom: 20px;*/
}

.stage-title {
  color: #000000;
  font-size: 15px;
  line-height: 1.4;
  width: 90%;
}

.stages-delivery{
  display: flex;
  flex-direction: row;
  gap: 100px;
}

.stages-delivery-title{
  color: #000000;
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 36px;
  line-height: 54px;
  width: 16%;
  flex-basis: 16%;
}

.stages-delivery-first{
  flex: 1;
  color: #000000;
  line-height: 1.4;
  font-size: 16px;
}

.stages-delivery-second{
  flex: 1;
  color: #000000;
  line-height: 1.4;
  font-size: 16px;
}
</style>