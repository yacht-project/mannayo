<template>
  <div class="when-form">
    <p class="title">
      언제 만나요?(필수에요.)
    </p>
    <div class="field has-addons has-addons-centered">
      <div class="control">
        <input
          id="checkbox"
          v-model="holidayIncluded"
          type="checkbox"
        >
        <label for="checkbox">휴일 {{ holidayIncluded ? '포함' : '미포함' }}</label>
        <vc-date-picker
          v-model="selectedValue"
          mode="range"
          is-inline
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  name: 'WhenForm',
  props: {
  },
});
</script>
