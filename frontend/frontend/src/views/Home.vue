<script setup lang="ts">
import { ElButton, ElContainer, ElHeader, ElMain, ElMenu } from 'element-plus';

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

                <el-menu-item  index="/Login">切换用户</el-menu-item>
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
        
        <ElContainer style="" v-for="item in board" class="scrollbar-demo-item" 
        @click = "clickBoard(item)"
        >
            <ElHeader style="height: 20px;font-weight: bold;font-size: 1.25em;">{{ item.name }}:</ElHeader>
            <ElMain
            style="
            margin: 10px;
            border-radius: 4px;
            border: solid 2px #B0C4DE;"
            >{{ item.content }}</ElMain>
        </ElContainer>

    </ElContainer>
    
</template>

<script lang="ts">
import router from "@/router"
import axios from 'axios';
import { ref } from 'vue';
    
    export default{
        data() {
            return{
                board:ref([]),
                keyword:""
                
                 /*
                    {
                        name:"板块名称",
                        content:"板块内容XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                    },
                    {
                        name:"板块名称",
                        content:"板块内容XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                    },
                    {
                        name:"板块名称",
                        content:"板块内容XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                    },
                    {
                        name:"板块名称",
                        content:"板块内容XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                    },
                    {
                        name:"板块名称",
                        content:"板块内容XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                    },
                    {
                        name:"板块名称",
                        content:"板块内容XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                    },
                    {
                        name:"板块名称",
                        content:"板块内容XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                    },
                    {
                        name:"板块名称",
                        content:"板块内容XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                    },
                    */
            }
        },
        methods:{
            clickBoard(item){
                router.push({
                    path:"/Board",
                    query:{name:item.name},
                })
                console.log(item.name)
            },
            getBoardList(){
                axios.get('/api/board/list',)
                    .then(response => {console.log(response);
                    this.board=response.data
                })
                .catch(error => console.error(error));
                
            },
            click_search(){
                router.push({
                    path:"/Board",
                    query:{keyword:this.keyword}
                })
            }
        },
        mounted(){
            this.getBoardList()
        }
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
    
</style>