<script setup lang="ts">
import { ElButton, ElContainer, ElHeader, ElMain, ElMenu } from 'element-plus';

</script>

<template>
  <router-view></router-view>
</template>

<style>
  .menubutton{
    display: flex;
    width: 100px;
    height: 56px;
  }
  .header{
    position: fixed;
    z-index: 999;
  }
</style>