<template>
    <div>
        <md-table>
            <md-table-row>
                <md-table-head>참여자</md-table-head>
                <md-table-head v-for="date in dates" v-bind:key="date">
                    {{ date }}
                </md-table-head>
            </md-table-row>

            <md-table-row v-for="(schedule, idx) in schedules" v-bind:key="idx">
                <md-table-cell>{{ schedule.get('name') }}</md-table-cell>
                <md-table-cell v-for="(date, dIdx) in schedule.get('dates')" v-bind:key="dIdx">
                    <div><md-button>안 비지</md-button></div>
                </md-table-cell>
            </md-table-row>
            <md-table-row>
                <md-table-cell>
                    <div>
                        <md-field>
                            <label>니 이름</label>
                            <md-input v-on:keyup.enter="add" v-model="name"></md-input>
                            <span class="md-helper-text">김모씨(34세)</span>
                        </md-field>
                    </div>
                </md-table-cell>
            </md-table-row>
        </md-table>
    </div>
</template>

<script>

export default {
    name: 'Schedule',
    element: 'schedule',
    data: function() {
        return {
            name: "",
            dates : [
                "1월 29일",
                "1월 30일",
                "1월 31일",
                "2월 1일",
                "2월 2일",
                "2월 3일"
            ],
            schedules : []
        }
    },
    methods: {
        add(element) {
            let dates = new Map();
            let schedules = new Map([
                ['name', this.name],
                ['dates', dates]
            ]);
            

            for (let date of this.dates) {
                dates.set(date, false);
            }
            schedules.set('dates', dates)
            this.schedules.push(schedules);
        }
    }
}
</script>
