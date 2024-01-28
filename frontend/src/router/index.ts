import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import { useStore } from 'vuex';

const store = useStore();

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
    path: '/delete-card',
    name: 'delete-card',
    component: () => import('../views/DeleteCardView.vue'),
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
  return !store;
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
