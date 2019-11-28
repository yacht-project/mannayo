<template>
  <div>
    <p class="title">
      누구랑 만나요?
    </p>
    <div class="field has-addons has-addons-centered">
      <div class="control">
        <div class="buttons">
          <button class="button is-outlined">
            회사
          </button>
          <button class="button is-outlined">
            친구
          </button>
          <button class="button is-outlined">
            가족
          </button>
          <button class="button is-outlined">
            낯선사람
          </button>
          <button class="button is-outlined">
            기타
          </button>
        </div>
        <input
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
});
</script>
