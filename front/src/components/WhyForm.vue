<template>
  <div>
    <p class="title">
      왜 만나요?
    </p>
    <div class="field has-addons has-addons-centered">
      <div class="control">
        <div class="buttons">
          <a class="button is-outlined">회식</a>
          <a class="button is-outlined">티타임</a>
          <a class="button is-outlined">급벙개</a>
          <a class="button is-outlined">작당모의</a>
          <a class="button is-outlined">동호회</a>
          <a class="button is-outlined">가족모임</a>
          <a class="button is-outlined">소개팅</a>
          <a class="button is-outlined">식사</a>
          <a class="button is-outlined">여행</a>
          <a class="button is-outlined">기타</a>
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
  name: 'WhyForm',
  props: {
  },
});
</script>
