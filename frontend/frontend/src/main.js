import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import axios from 'axios'


const app = createApp(App)
app.use(ElementPlus)
app.use(router)
app.config.globalProperties.$http = axios
// 配置axios默认选项，设置withCredentials为true，这样每个请求都会携带cookie
axios.defaults.withCredentials = true
// 可以根据需要设置baseURL
axios.defaults.baseURL = 'http://localhost:5000'  // 假设后端运行在5000端口
app.mount('#app')
