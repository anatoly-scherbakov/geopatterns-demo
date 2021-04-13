function random_int(max) {
    return Math.floor(Math.random() * max);
}

const GeopatternsApp = {
    data() {
        return {
            methods: [
                'hexagons', 'xes', 'overlapping_circles', 'overlapping_rings',
                'plaid', 'plus_signs', 'rings', 'sinewaves', 'squares',
                'triangles', 'xes',
            ],
            input_text: '',
            display_text: ''
        }
    },

    methods: {
        style_by_method(method) {
            return 'background-image: url(https://dqrura49d0.execute-api.us-east-1.amazonaws.com/generate?text=' + this.display_text + '&method=' + method + ')';
        },
        update_text() {
            this.display_text = this.input_text;
        }
    }
}

const app = Vue.createApp(GeopatternsApp)

app.component('preview-card', {
    template: '<div class="ui card"><div class="image" :style="style"></div></div>',
    props: {
        method: String,
        text: String
    },
    data: function() {
        return {
            style: String
        }
    },
    computed: {
        url() {
            return 'https://dqrura49d0.execute-api.us-east-1.amazonaws.com/generate?text=' + this.text + '&method=' + this.method;
        },
        style_string() {
            return 'background-image: url(' + this.url + ')';
        }
    },
    methods: {
        update_background() {
            let self = this;
            setTimeout(function () {
                console.log('Updating: ' + self.method);
                self.style = self.style_string;
            }, 1000);
        },
        download_background_and_update() {
            let self = this;
            console.log('downloading! ' + this.method);
            fetch(this.url).then(this.update_background).catch(function () {
                setTimeout(
                    self.download_background_and_update.bind(self),
                    random_int(10000),
                )
            });
        }
    },
    watch: {
        text: function() {
            this.download_background_and_update();
        }
    }
});

app.mount('#app');
