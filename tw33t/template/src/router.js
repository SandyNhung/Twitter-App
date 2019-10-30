import Vue from 'vue'
import Router from 'vue-router'
import tweetPage from './views/tweetPage.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'tweet-page',
      component: tweetPage
    }
  ]
})
