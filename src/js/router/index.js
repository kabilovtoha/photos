import Vue from 'vue';
import VueRouter from 'vue-router';

// import store from '@/store';

Vue.use(VueRouter);

const routes = [
  {
    path: '/photo/',
    name: 'photo-page',
    component: () => import('../views/photo/PhotoPage.vue'),
    meta: {
      noAuth: true,
      template: 'content-layout',
    },
  },
  {
    path: '/photo/city/:city_id/',
    name: 'photo-by-city',
    component: () => import('../views/photo/PhotoPage.vue'),
    meta: {
      noAuth: true,
      template: 'content-layout',
    },
  },
];

const router = new VueRouter({
  mode: 'history',
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.noAuth)) {
    // if (store.getters['auth/isLoggedIn']) {
    //   next('/index/');
    //   return;
    // }
    // next();
    // return;
  }
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // if (store.getters['auth/isLoggedIn']) {
    //   next();
    //   return;
    // }
    // next('/');
    // return;
  }
  next();
});

export default router;
