import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import store from '@/store';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'main',
    component: () => import('../views/MainView.vue'),
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/LoginView.vue'),
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('../views/RegisterView.vue'),
  },
  {
    path: '/add-card',
    name: 'add-card',
    component: () => import('../views/AddCardView.vue'),
  },
  {
    path: '/edit-card',
    name: 'edit-card',
    component: () => import('../views/EditCardView.vue'),
  },
  {
    path: '/settings',
    name: 'settings',
    component: () => import('../views/SettingsView.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

function isAuthenticated() {
  if (store === undefined) {
    return false;
  }
  return store.getters['user/user'] !== null;
}

router.beforeEach(async (to, from, next) => {
  if (to.name === 'login' || to.name === 'register') {
    next();
  } else if (!isAuthenticated()) {
    next({ name: 'login' });
  } else {
    next();
  }
  return false;
});

export default router;
