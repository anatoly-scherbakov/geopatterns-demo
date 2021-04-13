---
title: geopatterns-demo
---

<div id="app">
    <h1 class="ui header">
        Geopatterns demo
    </h1>
    <div class="ui container">
        <div class="ui large fluid action labeled input">
          <div class="ui label">
            Phrase: 
          </div>
          <input v-model="input_text" type="text" placeholder="">
          <button class="ui green button" @click="update_text">
            <i class="play alternate icon"></i>
          </button>
        </div>
    </div>

    <div class="ui hidden divider"></div>
    
    <div class="ui four cards">
        <preview-card :method="method" :text="display_text" v-for="method in methods">
        </preview-card>
    </div>

</div>

<style>
    .image {
        min-height: 128px;
        background-repeat: repeat !important;
        background-size: contain !important;
        background-position: center center;
    }
</style>
