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
    template: '<div class="ui card"><div class="image" :style="style"></div>',
    props: {
        method: String,
        text: String
    },
    computed: {
        url() {
            return 'https://dqrura49d0.execute-api.us-east-1.amazonaws.com/generate?text=' + this.text + '&method=' + this.method;
        },
        style() {
            console.log(fetch(this.url));
        }
    }
});

app.mount('#app');
