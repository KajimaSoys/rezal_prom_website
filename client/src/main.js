import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/style.css'
import axios from "axios";
import VueGoogleMaps from 'vue-google-maps-community-fork'

const app = createApp(App)

app.use(router, axios)

let backendURL = import.meta.env.VITE_BACKEND_HOST
axios.defaults.baseURL = backendURL

let api_key = import.meta.env.VITE_GOOGLE_API_KEY
app.use(VueGoogleMaps, {
    load: {
        key: api_key,
    },
})

app.mount('#app')

app.provide('backendURL', backendURL)


// axios.defaults.headers.common['Access-Control-Allow-Origin'] = 'http://localhost:5173'; // Set the allowed origin
// axios.defaults.headers.post['Content-Type'] = 'application/json'; // Set the Content-Type header for POST requests
