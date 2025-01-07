import {createRouter, createWebHistory} from 'vue-router'
import Home from './pages/Home.vue'
import Login from './pages/Login.vue'
import Register from "./pages/Register.vue";
import UserManagement from './admin/UserManagement.vue';
import ProductManagement from './admin/ProductManagement.vue';

const routes = [
    {
        path: '/',
        name: 'home',
        component: Home
    },
    {
        path: '/login',
        name: 'login',
        component: Login
    },
    {
        path: '/register',
        name: 'register',
        component: Register
    },
    {
        path: '/admin/UserManagement',
        name: 'Usermanagement',
        component: UserManagement
    },
    {
        path: '/admin/ProductManagement',
        name: 'Productmanagement',
        component: ProductManagement
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
