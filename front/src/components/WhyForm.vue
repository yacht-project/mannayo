<template>
  <div>
    <p class="title">
      왜 만나요?
    </p>
    <div class="field has-addons has-addons-centered">
      <div class="control">
        <div class="buttons">
          <button class="button is-outlined" value="회식" @click="selectWhy">
            회식
          </button>
          <button class="button is-outlined" value="티타임" @click="selectWhy">
            티타임
          </button>
          <button class="button is-outlined" value="급벙개" @click="selectWhy">
            급벙개
          </button>
          <button class="button is-outlined" value="작당모의" @click="selectWhy">
            작당모의
          </button>
          <button class="button is-outlined" value="동호회" @click="selectWhy">
            동호회
          </button>
          <button class="button is-outlined" value="가족모임" @click="selectWhy">
            가족모임
          </button>
          <button class="button is-outlined" value="소개팅" @click="selectWhy">
            소개팅
          </button>
          <button class="button is-outlined" value="식사" @click="selectWhy">
            식사
          </button>
          <button class="button is-outlined" value="여행" @click="selectWhy">
            여행
          </button>
          <button class="button is-outlined" value="" @click="selectWhy">
            기타
          </button>
        </div>
        <input
          v-model="why"
          class="input"
          type="text"
          placeholder="직접 입력"
        >
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  name: 'WhyForm',
  props: {
  },
  data: () => ({
    why: '',
  }),
  methods: {
    selectWhy(event: MouseEvent) {
      this.$data.why = (event.target as HTMLButtonElement).value;
    },
  },
});
</script>
