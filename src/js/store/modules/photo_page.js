/* eslint-disable no-shadow,no-param-reassign */
import axios from 'axios';


const state = {
  photoList: [],
  photoPagination: {
    currentPage: 1,
  },
  existsCities: [],
  activeCity: {},
};

const getters = {
};

const mutations = {
  setPhotoList(state, newPhotoList) {
    state.photoList = [...newPhotoList];
  },
  setPhotoPagination(state, value) {
    state.photoPagination = value;
  },
  setExistsCities(state, value) {
    state.existsCities = value;
  },
  setActiveCity(state, value) {
    state.activeCity = value;
  },
};

const actions = {
  async getPhotoList({ commit }, data) {
    await axios.get('/api/v1/photo/', { params: data })
      .then((response) => {
        const {
          results,
          next,
          previous,
          pages,
          // eslint-disable-next-line camelcase
          page_size,
          // eslint-disable-next-line camelcase
          current_page,
        } = response.data;
        const photoPagination = {
          nextPage: next,
          previousPage: previous,
          pages,
          currentPage: current_page,
          pageSize: page_size,
        };
        commit('setPhotoList', results);
        commit('setPhotoPagination', photoPagination);
      });
  },
  async getPhotoParams({ commit }, data) {
    await axios.get('/photos-filterparams/', { params: data })
      .then((response) => {
        const {
          cities,
        } = response.data;
        if (cities.length === 1) {
          commit('setActiveCity', cities[0]);
        }
        commit('setExistsCities', cities);
      });
  },
};


export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
