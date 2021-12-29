import Vue from 'vue'
import App from '@/App.vue'
import Vuetify from 'vuetify'
import "vuetify/dist/vuetify.min.css";

import router from '@/router'

Vue.config.productionTip = false

Vue.use(Vuetify)
const vuetifyOptions = { }
const vue = new Vue({
  vuetify: new Vuetify(vuetifyOptions),
  router,
  render: h => h(App)
})


vue.$mount('#app')
