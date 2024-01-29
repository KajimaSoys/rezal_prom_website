<template>
  <div class="questions">
    <div class="questions-max">
      <h1 class="questions-title" v-html="questions.title"></h1>

      <div v-for="(question, index) in questionsArr" :key="question.order" class="questions-tile"
           @click="toggleQuestion(index)">
        <div class="questions-header">
          <div class="questions-text" v-html="question.question"></div>
          <img
              src="/icons/icon-plus.svg"
              class="toggle-icon"
              :style="question.isOpen ? 'transform: rotate(45deg);' : ''"
              loading="lazy"
          >
        </div>
        <div :class="question.isOpen ? 'questions-answer-opened' : 'questions-answer-closed'" class="questions-answer"
             v-html="question.answer"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Questions",
  inject: ['backendURL'],
  props: [
    'questions',
    'questionsArr',
  ],
  methods: {
    toggleQuestion(index) {
      this.questionsArr[index].isOpen = !this.questionsArr[index].isOpen;
    },
  },
}
</script>

<style scoped>
.questions {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 150px;
}

.questions-max {
  width: 67rem;
  margin: 0 2rem;
}

.questions-title {
  color: #000000;
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 36px;
  line-height: 54px;
  margin-bottom: 80px;
}

.questions-tile {
  border: 1px solid #BDBDBD;
  border-radius: 20px;
  margin-bottom: 30px;
  padding: 25px 35px;
  transition: height 0.2s ease-in-out;
  cursor: pointer;
}

.questions-header {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
}

.questions-text {
  font-family: OnestMedium, Inter, sans-serif;
  font-weight: 500;
  font-size: 22px;
  line-height: 31px;
}

.toggle-icon {
  /*width: 35px;*/
  /*height: 35px;*/
  padding: 8px;
  border-radius: 50%;
  border: 1px solid #BDBDBD !important;
  background-color: white;
  color: #DD1D1D;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 0.1s ease-in-out;
}

img.toggle-icon {
  height: 16px;
  width: 16px;
  fill: white;
}

.questions-answer {
  line-height: 1.4;
  font-size: 15px;
  color: #000000;
  transition: all 0.2s ease-in-out;
}

.questions-answer-closed {
  padding-top: 0;
  height: 0;
  opacity: 0;
}

.questions-answer-opened {
  padding-top: 20px;
  height: auto;
  opacity: 1;
}

@media screen and (max-width: 640px) {
  .questions-title {
    line-height: 38px;
    font-size: 30px;
  }
}

@media screen and (max-width: 360px) {

}
</style>