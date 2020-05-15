<template>
  <div>
    <div
      v-if="existsCities.length > 1"
      class="mb-5"
    >
      <h2>Выберите город</h2>
      <div
        v-if="city_id"
        class="row"
      >
        <router-link
          v-for="city in existsCities"
          :key="`city_${city.id}`"
          :to="`/photo/city/${city.id}/`"
          class="ml-3"
          @click.prevent="checkRout(`/photo/city/${city.id}/`)"
        >
          {{ city.name }}
        </router-link>
        <router-view></router-view>
      </div>
      <div
        v-else
        class="row"
      >
        <a
          v-for="city in existsCities"
          :key="`city_${city.id}`"
          :href="`/photo/city/${city.id}/`"
          class="ml-3"
          @click.prevent="checkRout({ path: `/photo/city/${city.id}/`, cityId: city.id })"
        >
          {{ city.name }}
        </a>
      </div>
    </div>
    <div
      v-if="activeCity.id"
      class="row mb-4"
    >
      <h2>Фотографии города "{{ activeCity.name }}"</h2>
    </div>
    <div class="row">
      <div
        v-for="photo in photoList"
        :key="photo.id"
        class="col-sm-12 col-md-6 col-lg-3 photo-bl"
      >
        <div class="photo-bl-inner">
          <div class="img-bl">
            <a
              :href="photo.image"
              class="fancybox"
              data-fancybox="images"
            >
                <img
                  :src="photo.image_thumbnail"
                  alt=""
                >
            </a>
          </div>
          <div class="photo-info mt-2 mb-1">
            <div class="inf-item">
              <em>Город:</em> <span>{{ photo.city.name }}</span>
            </div>
            <div class="inf-item">
              <em>Автор:</em> <span>{{ photo.username }}</span>
            </div>
            <div class="inf-item">
              <em>Дата:</em>
              <span>{{ moment(photo.created).format('MMMM Do YYYY, h:mm a') }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import moment from 'moment';
import { mapState, mapMutations, mapActions } from 'vuex';

export default {
  name: 'PhotoPage',
  data() {
    return {
      city_id: this.$route.params.city_id,
      photos_count: 5,
    };
  },
  beforeRouteEnter(to, from, next) {
    // if (to.params.city_id && from.path === '/photo/') {
    // }
    next();
  },
  beforeRouteUpdate(to, from, next) {
    let cityId = null;
    try {
      cityId = parseInt(to.params.city_id, 10);
    } catch (e) {
      cityId = null;
    }
    if (cityId) {
      this.city_id = cityId;
      next();
    }
  },
  computed: {
    ...mapState('photoPage', [
      'photoList', 'existsCities', 'activeCity', 'photoPagination',
    ]),
  },
  watch: {
    photoList() {
    },
    city_id() {
      this.getPhotoList({ page: this.photoPagination.currentPage, city: this.city_id });
      const activeCity = this.existsCities.find((city) => {
        if (city.id === this.city_id) {
          return city;
        }
        return false;
      });
      if (activeCity) {
        this.setActiveCity(activeCity);
      }
    },
  },
  mounted() {
    if (this.city_id) {
      this.getPhotoList({ page: this.photoPagination.currentPage, city: this.city_id });
    } else {
      this.getPhotoList({ page: this.photoPagination.currentPage });
    }
    this.getPhotoParams();
  },
  methods: {
    ...mapActions('photoPage', [
      'getPhotoList', 'getPhotoParams',
    ]),
    ...mapMutations('photoPage', ['setActiveCity',
    ]),
    checkRout(data) {
      const { path, cityId } = data;
      this.city_id = cityId;
      this.$router.push(path);
    },
    moment,
  },
};
</script>

<style scoped>
  .photo-bl {
    padding: 8px;
  }
  .photo-bl-inner {
    padding: 6px;
    border: 1px solid #b5b5b5;
  }
  .img-bl {
    width: 100%;
    overflow: hidden;
  }
  .img-bl img {
    width: 100%;
  }
  .photo-info {
    width: 100%;
  }
</style>
