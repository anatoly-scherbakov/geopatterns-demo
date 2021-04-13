function random_int(max) {
    return Math.floor(Math.random() * max);
}

const GeopatternsApp = {
    data() {
        return {
            text: '',
            methods: ['hexagons', 'xes', 'overlapping_circles', 'overlapping_rings', 'plaid', 'plus_signs', 'rings', 'sinewaves', 'squares', 'triangles', 'xes']
        }
    },

    methods: {
        style_by_method(method) {
            return 'background-image: url(https://dqrura49d0.execute-api.us-east-1.amazonaws.com/generate?text=' + this.text + '&method=' + method + ')';
        },
    },

    computed: {
        url() {
            return 'https://dqrura49d0.execute-api.us-east-1.amazonaws.com/generate?text=' + this.text
        },

        style() {
            return 'background-image: url(' + this.url + ')';
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
            this.style = this.style_string;
        },
        download_background_and_update() {
            let self = this;
            fetch(this.url).then(this.update_background).catch(function () {
                setInterval(
                    self.update_background.bind(self),
                    random_int(10000),
                )
            });
        }
    },
    watch: {
        text(old_text, new_text) {
            setInterval(
                this.download_background_and_update.bind(this),
                random_int(5000),
            );
        }
    }
});

app.mount('#app');
