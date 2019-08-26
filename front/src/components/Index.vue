<template>
    <div class="container is-fluid">
        <nav class="level">
            <div class="level-item has-text-centered">
                <div>
                    <p class="heading">언제 만나요?(필수에요.)</p>
                    <div class="box">
                        <article class="media">
                            <div class="media-content">
                                <div class="content">
                                    <input type="checkbox" id="checkbox" v-model="holidayIncluded">
                                    <label for="checkbox">휴일 {{ holidayIncluded ? '포함' : '미포함' }}</label>
                                    <vc-date-picker
                                        mode='range'
                                        v-model='selectedValue'
                                        is-inline>
                                    </vc-date-picker>
                                </div>
                            </div>
                        </article>
                    </div>
                </div>
            </div>

            <div class="level-item has-text-centered">
                <div>
                    <p class="heading">왜 만나요?</p>
                    <div class="box">
                        <article class="media">
                            <div class="media-content">
                                <div class="content">
                                    <a class="button is-rounded">회식</a>
                                    <a class="button is-rounded">티타임</a>
                                    <a class="button is-rounded">급벙개</a>
                                    <a class="button is-rounded">작당모의</a>
                                    <a class="button is-rounded">동호회</a>
                                    <a class="button is-rounded">가족모임</a>
                                    <a class="button is-rounded">소개팅</a>
                                    <a class="button is-rounded">식사</a>
                                    <a class="button is-rounded">여행</a>
                                    <a class="button is-rounded">기타</a>
                                    <input class="input" type="text" placeholder="직접 입력">
                                </div>
                            </div>
                        </article>
                    </div>
                </div>
            </div>

            <div class="level-item has-text-centered">
                <div>
                    <p class="heading">누구랑 만나요?</p>
                    <div class="box">
                        <article class="media">
                            <div class="media-content">
                                <div class="content">
                                    <a class="button is-rounded">회사</a>
                                    <a class="button is-rounded">친구</a>
                                    <a class="button is-rounded">가족</a>
                                    <a class="button is-rounded">낯선사람</a>
                                    <a class="button is-rounded">기타</a>
                                    <input class="input" type="text" placeholder="직접 입력">
                                </div>
                            </div>
                        </article>
                    </div>
                </div>
            </div>

            <div class="level-item has-text-centered">
                <div>
                    <p class="heading">어디서 만나요?</p>
                    <div class="box">
                        <article class="media">
                            <div class="media-content">
                                <div class="content">
                                    <input class="input" type="text" placeholder="만날 장소를 입력해보세요.">
                                </div>
                            </div>
                        </article>
                    </div>
                </div>
            </div>
        </nav>
        
        <a class="button is-success float">만나자!</a>
    </div>
</template>

<script>


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
                return response;
            });  
        }
    }
}
</script>

<style scoped>
.float{
	position:fixed;
	width:60px;
	height:60px;
	bottom:40px;
	right:40px;
	background-color:#0C9;
	color:#FFF;
	border-radius:50px;
	text-align:center;
	box-shadow: 2px 2px 3px #999;
}
</style>