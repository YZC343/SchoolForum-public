<template>
    <ElContainer >
        <div style="display: flex;">
        <ElAside style="width: 15%"></ElAside>
        <ElScrollbar >
        <ElContainer v-for="item in message" class="scrollbar-demo-item">
            <ElHeader style="height: 20px;">{{ item.author }}:</ElHeader>
            <ElMain>{{ item.text }}</ElMain>
            <Footer>{{ item.time }}</Footer>
        </ElContainer>
      </ElScrollbar>
      <ElAside style="width: 15%"></ElAside>
    </div>
    </ElContainer>
  </template>
   
  <script>
import { ElAside, ElContainer, ElHeader, ElMain, ElScrollbar } from 'element-plus';

  export default {
    name:"Scroll",

    data() {
      return {
        count: 0,
        message:[
            {
                author:"东厂厂公凤九霄",
                text:"【分享】我玩过的模拟经营类游戏",
                time:"2014-11-07 21:27"
            },

            {
                author:"东厂厂公凤九霄",
                text:"怎么回事？我写了一大段怎么没了？",
                time:"2014-11-07 21:28"
            },

            {
                author:"东厂厂公凤九霄",
                text:"《不思议之国的冒险酒场》，开罗系列，牧场物语，《发明工坊》系列，《艾莉的工作室》系列，《中华客栈》",
                time:"2014-11-07 21:30"
            },

            {
                author:"东厂厂公凤九霄",
                text:"艾莉的工作室系列都是炼金术士类游戏，年头都比较早，还是PSP游戏，win7用户玩这个得下模拟器，要是模拟器还玩不起就还得下其他东西，百度上有。中华客栈2就是选个角色然后开店，卖菜。刚开始还有点新鲜劲，后来店升到五级后久没啥意思了。",
                time:"2014-11-07 21:33"
            },

            {
                author:"东厂厂公凤九霄",
                text:"《不思议之国的冒险酒场》是RPG+经营的手机单机游戏，非常好玩儿的游戏。希望霓虹国多开发此类游戏。开罗是像素风格的手游，现在是越来越增加游戏元素了，好评。《发明工坊》也是RPG+经营，但是第1部真心难玩儿！作弊都打不过！但是有剧情限制，一旦剧情结束，你、建成的所有的东西都必须停止，差评！",
                time:"2014-12-01 11:38"
            },

            {
                author:"东厂厂公凤九霄",
                text:"【分享】我玩过的模拟经营类游戏",
                time:"2014-11-07 21:27"
            },

            {
                author:"东厂厂公凤九霄",
                text:"怎么回事？我写了一大段怎么没了？",
                time:"2014-11-07 21:28"
            },

            {
                author:"东厂厂公凤九霄",
                text:"《不思议之国的冒险酒场》，开罗系列，牧场物语，《发明工坊》系列，《艾莉的工作室》系列，《中华客栈》",
                time:"2014-11-07 21:30"
            },

            {
                author:"东厂厂公凤九霄",
                text:"艾莉的工作室系列都是炼金术士类游戏，年头都比较早，还是PSP游戏，win7用户玩这个得下模拟器，要是模拟器还玩不起就还得下其他东西，百度上有。中华客栈2就是选个角色然后开店，卖菜。刚开始还有点新鲜劲，后来店升到五级后久没啥意思了。",
                time:"2014-11-07 21:33"
            },

            {
                author:"东厂厂公凤九霄",
                text:"《不思议之国的冒险酒场》是RPG+经营的手机单机游戏，非常好玩儿的游戏。希望霓虹国多开发此类游戏。开罗是像素风格的手游，现在是越来越增加游戏元素了，好评。《发明工坊》也是RPG+经营，但是第1部真心难玩儿！作弊都打不过！但是有剧情限制，一旦剧情结束，你、建成的所有的东西都必须停止，差评！",
                time:"2014-12-01 11:38"
            },
            {
                author:"东厂厂公凤九霄",
                text:"【分享】我玩过的模拟经营类游戏",
                time:"2014-11-07 21:27"
            },

            {
                author:"东厂厂公凤九霄",
                text:"怎么回事？我写了一大段怎么没了？",
                time:"2014-11-07 21:28"
            },

            {
                author:"东厂厂公凤九霄",
                text:"《不思议之国的冒险酒场》，开罗系列，牧场物语，《发明工坊》系列，《艾莉的工作室》系列，《中华客栈》",
                time:"2014-11-07 21:30"
            },

            {
                author:"东厂厂公凤九霄",
                text:"艾莉的工作室系列都是炼金术士类游戏，年头都比较早，还是PSP游戏，win7用户玩这个得下模拟器，要是模拟器还玩不起就还得下其他东西，百度上有。中华客栈2就是选个角色然后开店，卖菜。刚开始还有点新鲜劲，后来店升到五级后久没啥意思了。",
                time:"2014-11-07 21:33"
            },

            {
                author:"东厂厂公凤九霄",
                text:"《不思议之国的冒险酒场》是RPG+经营的手机单机游戏，非常好玩儿的游戏。希望霓虹国多开发此类游戏。开罗是像素风格的手游，现在是越来越增加游戏元素了，好评。《发明工坊》也是RPG+经营，但是第1部真心难玩儿！作弊都打不过！但是有剧情限制，一旦剧情结束，你、建成的所有的东西都必须停止，差评！",
                time:"2014-12-01 11:38"
            },
            
        ]
      }
    },
    methods: {
      load() {
        console.log('我触发了')
        this.count += 2
      }
    }
  }
  </script>
   
  <style>
  .box{
    width: 100%;
    height: 50px;
    background-color: red;
    border: none;
  }
  .scrollbar-demo-item {
  display: flex;
  justify-content: center;
  margin: 10px;
  border-radius: 4px;
  background: var(--el-color-primary-light-9);
  /*color: var(--el-color-primary);*/
  
}
  </style>