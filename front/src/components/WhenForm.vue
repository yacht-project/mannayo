<template>
    <div class="when-form">
        <p class="title">언제 만나요?(필수에요.)</p>
        <div class="field has-addons has-addons-centered">
            <div class="control">
                <input type="checkbox" id="checkbox" v-model="holidayIncluded">
                <label for="checkbox">휴일 {{ holidayIncluded ? '포함' : '미포함' }}</label>
                <vc-date-picker
                    mode='range'
                    v-model='selectedValue'
                    is-inline>
                </vc-date-picker>
            </div>
        </div>
    </div>
</template>
