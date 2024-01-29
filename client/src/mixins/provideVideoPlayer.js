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
            document.body.style.overflow = "hidden";
        },
        hideVideo() {
            this.videoVisible = false;
            document.body.style.overflow = "";
        },
    },
    provide() {
        return {
            showVideo: this.showVideo,
            hideVideo: this.hideVideo,
        };
    },
};