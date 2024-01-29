import {createRouter, createWebHistory} from 'vue-router'
import MainView from "../views/MainView.vue";
import PolicyView from "../views/PolicyView.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'main',
            component: MainView
        },
        {
            path: '/policy',
            name: 'policy',
            component: PolicyView
        },
    ]
})

export default router
