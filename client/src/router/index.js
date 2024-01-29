import {createRouter, createWebHistory} from 'vue-router'
import MainView from "../views/MainView.vue";
import PolicyView from "../views/PolicyView.vue";
import NotFoundView from "../views/NotFoundView.vue";

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
        {
            path: '/:catchAll(.*)',
            name: 'not-found',
            beforeEnter: (to, from, next) => {
                to.fullPath = decodeURIComponent(to.fullPath);
                next();
            },
            component: NotFoundView,
        },
    ]
})

export default router
