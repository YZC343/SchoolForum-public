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
            <el-menu-item  index="/home">首页</el-menu-item>
    
            
                <div style="display: flex;">
                    <ElInput style="height: 60%;width: 100%;" type="UserName"  autocomplete="off" placeholder=""></ElInput>
    
                    <ElButton style="height: 60%;" type="primary">搜索</ElButton>
                </div>
                
                <div style="display: flex;">
                    <el-menu-item index="/home">私信</el-menu-item>
    
                    <el-menu-item index="/User">用户</el-menu-item>
                </div>
            
                
            
        </ElMenu>   
        <ElContainer style="width: 50%;margin-left: 25%;margin-right: 25%;display: flex">
            <ElContainer style="min-width: 120px;max-width: 120px;height: 100%;border-radius: 4px;
                border: solid 2px #B0C4DE;flex-direction: column;display: flex;
                ">
                
                <ElContainer style="border-radius: 4px;border: solid 2px #B0C4DE;height: 40px;
                
                
                "
                v-for="user in userList"
                >
                    {{user.username}}
                </ElContainer>
                
            </ElContainer>


            <ElContainer style="height: 100%;border-radius: 4px;
                border: solid 2px #B0C4DE;flex-direction: column;display: flex;background-color:#EEEEEE;">

                <ElContainer style="display: flex;height: 40px;">

                <ElContainer style="width: 30%;">

                </ElContainer>

                <ElContainer style="background-color:blueviolet;width: 70%;">
                    
                </ElContainer>
                </ElContainer>

                <ElContainer style="border-radius: 4px;border:none;
                
                "
                v-for="message in messageList"
                
                >   
                <ElContainer style="display: flex;margin-top: 40px;"
                    v-if="message.sender_username == myname">

                    <ElContainer style="width: 30%;">

                    </ElContainer>

                    <ElContainer style="width: 70%;border-radius: 4px;
                        flex-direction: column;
                        box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5);
                        background-color: white;
                        ">
                        <div>{{message.sender_username}}</div>
                        <div>{{message.content}}</div>
                    </ElContainer>
                </ElContainer>
                
                <ElContainer style="display: flex;margin-top: 40px;"
                    v-if="message.sender_username != myname">

                    <ElContainer style="width: 70%;border-radius: 4px;
                        flex-direction: column;
                        box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.5);
                        background-color: white;
                        ">
                        <div>{{message.sender_username}}</div>
                        <div>{{message.content}}</div>
                    </ElContainer>

                    <ElContainer style="width: 30%;">

                    </ElContainer>

                    
                </ElContainer>   

                        
                        
                   
                    
                    
                    
                    
                </ElContainer>

                
            </ElContainer>
            
    
        </ElContainer>
        
    </template>
    
    <script lang="ts">
    import router from "@/router"
        export default{
            data() {
                return{
                    myname:"user0",

                    userList:[
                        {
                            username:"user1"
                        },
                        {
                            username:"user2"
                        },
                        {
                            username:"user3"
                        },
                        {
                            username:"user4"
                        },
                        {
                            username:"user5"
                        },
                    ],

                    messageList:[
                        {
                            sender_username:"user1",
                            content:"sendmessage1"
                        },
                        {
                            sender_username:"user1",
                            content:"sendmessage2"
                        },
                        {
                            sender_username:"user0",
                            content:"sendmessage3"
                        },
                        {
                            sender_username:"user1",
                            content:"sendmessage4"
                        },
                        {
                            sender_username:"user0",
                            content:"sendmessage5"
                        },
                    ],

                    
                }
                
                
            },
            methods:{
                clickBoard(){
                    router.push("/Board")
                }
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