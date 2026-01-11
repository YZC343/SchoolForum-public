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
            <ElContainer style="margin-left: 20px;margin-right: 20px;">
                <ElFormItem style="width: 100%;">
                    <ElInput 
                    style="width: 100%;" 
                    show-word-limit
                    maxlength="800"
                    :autosize = "{ minRows: 18, maxRows: 30 }"
                    type="textarea"
                    v-model="reply.content" 
                    autocomplete="off" 
                    placeholder="输入帖子内容">
                </ElInput>
                </ElFormItem>
            </ElContainer>
            <ElContainer>
                <ElAside style="width: 80%;">
    
                </ElAside>
                <ElAside>
                    <ElButton  text @click="modify_reply" type="primary">确认修改</ElButton>
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
                    post:{},
                    reply:{}
                }
                
            },
            mounted(){
                this.getReply()
            },
            methods:{
                modify_reply(){
                    if(this.title!=''&&this.content!=''){
                        axios.post('/api/replies/edit',
                        {uuid:this.$route.query.uuid,sequence_no:this.$route.query.sequence_no,content:this.reply.content},
                        {withCredentials: true,}
                    )
                        .then(response =>console.log(response.data))
                        .catch(error => console.error(error));
                        console.log("edit_reply")
                        router.push({
                            path:"/User",
                        })
                    }
                },
                getReply(){
                axios.post('/api/replies/pick',{uuid:this.$route.query.uuid,sequence_no:this.$route.query.sequence_no})
                    .then(response => {
                        console.log(response);
                        this.reply=response.data
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