import 'babel-polyfill';

import 'jquery/dist/jquery.min';
import 'popper.js/dist/popper.min';
import 'bootstrap/dist/js/bootstrap.min';

import '@fancyapps/fancybox/dist/jquery.fancybox.min.css';
import '@fancyapps/fancybox';

import Vue from 'vue';

import { BootstrapVue } from 'bootstrap-vue';
import moment from 'moment';
import axios from 'axios';


// Подключаю роутер
import App from './App.vue';
import router from './router';
import store from './store';
// End импорты для роутера

Vue.config.productionTip = false;
Vue.use(BootstrapVue);


moment.locale('ru');

const token = localStorage.getItem('token');
if (token) {
  axios.defaults.headers.common.Authorization = `Token ${token}`;
}

new Vue({
  router,
  render: h => h(App),
  store,
}).$mount('#app');
