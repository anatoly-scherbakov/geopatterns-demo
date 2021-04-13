---
title: geopatterns
---

<div id="app">
    <div class="ui container">
        <form class="ui form" @submit.prevent="update_text">    
            <div class="ui large fluid action labeled input">
              <div class="ui label">
                Phrase: 
              </div>
              <input v-model="input_text" type="text" placeholder="Input something and hit Enter ☺">
              <button type="submit" class="ui green button">
                <i class="play alternate icon"></i>
              </button>
            </div>
        </form>
    </div>

    <div class="ui hidden divider"></div>
    
    <div class="ui four stackable cards">
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
