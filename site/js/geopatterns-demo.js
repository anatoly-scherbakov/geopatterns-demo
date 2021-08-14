// I am not a Javascript developer at all, so this might be a piece of junk.
// Feel free to submit pull requests!

// API handled by AWS Lambda
const API_URL = 'https://dqrura49d0.execute-api.us-east-1.amazonaws.com/generate';
const RANDOM_TEXT_URL = 'https://dqrura49d0.execute-api.us-east-1.amazonaws.com/random-phrase';


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
            text: null,
            method: 0,
            style: ''
        }
    },
    computed: {
        url() {
            let method_name = '';
            if (this.method < 0) {
                method_name = this.methods[0];
            } else if (this.method > this.methods.length - 1) {
                method_name = this.methods[this.methods.length - 1];
            } else {
                method_name = this.methods[this.method];
            }
            let params = new URLSearchParams({
                text: this.text,
                method: method_name,
            });

            console.log(this.method, method_name);
            return `${API_URL}?${params.toString()}`;
        }
    },
    methods: {
        on_key_pressed: function (event) {
            let last_method = this.methods.length - 1;

            if (event.code === 'ArrowUp') {
                if (this.method > 0) {
                    this.method = this.method - 1;
                } else {
                    this.method = last_method;
                }
            }

            if (event.code === 'ArrowDown') {
                if (this.method < last_method) {
                    this.method = this.method + 1;
                } else {
                    this.method = last_method;
                }
            }

            this.download_background_and_update();
        },
        download_background_and_update() {
            let self = this;
            fetch(
                this.url,
            ).catch(
                response => {
                    // Retry a bit later!
                    setTimeout(
                        self.download_background_and_update.bind(self),
                        random_int(1000),
                    );
                },
            ).then(
                response => {
                    if (response.ok) {
                        return response.blob();
                    }

                    setTimeout(
                        self.download_background_and_update.bind(self),
                        random_int(1000),
                    );
                    return null;
                },
            ).then(
                blob => {
                    if (!blob) {
                        return;
                    }

                    let reader = new FileReader();
                    reader.onload = function () {
                        self.style = `background-image: url(${this.result})`;
                    }
                    reader.readAsDataURL(blob);
                }
            );
        }
    },
    watch: {
        text: function () {
            this.download_background_and_update();
        }
    },
    mounted() {
        axios
          .get(RANDOM_TEXT_URL)
          .then(response => (this.text = response.data.text));
        this.download_background_and_update();
    }
}


const app = Vue.createApp(GeopatternsApp)

app.mount('#app');
