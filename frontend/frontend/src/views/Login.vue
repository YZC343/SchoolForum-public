<script setup lang="ts">
import { ElAside, ElContainer, ElForm, ElFormItem, ElHeader, ElInput, ElMain } from 'element-plus';

</script>

<template >
        <ElHeader style="height: 50px;
        box-shadow: 2px 0 6px rgba(0, 21, 41, 0.35);
        transition: all 0.3s;
        margin-bottom: 20px;
        ">
        <ElAside c style="vertical-align: middle;">
            <H3>校园论坛</H3>
        </ElAside>
        </ElHeader>
    
    <div style="justify-items: center;">
    <ElContainer style="width:360px;border:2px solid var(--el-border-color);border-radius: 8px;">
        <ElHeader 
        style="height: 24%;width: 100%;display: flex;justify-content: center;align-items: center;">
            <H1 style="color: var(--el-text-color-regular);"></H1>
        </ElHeader>
        <ElMain>
            <ElForm
        style="max-width:600px;justify-items: center"
        status-icon
        >
        <ElAside>
            <ElFormItem class="input">
                <ElInput style="width: 80%;" type="UserName" v-model="userName" autocomplete="off" placeholder="用户名"></ElInput>
            </ElFormItem>

            <ElFormItem class="input">
                <ElInput style="width: 80%;" type="Passowrd" v-model="password" autocomplete="off" placeholder="密码"></ElInput>
            </ElFormItem>
        </ElAside>
            

            </ElForm>
        </ElMain>
        <ElFooter style="display: flex;justify-content: center;">
             <ElButton @click="onClick_Login"  type="primary">登录</ElButton>
        </ElFooter>
        <ElFooter>
            <ElButton  text @click="onClick_Sign_up">立即注册</ElButton>
        </ElFooter>
    </ElContainer>
</div>

</template>

<script lang="ts">
    import router from '@/router';
    import axios from 'axios';
    export default {
        data(){
            return {
                userName:"",
                password:""
            }
        },

        methods:{
            onClick_Login(){
                if(this.userName!=''&&this.password!=''){
                    axios.post('/api/auth/login',{username:this.userName,pwd:this.password})
                    .then(response => {console.log(response);
                    if(response.status === 201 || response.status === 200){
                        console.log("login")
                        router.push('/Home');
                    }
                })
                .catch(error => console.error(error));
                }
                
            },
            postfrom() {
                
                axios.post('/api/login',
                {username:this.userName,pwd:this.password,},
                {withCredentials: true,}
            )
                .then(response => {console.log(response.data);
                    if(response.status === 201 || response.status === 200){
                        console.log("login")
                        router.push('/Home');
                    }
                })
                .catch(error => console.error(error));
            },
            onClick_Sign_up(){
                router.push({path:'/Sign_up'})
            }
        }
    }
</script>

<style>
    .input{
        width: 92%;
    }
</style>