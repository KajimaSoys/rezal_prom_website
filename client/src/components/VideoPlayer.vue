<template>
  <div v-if="visible" class="video-player" @click="hideVideo">
    <div class="video-container" @click.stop>
      <button class="close-button" @click="hideVideo" ref="closeButton">×</button>
      <iframe
        :src="videoSrc"
        frameborder="0"
        allowfullscreen
      ></iframe>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    visible: Boolean,
    videoId: String,
  },
  computed: {
    videoSrc() {
      return `https://www.youtube.com/embed/${this.videoId}`;
    },
  },
  methods: {
    hideVideo(event) {
      if (event.target === this.$el || event.target === this.$refs.closeButton) {
        this.$emit('close');
      }
    },
  },
};
</script>

<style scoped>
.video-player {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1011;
}

.video-container {
  position: relative;
  width: 80%;
  height: 80%;
}

iframe {
  width: 100%;
  height: 100%;
}

.close-button {
  position: absolute;
  top: -50px;
  right: -95px;
  background: transparent;
  border: none;
  color: rgba(255, 255, 255, 0.7);
  font-size: 3rem;
  cursor: pointer;
  padding: 5px 10px;
  transition: color 0.2s ease-in-out;
}

.close-button:hover {
  color: rgba(255, 255, 255, 1);
}

@media screen and (max-width: 990px) {
  .close-button{
    top: -70px;
    right: -60px;
  }
}

@media screen and (max-width: 640px) {
  .close-button{
    top: -70px;
    right: -40px;
  }
}
</style>