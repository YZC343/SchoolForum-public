<script setup lang="ts">
import { ElAside, ElButton, ElContainer, ElHeader, ElMain, ElMenu } from 'element-plus';

</script>
    
<template>
    
    <ElMenu
    mode="horizontal"
    background-color="#545c64"
    text-color="#fff"
    active-text-color="#ffd04b"
    :default-active="$route.path"
    router
    style="display: flex;
    align-items: center;
    justify-content: space-between;
    position: sticky;
    top:0;
    "
    >   
        <div style="display: flex;">
            <el-menu-item  index="/home">首页</el-menu-item>

            <el-sub-menu>
                <template #title>
                    <el-icon><location /></el-icon>
                    <span>排序</span>
                </template>

                <el-menu-item >最新</el-menu-item>
                <el-menu-item >本周最热</el-menu-item>
                <el-menu-item >默认</el-menu-item>
            </el-sub-menu>
            <el-menu-item-group>

            </el-menu-item-group>
        </div>
        

        
            <div style="display: flex;">
                <ElInput style="height: 60%;width: 100%;" type="UserName"  autocomplete="off" placeholder="" v-model="keyword"></ElInput>

                <ElButton style="height: 60%;" type="primary" @click="click_search">搜索</ElButton>
            </div>
            
            <div style="display: flex;">
                <el-menu-item index="/home">私信</el-menu-item>

                <el-menu-item index="/User">用户</el-menu-item>
            </div>
        
            
        
    </ElMenu>   
    <ElContainer style="width: 50%;margin-left: 25%;margin-right: 25%;display: flex;flex-direction: column;">
        
        <ElContainer style="" v-for="item in posts" class="scrollbar-demo-item"
        @click = "clickPost(item)"
        >
            <ElHeader style="height: 20px;font-weight: bold;font-size: 1em;overflow: hidden;white-space: nowrap;">
                标题:{{ item.title }}
            </ElHeader>
            <ElMain
                style="
                margin: 10px;
                border-radius: 4px;
                border: solid 2px #B0C4DE;"
                >{{ item.content }}
            </ElMain>
            <ElAside>
                <div 
                    style="display: flex;"
                    
                >
                    <ElContainer style="margin-left: 15px;">作者:{{ item.author_username }}</ElContainer>
                    <ElContainer style="margin-left: 15px;">{{ item.created_time }}</ElContainer>
                </div>
            </ElAside>
        </ElContainer>
        

    </ElContainer>
        
    <div style="height: 70px;background-color: white;"></div>

    <div style="
    position: fixed;
    position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 5%;
        background-color: #6495ED;
        /*color: #fff;*/
        text-align: center;
        padding: 10px 0;
        display: flex;
        justify-content: center;
        width: 50%;
        margin-left: 25%;
        margin-right: 25%;
        border-radius: 4px;
        box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5);
    "


        @click="onClick_publish_post"
    >
    <!-- 底栏内容 -->
    <p >发布帖子</p>
    </div>
    
</template>

<script  lang="ts">
    import router from '@/router';
    import axios from 'axios';
    import { ref } from 'vue';

    export default{

        methods:{
            onClick_publish_post(){
                router.push({
                    path:'/PublishPost',
                    query:{board:this.$route.query.name},
                })
            },
            clickPost(item){
                router.push({
                    path:"/Post",
                    query:{uuid:item.uuid,board:item.board_name},
                })
                console.log(item.name)
            },
            getPostList(){
                axios.post('/api/posts/query',{board:this.$route.query.name,keyword:this.$route.query.keyword})
                    .then(response => {
                        console.log(response);
                        this.posts=response.data
                })
                .catch(error => console.error(error));
            },
            click_search(){
                axios.post('/api/posts/query',{keyword:this.keyword})
                    .then(response => {
                        console.log(response);
                        this.posts=response.data
                })
            }
        },

        data() {
            return{
                posts:ref([]),
                keyword:""
                /*
                {
                        name:"帖子标题",
                        content:"帖子内容XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                        time:"2025-12-3",
                        author:"Lee",
                    },
                    {
                        name:"帖子标题",
                        content:"帖子内容XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                        time:"2025-12-3",
                        author:"Lee",
                    },
                    {
                        name:"帖子标题",
                        content:"帖子内容XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                        time:"2025-12-3",
                        author:"Lee",
                    },
                    {
                        name:"帖子标题",
                        content:"帖子内容XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                        time:"2025-12-3",
                        author:"Lee",
                    },
                    {
                        name:"帖子标题",
                        content:"帖子内容XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                        time:"2025-12-3",
                        author:"Lee",
                    },
                    {
                        name:"帖子标题",
                        content:"帖子内容XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                        time:"2025-12-3",
                        author:"Lee",
                    },
                 */
            }
        },
        mounted(){
            this.getPostList()
        },
    }
</script>

<style >
    navbar {
        background-color: #333;
        color: #fff;
        padding: 10px;
    }
    navbar ul {
        list-style-type: none;
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: space-around;
    }
    navbar ul li {
        cursor: pointer;
        }
        router-link-active {
        color: #f00;
    }
    .scrollbar-demo-item {
        display: flex;
        justify-content: center;
        margin: 10px;
        border-radius: 4px;
        background-color: #fff;
        box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5);
        word-break: break-all;
    }
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 5%;
        background-color: #6495ED;
        /*color: #fff;*/
        text-align: center;
        padding: 10px 0;
        display: flex;
        justify-content: center;
        width: 50%;
        margin-left: 25%;
        margin-right: 25%;
        border-radius: 4px;
        box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5);
    }
    
</style>