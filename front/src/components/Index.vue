<template>
    <div id="index">
        <form id="myForm" @submit.prevent="sendPost">
            <input v-model="title" placeholder="제목">
            <br>
            <input v-model="place" placeholder="장소">
            <br>
            <input type="checkbox" id="checkbox" v-model="holidayIncluded">
            <label for="checkbox">휴일 {{ holidayIncluded ? '포함' : '미포함' }}</label>
            <vc-date-picker
                mode='range'
                v-model='selectedValue'
                is-inline>
            </vc-date-picker>
            <button>저장</button>
        </form>
    </div>
</template>

<script>
import Vue from 'vue';
import VCalendar from 'v-calendar';
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VCalendar, {
  componentPrefix: 'vc',
});
Vue.use(VueAxios, axios);


export default {
    name: 'Index',
    data: function() {
        return {
            title: '',
            place: '',
            holidayIncluded: false,
            selectedValue: null
        }
    },
    methods: {
        sendPost: function () {
            this.axios.get('http://localhost:8081').then((response) => {
                console.log(response.data);
            });  
        }
    }
}
</script>