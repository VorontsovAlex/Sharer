<template>
    <div class="form">
            <div class="form__item">
                <label
                    class="form__label"
                    for="email"
                >
                    Email:
                </label>
                <input
                    v-model="login"
                    type="text"
                    id="email"
                    name="email"
                    placeholder="Email"
                    class="form__input form__input--text"
                >
            </div>
            <div class="form__item">
                <label
                    class="form__label"
                    for="password"
                >
                    Пароль:
                </label>
              <!-- password -  {{password}} -->
                <input
                    v-model="password"
                    type="password"
                    id="password"
                    name="password"
                    placeholder="Пароль"
                    class="form__input form__input--text"
                >
            </div>

          {{errorMessage}}
          <div
              v-if="isRegistered"
              class="form__row"
          >
            <div class="form__checkbox">
              <input
                  type="checkbox"
                  id="remember"
                  class="form__input form__input--checkbox"
              >
              <label
                for="remember"
                class="form__remember"
              >
                Запомнить меня
              </label>
            </div>
             <router-link class="form__action" to="/registration">Зарегистрироваться</router-link>
          </div>
            <div
                v-if="!isRegistered"
                class="form__row"
            >
                 <router-link class="form__action" to="/login">Войти</router-link>
            </div>
            <button
                v-if="isRegistered"
                @click="onLoginClick"
                class="form__action form-action"
            >
                <span class="form-action__text">Войти</span>
            </button>
            <button
                v-else
                :disabled="isRegistrationDisabled"
                @click="onRegistrationClick"
                type="button"
                class="form__action form-action"
            >
                <span  class="form-action__text">Зарегистрироваться</span>
            </button>
    </div>
</template>

<script lang="ts">
    import { Button } from 'ant-design-vue';
    import {tryRegistration, tryLogin} from "~/api/registration";
    import {useUserStore} from "~/store/user";

    export default {
        components: {
            Button,
        },
        props: {
            isRegistered: {
                type: Boolean,
                default: true,
            },
        },
        setup() {
          const router = useRouter()
          const login = ref('FTeam@mail.ru');
          const password = ref('qwe');
          const errorMessage = ref('');
          const {setToken} = useUserStore();
          const onRegistrationClick = async () => {
            const response = await tryRegistration(unref(login), unref(password))

            if (unref(response.status) === 'success') {
              await router.push('/login');
            } else {
              errorMessage.value = unref(response.error)?.data?.detail;
            }
          }
          const onLoginClick = async () => {
            const response = await tryLogin(unref(login), unref(password))

            if (unref(response.data)?.access_token) {
              setToken(unref(response.data).access_token);
              await router.push('/')
            } else {
              errorMessage.value = unref(response.data).error;
            }
          }

          const isRegistrationDisabled = computed(() => unref(password).length === 0 || unref(login).length === 0)
          return {
            login,
            password,
            onRegistrationClick,
            onLoginClick,
            isRegistrationDisabled,
            errorMessage,
          }
        }
    }
</script>

<style lang="scss">
  @use "./styles/form/form";
</style>
