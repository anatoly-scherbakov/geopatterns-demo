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
        }
    },
    methods: {
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
        this.download_background_and_update();
    }
}


const app = Vue.createApp(GeopatternsApp)

app.mount('#app');
