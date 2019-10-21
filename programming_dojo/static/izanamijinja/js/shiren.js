let shiren_obj = JSON.parse(document.getElementById('shiren_obj').textContent);
let tekishu = shiren_obj.tekishu;
console.log('tekihsu:', tekishu);

let kazu = 0;
let tekikazu = tekishu.length;
let kata = tekishu[kazu];
let wazas = [kata.waza1, kata.waza2, kata.waza3]

new Vue({
    el: '#shiren',
    delimiters: ['[[', ']]'],
    data: {
        vkazu: kazu + 1,
        vtekishu: tekishu,
        vtekikazu: tekikazu,
        vkata: kata,
        zan1: '',
        zan2: '',
        zan3: '',
        zanbtnlabel: 'Zan',
        zanbtnclassname: 'btn btn-info',
        showshirengroup: true,
    },
    computed: {
        zanbtnclass: {
            get: function() {
                if (kazu >= tekikazu - 1) {
                    return 'btn btn-success';
                }
                return this.zanbtnclassname;
            },
            set: function(newclassname) {
                this.zanbtnclassname = newclassname;
            }
        }
    },
    methods: {
        zan: function() {
            if (kazu >= tekikazu - 1) {
                console.log('Zanshin');
                console.log('tekishu', tekishu);
                this.showshirengroup = false;
                return;
            }
            let zan_lst = [this.zan1.trim(), this.zan2.trim(), this.zan3.trim()];
            let waza_lst = [kata.waza1.trim(), kata.waza2.trim(), kata.waza3.trim()];
            console.log('zan_set:', zan_lst);
            console.log('waza_set:', waza_lst);
            let seikou = true;
            for (let zan of zan_lst) {
                if (!waza_lst.includes(zan)) {
                    seikou = false;
                    break;
                }
            }
            console.log('seikou:', seikou);
            kata.seikou = seikou;
            if (kazu >= tekikazu - 2) {
                this.zanbtnlabel = 'Zanshin';
                this.zanbtnclass = 'btn btn-success';
            }

            this.zan1 = '';
            this.zan2 = '';
            this.zan3 = '';
            this.vkazu = ++kazu + 1;
            this.vkata = tekishu[kazu];
            kata = tekishu[kazu];
        }
    }
});
