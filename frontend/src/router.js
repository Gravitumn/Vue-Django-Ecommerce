import {createRouter, createWebHistory} from 'vue-router'
import Home from './pages/Home.vue'
import Login from './pages/Login.vue'
import Register from "./pages/Register.vue";
import UserManagement from './admin/UserManagement.vue';
import AdminProductManagement from './admin/AdminProductManagement.vue';
import ProductManagement from './pages/ProductManagement.vue';

function isAdmin() {
    const parsedAuthState = JSON.parse(localStorage.getItem('authState'));
    const user = parsedAuthState.user;
    return user && user.role === 'admin';
}

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
        component: UserManagement,
        meta: { requiresAdmin: true }
    },
    {
        path: '/admin/ProductManagement',
        name: 'AdminProductmanagement',
        component: AdminProductManagement,
        meta: {requiresAdmin:true}
    },
    {
        path: '/ProductManagement',
        name: 'Productmanagement',
        component: ProductManagement
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAdmin)) {
        if(!isAdmin()){
            alert('Access denied: Admins only');
            next({ name: 'home' });
        }
        else{
            next();
        }
        
    }else{
        next()
    }
});

export default router
