<template>
  <div>
    <p class="title">
      누구랑 만나요?
    </p>
    <div class="field has-addons has-addons-centered">
      <div class="control">
        <div class="buttons">
          <button class="button is-outlined" value="회사" @click="selectWho">
            회사
          </button>
          <button class="button is-outlined" value="친구" @click="selectWho">
            친구
          </button>
          <button class="button is-outlined" value="가족" @click="selectWho">
            가족
          </button>
          <button class="button is-outlined" value="낯선사람" @click="selectWho">
            낯선사람
          </button>
          <button class="button is-outlined" value="" @click="selectWho">
            기타
          </button>
        </div>
        <input
          v-model="who"
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
  name: 'WhoForm',
  props: {
  },
  data: () => ({
    who: '',
  }),
  methods: {
    selectWho(event: MouseEvent) {
      this.$data.who = (event.target as HTMLButtonElement).value;
    },
  },
});
</script>
