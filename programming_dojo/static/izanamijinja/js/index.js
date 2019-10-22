console.log('kata_lst_length:', kata_lst_length);
let showArr = [];
for (let i = 0; i < kata_lst_length; ++i) showArr.push(false);
console.log('showArr:', showArr);

new Vue({
    el: '#katalst',
    delimiters: ['[[', ']]'],
    data: {
        show: true,
        showArray: showArr,
    },
    methods: {
        isBlank: function(str) {
            return str.length > 0;
        },
        getShow: function(idx) {
            console.log('getShow:', this.showArray);
            console.log('idx', idx);
            return this.showArray[idx];
        },
        shousai: function(idx) {
            console.log('shousai:', this.showArray);
            console.log('idx', idx);
            this.$set(this.showArray, idx, !this.showArray[idx]);
        }
    }
});