<script setup lang="ts">
import { ElAside, ElButton, ElContainer, ElFooter, ElForm, ElFormItem, ElHeader, ElInput, ElMain, messageConfig } from 'element-plus';

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
            <ElButton text @click = "onClick_Login">已有账号？登录</ElButton>
        
        </ElAside>
        
        <ElAside>
            <ElFormItem class="input">
                <ElInput style="width:80%;" type="UserName" v-model="userName" autocomplete="off" placeholder="用户名"></ElInput>
            </ElFormItem>

            <ElFormItem style="margin-bottom: 15%;" class="input">
                <ElInput style="width:80%;" type="Passowrd" v-model="password" autocomplete="off" placeholder="密码"></ElInput>
            </ElFormItem>

            <ElFormItem  class="input">
                <ElInput style="width:80%;"  type="Passowrd" v-model="password_confirm" autocomplete="off" placeholder="确认密码"></ElInput>
            </ElFormItem>
        </ElAside>
        

        

        </ElForm>
    </ElMain>
    <ElFooter style="display: flex;justify-content: center;">
        <ElButton @click="onClick"  type="primary">注册</ElButton>
    </ElFooter>
    </ElContainer>
</div>

</template>

<script lang="ts">
    import axios from 'axios';
    import router from '@/router';
    export default {
        data() {
            return {
                userName:"",
                password:"",
                password_confirm:"",
                email:"",
                };
            },
        methods: {
            onClick() {
                if(this.userName!=''&&this.password==this.password_confirm&&this.password!=''){
                    
                    axios.post('http://127.0.0.1:5000/api/auth/register',{
                        username:this.userName,
                        password:this.password
                    })
                    .then(response => {console.log(response);
                        if(response.status === 201 || response.status === 200){
                        router.push('/Login');
                    }
                    }
                )
                    .catch(error => console.error(error));
                    
                }
                
            },

            postfrom() {
                
                axios.post('http://127.0.0.1:5000/api/register',{username:this.userName,password:this.password})
                .then(response => console.log(response))
                .catch(error => console.error(error));
            },
            onClick_Login(){
                router.push({path:'/Login'})
            }
        },
        /*
        mounted(){
            axios.post('/api/sign_up')
            .then(request => {
                request.data=[this.userName,this.password,this.email]
            })
            .catch(error => {
                console.error('There was an error!', error);
            });
        }
        */
    }
</script>

<style>
    .input{
        width: 92%;
    }
</style>

#