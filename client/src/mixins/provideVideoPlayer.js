export default {
  data() {
    return {
      videoVisible: false,
      videoId: '',
    };
  },
  methods: {
    showVideo(videoId) {
      this.videoId = videoId;
      this.videoVisible = true;
    },
    hideVideo() {
      this.videoVisible = false;
    },
  },
  provide() {
    return {
      showVideo: this.showVideo,
      hideVideo: this.hideVideo,
    };
  },
};