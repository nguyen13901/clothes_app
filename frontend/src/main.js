import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

axios.defaults.baseURL = 'https://55cd-190-2-130-168.eu.ngrok.io/'
axios.defaults.headers.get['Access-Control-Allow-Origin'] = '*';
axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
axios.defaults.headers['Access-Control-Allow-Origin'] = '*';

createApp(App).use(store).use(router, axios).mount('#app')
