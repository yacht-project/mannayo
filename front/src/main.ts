import Vue from 'vue';
import VCalendar from 'v-calendar';
import axios from 'axios';
import VueAxios from 'vue-axios';
import Buefy from 'buefy';

import App from './App.vue';

import 'buefy/dist/buefy.css';

Vue.use(Buefy);
Vue.use(VCalendar, {
  componentPrefix: 'vc',
});
Vue.use(VueAxios, axios);

Vue.config.productionTip = false;

new Vue({
  render: (h) => h(App),
}).$mount('#app');
