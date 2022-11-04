<template>
    <div class='chart' id='chart'></div>
    <div v-if="lang == 'en'">
        <div class="reborn-botton">
            <el-button @click="reborn()">Reborn</el-button>
        </div>
        <div v-show="showTable">
            <div class="count-table">
                <el-table :data="rebornCount" :table-layout="auto" size="small" style="width: 100%; font-weight: bold;">
                    <el-table-column prop="times" label="Frequency" style="width: auto;" />
                    <el-table-column prop="非洲" label="AF" width="auto" />
                    <el-table-column prop="欧洲" label="EU" width="auto" />
                    <el-table-column prop="亚洲" label="AS" width="auto" />
                </el-table>
            </div>
            <div class="count-table">
                <el-table show-header :data="rebornCount" :table-layout="auto" size="small"
                    style="width: 100%; font-weight: bold;">
                    <el-table-column prop="北美洲" label="NA" width="auto" />
                    <el-table-column prop="南美洲" label="SA" width="auto" />
                    <el-table-column prop="大洋洲" label="OA" width="auto" />
                    <el-table-column prop="南极洲" label="AN" width="auto" />
                </el-table>
            </div>
        </div>
        <div v-show="showTable" class="reborn-info">
            <el-table :data="rebornLog" :table-layout="auto" size="small" stripe style="width: 100%;">
                <el-table-column prop="times" label="Frequency" sortable style="width: auto;" />
                <el-table-column prop="continent" label="Continent" sortable width="auto" />
                <el-table-column prop="name" label="Country" sortable width="auto" />
            </el-table>
        </div>
    </div>
    <div v-else>
        <div class="reborn-botton">
            <el-button @click="reborn()">重生</el-button>
        </div>
        <div v-show="showTable">
            <div class="count-table">
                <el-table :data="rebornCount" :table-layout="auto" size="small" style="width: 100%; font-weight: bold;">
                    <el-table-column prop="times" label="重生次数" style="width: auto;" />
                    <el-table-column prop="非洲" label="非洲" width="auto" />
                    <el-table-column prop="欧洲" label="欧洲" width="auto" />
                    <el-table-column prop="亚洲" label="亚洲" width="auto" />
                </el-table>
            </div>
            <div class="count-table">
                <el-table show-header :data="rebornCount" :table-layout="auto" size="small"
                    style="width: 100%; font-weight: bold;">
                    <el-table-column prop="北美洲" label="北美洲" width="auto" />
                    <el-table-column prop="南美洲" label="南美洲" width="auto" />
                    <el-table-column prop="大洋洲" label="大洋洲" width="auto" />
                    <el-table-column prop="南极洲" label="南极洲" width="auto" />
                </el-table>
            </div>
        </div>
        <div v-show="showTable" class="reborn-info">
            <el-table :data="rebornLog" :table-layout="auto" size="small" stripe style="width: 100%;">
                <el-table-column prop="times" label="重生次数" sortable style="width: auto;" />
                <el-table-column prop="continent" label="地区" sortable width="auto" />
                <el-table-column prop="name" label="国家" sortable width="auto" />
            </el-table>
        </div>
    </div>
</template>
 
<script>
module.exports = {
    data() {
        return {
            protocol: 'http',
            url: window.location.host,
            data: {},
            coordinate: [104.195397, 35.86166], //China
            percentArray: null,
            showTable: false,
            times: 0,
            continentDict: {
                'AF': '非洲',
                'EU': '欧洲',
                'AS': '亚洲',
                'OA': '大洋洲',
                'NA': '北美洲',
                'SA': '南美洲',
                'AN': '南极洲'
            },
            rebornCount: [{
                'times': 0,
                '非洲': 0,
                '欧洲': 0,
                '亚洲': 0,
                '大洋洲': 0,
                '北美洲': 0,
                '南美洲': 0,
                '南极洲': 0
            }],
            rebornLog: [],
            zoom: 1.25,
            center: [17.228331, 26.3351]
        };
    },
    props: {
        lang: '',
    },
    mounted: function () {
        this.getData()
    },
    methods: {
        getData() {
            var that = this
            $.ajax({
                type: "get",
                url: this.protocol + '://' + this.url + '/reborn/getData',
                async: false,
                success: function (result) {
                    result = eval(result)
                    that.data = result
                }
            })
            this.init()
            // console.log(this.data)
        },
        init() {
            this.myChart = echarts.init(document.getElementById('chart'))
            this.myChart.setOption(this.option());
        },
        reborn() {
            let total = 100000
            if (this.percentArray == null) {
                this.percentArray = new Array();
                for (let i = 0; i < this.data.length; i++) {
                    let percent = this.data[i]['birth_rate'] * 1000
                    for (let j = 0; j < percent; j++) {
                        this.percentArray.push(i)
                    }
                }
            }
            let rand = Math.floor(Math.random() * total)
            let result = this.data[this.percentArray[rand]]
            // console.log(result)

            this.coordinate = result['position']
            this.center = result['position']
            this.times += 1
            let temp_dict = {}
            temp_dict['times'] = this.times
            temp_dict['name'] = this.lang == 'en' ? result['en'] : result['cn']
            temp_dict['continent'] = this.lang == 'en' ? result['continent'] : this.continentDict[result['continent']]
            this.rebornLog.unshift(temp_dict)

            this.rebornCount[0]['times'] = this.times
            this.rebornCount[0][this.continentDict[result['continent']]] += 1

            this.showTable = true
            this.zoom = 2.0
            this.myChart.setOption(this.option())
        },
        option() {
            return {
                backgroundColor: '#E8E8E8',
                geo: {
                    map: 'world',
                    roam: true,
                    zoom: this.zoom,
                    label: {
                        emphasis: {
                            show: false,
                        }
                    },
                    center: this.center,
                    tooltip: {
                        show: true
                    },
                    // silent: true,
                    itemStyle: {
                        normal: {
                            areaColor: '#CFCFCF',
                            borderColor: '#111'
                        },
                        emphasis: {
                            areaColor: '#2a333d'
                        }
                    }
                },
                series: {
                    type: 'custom',
                    coordinateSystem: 'geo',
                    geoIndex: 0,
                    zlevel: 1,
                    data: [
                        this.coordinate
                    ],
                    renderItem(params, api) {
                        const coord = api.coord([
                            api.value(0, params.dataIndex),
                            api.value(1, params.dataIndex)
                        ]);
                        const circles = [];
                        for (let i = 0; i < 5; i++) {
                            circles.push({
                                type: 'circle',
                                shape: {
                                    cx: 0,
                                    cy: 0,
                                    r: 30
                                },
                                style: {
                                    stroke: 'red',
                                    fill: 'none',
                                    lineWidth: 2
                                },
                                // Ripple animation
                                keyframeAnimation: {
                                    duration: 4000,
                                    loop: true,
                                    delay: (-i / 4) * 4000,
                                    keyframes: [
                                        {
                                            percent: 0,
                                            scaleX: 0,
                                            scaleY: 0,
                                            style: {
                                                opacity: 1
                                            }
                                        },
                                        {
                                            percent: 1,
                                            scaleX: 1,
                                            scaleY: 0.4,
                                            style: {
                                                opacity: 0
                                            }
                                        }
                                    ]
                                }
                            });
                        }
                        return {
                            type: 'group',
                            x: coord[0],
                            y: coord[1],
                            children: [
                                ...circles,
                                {
                                    type: 'path',
                                    shape: {
                                        d: 'M16 0c-5.523 0-10 4.477-10 10 0 10 10 22 10 22s10-12 10-22c0-5.523-4.477-10-10-10zM16 16c-3.314 0-6-2.686-6-6s2.686-6 6-6 6 2.686 6 6-2.686 6-6 6z',
                                        x: -10,
                                        y: -35,
                                        width: 20,
                                        height: 40
                                    },
                                    style: {
                                        fill: 'red'
                                    },
                                    // Jump animation.
                                    keyframeAnimation: {
                                        duration: 1000,
                                        loop: true,
                                        delay: Math.random() * 1000,
                                        keyframes: [
                                            {
                                                y: -10,
                                                percent: 0.5,
                                                easing: 'cubicOut'
                                            },
                                            {
                                                y: 0,
                                                percent: 1,
                                                easing: 'bounceOut'
                                            }
                                        ]
                                    }
                                }
                            ]
                        };
                    }
                }
            }
        }
    }
}
</script>
 
<style>

</style>