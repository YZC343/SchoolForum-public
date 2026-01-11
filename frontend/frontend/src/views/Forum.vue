

<template>
    <ElContainer>
      <ElHeader>
        
      </ElHeader>
      <ElMain>
        <scroll></scroll>
      </ElMain>
      <ElFooter style="display: flex;justify-content: center;">
        <input-box></input-box>
      </ElFooter>
    </ElContainer>
    
  </template>
  
  <script setup>
    import { ElContainer, ElFooter, ElHeader, ElMain } from 'element-plus';
  import Scroll from '@/components/Scroll.vue';
  import InputBox from '@/components/InputBox.vue';

  

  </script>