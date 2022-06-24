import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";

// axios.defaults.baseURL = 'http://localhost:8000/'
axios.defaults.baseURL = 'https://d146-190-2-130-168.eu.ngrok.io'
createApp(App).use(store).use(router, axios).mount("#app");
