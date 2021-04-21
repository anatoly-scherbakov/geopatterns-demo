// I am not a Javascript developer at all, so this might be a piece of junk.
// Feel free to submit pull requests!

// API handled by AWS Lambda
const API_URL = 'https://dqrura49d0.execute-api.us-east-1.amazonaws.com/generate';


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
            text: 'Type something ☺',
            method: 'hexagons',
            style: ''
        }
    },
    computed: {
        url() {
            let params = new URLSearchParams({
                text: this.text,
                method: this.method,
            });
            return `${API_URL}?${params.toString()}`;
        },
        style_string() {
            return 'background-image: url(' + this.url + ')';
        }
    },
    methods: {
        update_background() {
            let self = this;
            console.log('update_background()')
            setTimeout(function () {
                self.style = self.style_string;
                console.log(':=');
            }, 1000);
        },
        download_background_and_update() {
            let self = this;
            fetch(this.url).then(function(response) {
                if (response.ok) {
                    console.log('ok', response)
                    response.body.getReader().read().then(
                        self.update_background.bind(self)
                    );
                } else {
                    console.log('error: ', response);
                    setTimeout(
                        self.download_background_and_update.bind(self),
                        random_int(1000),
                    );
                }
            }).catch(function () {
                setTimeout(
                    self.download_background_and_update.bind(self),
                    random_int(1000),
                )
            });
        }
    },
    watch: {
        text: function() {
            this.download_background_and_update();
        }
    },
    mounted() {
        this.download_background_and_update();
    }
}


const app = Vue.createApp(GeopatternsApp)

app.mount('#app');
