var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        commands: []
    },
    mounted() {
        fetch
            ('http://localhost:5000/commands')
            .then(res => {
                if (res.status != 200) {
                    alert(res.statusText)
                    return;
                }

                res.json().then(json => (this.commands = json))

            }).catch(console.error);
    },
    methods: {
        runCommand: function (index) {
            fetch
                (`http://localhost:5000/commands/456/run`)
                .then(res => res.json())
                .then(response => alert('Happy coding!'))
        },
    }
})
