import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import './assets/style.css'
import axios from "axios";
import VueGoogleMaps from 'vue-google-maps-community-fork'

import ElementPlus from "element-plus";
import 'element-plus/dist/index.css'

// import VueYandexMetrika from 'vue3-yandex-metrika'

// import { TheMask } from 'vue-the-mask';

const app = createApp(App)

app.use(router, axios)

app.use(ElementPlus)

// app.use(VueYandexMetrika, {
//     id: 93839626,
//     router: router,
//     env: process.env.NODE_ENV
//   })

let backendURL = import.meta.env.VITE_BACKEND_HOST;
let frontendURL = import.meta.env.VITE_FRONTEND_HOST;

axios.defaults.baseURL = backendURL

let api_key = import.meta.env.VITE_GOOGLE_API_KEY;
app.use(VueGoogleMaps, {
    load: {
        key: api_key,
    },
})

router.isReady().then(() => {
    app.mount('#app')

    window.ym = window.ym || function () {
        (window.ym.a = window.ym.a || []).push(arguments)
    }
    window.ym.l = 1 * new Date()
    ym(93839626, 'init', {
        clickmap: true,
        trackLinks: true,
        accurateTrackBounce: true,
        // webvisor: true,
    })

    let script = document.createElement('script')
    script.type = 'text/javascript'
    script.async = true
    script.src = 'https://mc.yandex.ru/metrika/tag.js'
    let firstScript = document.getElementsByTagName('script')[0]
    firstScript.parentNode.insertBefore(script, firstScript)
})

app.provide('backendURL', backendURL)
app.provide('frontendURL', frontendURL)

app.config.globalProperties.$projectVersion = '1.6'
// axios.defaults.headers.common['Access-Control-Allow-Origin'] = 'http://localhost:5173'; // Set the allowed origin
// axios.defaults.headers.post['Content-Type'] = 'application/json'; // Set the Content-Type header for POST requests
