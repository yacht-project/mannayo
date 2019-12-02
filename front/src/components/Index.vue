<template>
  <div class="container">
    <div class="tile is-ancestor">
      <div class="tile is-vertical is-8">
        <div class="tile">
          <div class="tile is-parent is-vertical">
            <article class="tile is-child notification is-primary has-text-centered">
              <when-form />
            </article>
            <article class="tile is-child notification is-success has-text-centered">
              <who-form />
            </article>
            <article class="tile is-child notification is-info has-text-centered">
              <why-form />
            </article>
            <article class="tile is-child notification is-warning has-text-centered">
              <where-form />
            </article>
          </div>
        </div>
      </div>
    </div>
    <a class="button is-success float">만나자!</a>
  </div>
</template>

<script lang='ts'>
import Vue from 'vue';
import WhenForm from './WhenForm.vue';
import WhyForm from './WhyForm.vue';
import WhoForm from './WhoForm.vue';
import WhereForm from './WhereForm.vue';

export default Vue.extend({
  name: 'Index',
  components: {
    'when-form': WhenForm,
    'why-form': WhyForm,
    'who-form': WhoForm,
    'where-form': WhereForm,
  },
  data() {
    return {
      title: '',
      place: '',
      holidayIncluded: false,
      selectedValue: null,
    };
  },
  methods: {
    sendPost() {
      this.axios.get('http://localhost:8081').then((response: any) => response);
    },
  },
});
</script>

<style scoped>
.float{
  position:fixed;
  width:60px;
  height:60px;
  bottom:40px;
  right:40px;
  background-color:#0C9;
  color:#FFF;
  border-radius:50px;
  text-align:center;
  box-shadow: 2px 2px 3px #999;
}
</style>
