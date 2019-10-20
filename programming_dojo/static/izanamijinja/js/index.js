let katas = JSON.parse(document.getElementById('katas_obj').textContent);
console.log('katas', katas)

people = [
    {
        name: 'person1',
        age: 10,
        url: 'https://example.com'
    },
    {
        name: 'person2',
        age: 20,
        url: 'https://example.com'
    },
    {
        name: 'person3',
        age: 30,
        url: 'https://example.com'
    },
]

var app = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
        message: 'Hello Vue!',
        people: people
    },
    methods: {
        greet: (name) => {
            console.log('Hello from ' + name + '!');
        }
    }
});

var example1 = new Vue({
    delimiters: ['[[', ']]'],
    el: '#example-1',
    methods: {
        update: () => {
            // console.log('This is example-1!!')
            people.push({
                name: 'person4',
                age: 40,
                url: 'https://example.com'
            });
        }
    }
})