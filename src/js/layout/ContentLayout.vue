<template>
  <div class="fix-header card-no-border fix-sidebar">
    <div id="main-wrapper">
<!--      <Header />-->
      <div
        class="page-wrapper"
        style="min-height: 324px;"
      >
        <router-view />
<!--        <Footer />-->
      </div>
    </div>
  </div>
</template>

<script>
// import Header from '@/components/Header';
// import Footer from '@/components/Footer';

export default {
  name: 'ContentLayout',
  components: {
    // Header,
    // Footer,
  },
};
</script>
