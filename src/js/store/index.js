import Vue from 'vue';
import Vuex from 'vuex';

import photoPage from './modules/photo_page';


Vue.use(Vuex);


export default new Vuex.Store({
  modules: {
    photoPage,
  },
});
