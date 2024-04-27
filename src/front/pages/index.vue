<template>
    <div class="index">
        <Header />
        <Directions class="index__directions" />
        <SortItems />
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
