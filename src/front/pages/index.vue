<template>
    <div class="index">
        <Header />
        <div class="index__content">
            <Directions />
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            isRegistered: {
                type: Boolean,
                default: false,
            },
        }
    }
</script>

<style lang="scss" scoped>
  @import "./styles/index/index";
</style>
