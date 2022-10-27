<template>
    <div class='chart' id='chart'></div>
</template>
 
<script>
module.exports = {
    data() {
        return {
            protocol: 'http',
            url: window.location.host,
            showFlag: false,
            initDataNum: 10,
            curData: {},
            keys: [],
            data: {},
        };
    },
    // props: {
    //     year: null,
    //     tab: null
    // },
    mounted: function () {
        this.getData()
        // let dataList
        // $.ajax({
        //     type: "get",
        //     url: this.protocol + '://' + this.url + '/animationlist/getData?year=' + this.year,
        //     async: false,
        //     success: function (result) {
        //         dataList = eval('[' + result + ']')[0]
        //     }
        // })
        // this.data = dataList
        // // console.log(this.data)
        // this.keys = Object.keys(this.data)
        // for (let i = 0; i < 10; i++) {
        //     this.curData[this.keys[i]] = this.data[this.keys[i]]
        // }
        // this.showFlag = true
    },
    methods: {
        getData() {
            var that = this
            $.ajax({
                type: "get",
                url: this.protocol + '://' + this.url + '/redeploy/getData',
                async: false,
                success: function (result) {
                    result = eval('[' + result + ']')[0]
                }
            })
            this.init()
        },
        init() {
            this.myChart = echarts.init(document.getElementById('chart'))
            this.myChart.setOption(this.option());
        },
        option() {
            return {
                backgroundColor: '#000',
                // title: {
                //     text: '10000000 GPS Points',
                //     left: 'center',
                //     textStyle: {
                //         color: '#fff'
                //     }
                // },
                geo: {
                    map: 'world',
                    roam: true,
                    label: {
                        emphasis: {
                            show: false
                        }
                    },
                    silent: true,
                    itemStyle: {
                        normal: {
                            areaColor: '#323c48',
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
                        [-75.440806, 40.652083, 100],
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