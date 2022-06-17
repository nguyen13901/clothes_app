<template>
    <div>
        <ul v-for="product in products" :key="product">
           <li>{{product.name}}</li> 
        </ul>
    </div>
</template>

<script>
    import axios from "axios";
    export default {
        name: 'CategoryView',
        data() {
            return {
                products: {},
                category: {},
            }
        },
        mounted() {
            this.getProducts()
        },
        methods: {
            getProducts() {
                const category_slug = this.$route.params.category_slug
            
                axios
                    .get(`/api/v1/products/${category_slug}`)
                    .then(response => {
                        this.category = response.data
                        this.products = this.category.products
                    })
                    .catch(error => {
                        console.log(error)
                    })
            }
        }
    }
</script>

