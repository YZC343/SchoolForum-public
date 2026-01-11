import { createRouter, createWebHistory } from 'vue-router'
import Forum from '@/views/Forum.vue'
import Login from '@/views/Login.vue'
import Sign_up from '@/views/Sign_up.vue'
import Home from '@/views/Home.vue'
import Board from '@/views/Board.vue'
import publishPost from '@/views/publishPost.vue'
import Post from '@/views/Post.vue'
import User from '@/views/User.vue'
import Message from '@/views/Message.vue'
import modifyPost from '@/views/modifyPost.vue'
import modifyReply from '@/views/modifyReply.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/Login' 
    },

    {
      path:'/Forum',
      component:Forum
    },
    {
      path:'/Login',
      component:Login
    },
    
    {
      path:'/Sign_up',
      component:Sign_up
    },
    {
      path:'/Home',
      component:Home
    },
    {
      path:'/Board',
      component:Board
    },
    {
      path:"/PublishPost",
      component:publishPost
    },
    {
      path:"/ModifyPost",
      component:modifyPost
    },
    {
      path:"/Post",
      component:Post
    },
    {
      path:"/ModifyReply",
      component:modifyReply
    },
    {
      path:"/User",
      component:User
    },
    {
      path:"/Message",
      component:Message

    }
  ],
  
})

export default router
