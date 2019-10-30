<template>
  <div class="container">
    <div class="input-form">
      <div class="text-center mb-4">
          <img src="../assets/twitter_logo.png" alt="" class="mb-4" width="180">
          <h1>Search tweet</h1>
          <p v-if="error" class="alert alert-danger">{{error.Error}}</p>
      </div>
      <div class="input-group">
        <input type="text" class="form-control" v-model="tweet_handler" placeholder="Search Twitter">
      </div>
    </div>
    <!--search output from screen name-->
    <div class="tweet-user-search" v-if="users_list && tweet_handler">
      <div class="users" v-for="user in users_list" :key="user.screen_name" @click="getTimeline(user)">
        <img :src="user.profile_image" alt="user profile image"
             class="rounded-circle" width='48px' height='48px'>
        {{user.name}} -  <span style="color:#66757f, font-size='12px'">@{{user.screen_name}}</span>
      </div>
    </div>

    <!--loading waiting for timeline -->
    <div class="spinner-grow" style="width: 3rem; height: 3rem; color:#e0245e " role="status" v-if="!timeline">
      <span class="sr-only">Loading...</span>
    </div>

    <!--timeline of selected tweet handler -->
    <div class="tweet-timeline" v-if="timeline && users_list === null">
      <div class="content-tweet" v-for="(post, index) in timeline.timeline" :key="index">
        <div class="stream-item-header">
          <img :src="timeline.profile_image" alt="user profile image"
               class="rounded-circle avatar" width='48px' height='48px'>
          <p><strong>{{timeline.name}}</strong></p>
          <p style="color:#66757f; font-size:14px">@{{timeline.screen_name}}</p>
        </div>
        <div class="stream-content">
          <p>{{post.text}}</p>
        </div>
        <div class="stream-footer">
          <span style="margin-right:20px; color:#17bf63">
            <i class="fas fa-retweet" style="font-size:20px; color:#17bf63"></i><strong> {{post.retweet_count}}</strong>
          </span>
          <span style="color:#e0245e">
            <i class="far fa-heart" style="font-size: 20px; color:#e0245e"></i><strong> {{post.favorite_count}}</strong>
          </span>
          <span style="float:right; margin-right:10px"><strong>{{post.created_at | moment}}</strong></span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'
import moment from 'moment'
// @ is an alias to /src

export default {
  name: 'tweetPage',
  data (){
    return {
      tweet_handler: '',
      users_list: null,
      error: null,
      timeline: {},
    }
  },
  created() {
    this.debouncedGetAnswer = _.debounce(this.getUser, 300)
  },
  watch: {
    tweet_handler(){
      this.error = null
      this.debouncedGetAnswer()
    }
  },
  methods: {
    getUser(){
      if(this.tweet_handler){
        axios.get('/user-search/' + this.tweet_handler)
        .then( res=> {
          if (res.data.length > 0){
            this.users_list = res.data
          }
          else {
            this.users_list = null
            this.error = res.data
          }
        })
        .catch(()=>this.error = {"Error": "The connection was interrupted!"})
      }
      else{
        this.users_list = null
      }
    },
    getTimeline(data){
      this.users_list = null
      this.timeline = null
      axios.get('/timeline-search/' + data.screen_name)
      .then(res=>{
        if (res.data.timeline.length > 0){
          this.timeline = res.data
        }
        else {
          this.timeline = {}
          this.error = {"Error": "The user don't have any post!"}
        }
      })
      .catch(()=>this.error = {"Error": "The connection was interrupted!"})
    }
  },
  filters: {
    moment(data){
      return moment(data).format("DD MMM YYYY h:mm")
    }
  }

}
</script>

<style scoped>
  .container {
    width: 100%;
    max-width: 700px;
    padding: 15px;
    margin: auto;
    color: #434548;
    border-radius: 10px;
    margin-top: 5%;
  }

  .tweet-user-search{
    color: black;
    background-color: #fff;
    margin-top: 10px;
    border-radius: 10px;
    text-align: left;
    border: 1px solid
  }
  .users {
    padding: 5px;
  }
  div .users:hover {
    background-color: #97ddf3;
    cursor: pointer;
  }

  .form-control{
    width: 300px;
  }
  .content-tweet {
    text-align: left;
    padding: 10px 5px;
    border-radius: 15px;
    border: 2px solid #d4dfe3;
    margin: 5px 0;
  }
  .avatar {
    float: left;
    margin-right: 5px;
  }
  p{
    margin: 0
  }
  .stream-footer{
    margin-top: 20px;
    padding-left: 20px;
  }
  .retweet-icon {
    margin-right: 20px;
  }
</style>
