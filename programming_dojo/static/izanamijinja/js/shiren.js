axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

let shiren_obj = JSON.parse(document.getElementById('shiren_obj').textContent);
console.log('shiren_obj:', shiren_obj);

let rendo_arr = ['Mijuku', 'Nami', 'Jukuren'];

new Vue({
    el: '#shiren',
    delimiters: ['[[', ']]'],
    data: {
        kazu: 0,
        seikousu: 0,
        tekishu: shiren_obj.tekishu,
        tekikazu: shiren_obj.tekishu.length,
        kata: shiren_obj.tekishu[0],
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
                if (this.kazu >= this.tekikazu - 1) {
                    return 'btn btn-success';
                }
                return this.zanbtnclassname;
            },
            set: function(newclassname) {
                this.zanbtnclassname = newclassname;
            }
        },
    },
    methods: {
        isBlank: function(str) {
            return str.length > 0;
        },
        isShippai: function(shippai_lst, waza) {
            return shippai_lst.includes(waza);
        },
        showrendo: function(rendo) {
            return rendo_arr[parseInt(rendo)]
        },
        showmigaki: function(migaki) {
            if (migaki > 0) return '(+1)';
            return '';
        },
        zanshincardstyle: function(shippai_lst) {
            console.log('### zanshincardstyle ###');
            console.log('zanshincardstyle.shippai_lst', shippai_lst);
            let common_str = 'margin:5px; '
            if (shippai_lst.length > 0) return common_str + 'background-color:#ffc2e5;';
            return common_str +'background-color:#b9dca4;'
        },
        zan: function() {
            this.kata.zan_lst = [this.zan1.trim(), this.zan2.trim(), this.zan3.trim()];
            let waza_lst = [this.kata.waza1.trim(), this.kata.waza2.trim(), this.kata.waza3.trim()];
            console.log('zan_lst:', this.kata.zan_lst);
            console.log('waza_lst:', waza_lst);
            for (let waza of waza_lst) {
                if (!this.kata.zan_lst.includes(waza)) {
                    this.kata.shippai_lst.push(waza);
                }
            }
            console.log('shippai_lst:', this.kata.shippai_lst);
            if (this.kata.shippai_lst.length == 0) {
                shin_rendo = Math.min(this.kata.rendo + 1, 2);
                this.kata.migaki = shin_rendo - this.kata.rendo;
                this.kata.rendo = shin_rendo;
                ++this.seikousu;
            }
            if (this.kazu >= this.tekikazu - 1) {
                console.log('Zanshin');
                console.log('tekishu', this.tekishu);

                axios.post(zanshin_url, {
                    'tekishu': this.tekishu,
                })
                .then(function(response) {
                    console.log('response', response);
                })
                .then(function(error) {
                    console.log('error', error);
                });
                this.showshirengroup = false;
                return;
            }
            if (this.kazu >= this.tekikazu - 2) {
                this.zanbtnlabel = 'Zanshin';
                this.zanbtnclass = 'btn btn-success';
            }

            this.zan1 = '';
            this.zan2 = '';
            this.zan3 = '';
            this.kata = this.tekishu[++this.kazu];
        }
    }
});
