<script setup lang="ts">
    import { ElAside, ElButton, ElContainer, ElHeader, ElMain, ElMenu, } from 'element-plus';
    
    
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
                    <el-menu-item index="/home">私信</el-menu-item>
    
                    <el-menu-item index="/home">用户</el-menu-item>
                </div>
            
                
            
        </ElMenu>
        <ElContainer style="width: 50%;
        margin-top: 30px;
        margin-left: 25%;
        margin-right: 25%;
        display: flex;
        flex-direction: column;
        border: 2px solid #666;
        border-radius: 4px;">
            <ElAside style="margin-top: 20px;margin-left: 20px;">
                <ElFormItem class="input">
                    <ElInput style="width: 80%;" type="UserName" v-model="post.title" autocomplete="off" placeholder="标题"></ElInput>
                </ElFormItem>
            </ElAside>
            <ElContainer style="margin-left: 20px;margin-right: 20px;">
                <ElFormItem style="width: 100%;">
                    <ElInput 
                    style="width: 100%;" 
                    show-word-limit
                    maxlength="800"
                    :autosize = "{ minRows: 18, maxRows: 30 }"
                    type="textarea"
                    v-model="post.content" 
                    autocomplete="off" 
                    placeholder="输入帖子内容">
                </ElInput>
                </ElFormItem>
            </ElContainer>
            <ElContainer>
                <ElAside style="width: 80%;">
    
                </ElAside>
                <ElAside>
                    <ElButton  text @click="modify_post" type="primary">确认修改</ElButton>
                </ElAside>
            </ElContainer>
            
        </ElContainer>
    
    
        
        
        
    </template>
    
    <script lang="ts">
    import router from '@/router';
    import axios from 'axios';
        export default{
            data() {
                return{
                    post:{}
                }
                
            },
            mounted(){
                this.getPost()
            },
            methods:{
                modify_post(){
                    if(this.title!=''&&this.content!=''){
                        axios.post('/api/posts/edit',
                        {uuid:this.$route.query.uuid,title:this.post.title,content:this.post.content},
                        {withCredentials: true,}
                    )
                        .then(response =>console.log(response.data))
                        .catch(error => console.error(error));
                        console.log("edit_post")
                        router.push({
                            path:"/User",
                        })
                    }
                },
                getPost(){
                axios.post('/api/posts/pick',{uuid:this.$route.query.uuid})
                    .then(response => {
                        console.log(response);
                        this.post=response.data
                })
                .catch(error => console.error(error));
                },
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