<template>
  <div class="back_body">
    <GlobalHeader />

    <h2>Let's SignUp</h2>
    <v-card
      class="card_style"
      max-width="800"
    >
      <v-form v-model="form.valid" @submit.prevent="submitSignup">
        <v-layout wrap>
          <v-flex xs12 sm6 md3><img src="@/assets/img/superman.png"></v-flex>
          <v-flex xs12 sm6 md9>
            <v-container>
              <v-row>
                <v-col
                  cols="12"
                  md="12"
                >
                  <v-text-field
                    v-model="form.email"
                    :rules="form.emailRules"
                    label="メールアドレス"
                    required
                  ></v-text-field>
                </v-col>

                <v-col
                  cols="12"
                  md="12"
                >
                  <v-text-field
                    type="text"
                    v-model="form.username"
                    label="ユーザーネーム"
                    required
                  ></v-text-field>
                </v-col>

                <v-col
                  cols="12"
                  md="12"
                >
                  <v-text-field
                    v-model="form.password"
                    type="password"
                    label="パスワード"
                    required
                  ></v-text-field>
                </v-col>

                <!-- <v-col
                  cols="12"
                  md="12"
                >
                  <v-text-field
                    v-model="form.password2"
                    :rules="form.nameRules"
                    :counter="10"
                    label="パスワード(確認用)"
                    required
                  ></v-text-field>
                </v-col> -->

              </v-row>
              <div class="back-color">
                  <v-btn type="submit" class="start">この内容ではじめる</v-btn>
              </div>
              <div class="login_page">
                <a href="login"><p>アカウントをお持ちですか？</p></a>
              </div>
            </v-container>
          </v-flex>

        </v-layout>
      </v-form>
    </v-card>
  </div>

</template>



<script>
import GlobalHeader from '../components/GlobalHeader'

export default {
  components: {
    GlobalHeader,
  },
  data (){
    return {
      form: {
        valid: false,
        username: '',
        password: '',
        nameRules: [
          v => !!v || 'Name is required',
          v => v.length <= 10 || 'Name must be less than 10 characters',
        ],
        email: '',
        emailRules: [
          v => !!v || 'E-mail is required',
          v => /.+@.+/.test(v) || 'E-mail must be valid',
        ],
      },
      url: '',
      show: true,
    }
  },
  methods: {
    // サインアップボタン押下
    submitSignup: function () {
      // サインアップ
      this.$store.dispatch('auth/signup', {
        email: this.form.email,
        username: this.form.username,
        password: this.form.password
      })
        .then(() => {
          console.log('Signup succeeded.')
          this.$store.dispatch('message/setInfoMessage', { message: '登録が完了しました。ログインしてください。' })
          // クエリ文字列に「next」がなければ、ホーム画面へ
          const next = this.$route.query.next || '/login'
          this.$router.replace(next)
        })
    },
    uploadFile(){
      const file = this.$refs.preview.files[0];
      this.url = URL.createObjectURL(file);
      this.$refs.preview.value = '';
      // 画像のアップ時にfileinputを消す
      this.show = !this.show
    },
    deletePreview(){
      this.url = '';
      // ファイルアップロードの復活
      this.show = !this.show
    },
  },
}
</script>


<style lang="scss" scoped>
label > input {
  display: none;
}

label {
  padding: 0 1rem;
} 

label::after {
  font-size: 1rem;
  color: #888;
  padding-left: 1rem;
}

.back_body{
  background-color: #eee;
  overflow: hidden;
  min-height: 100vh;
  

  h2{
    text-align: center;
    font-size: 45px;
    font-weight: 600;
    text-align: center;
    margin: 30px;
  }

  .card_style{
    margin: 30px auto;
    padding: 50px;
    border-top: 5px solid #33b5e5;

    img {
      width: 115px;
    }

    p{
      font-size: 1.0 rem;
    }

    .back-color{
      button.start{
        background-color: #329eff!important;
        font-size: 0.9rem;
        color: #fff;
        font-weight: bold;
        margin-top: 20px;
        padding: 20px;
        text-decoration: none;
        outline: none;
      }
    }
  }
}

.login_page{
  p{
    color: #329eff;
    margin: 20px 0;
    font-weight: 500;
    font-size: 1rem;
  }

  a{
    text-decoration: none;

    :hover{
      opacity: 0.8;
      transition: 0.5s;
    }
  }
}

.file_input{

  border: 1px solid #999;
  border-radius: 50px;
  width: 100px;
  height: 100px;

  .camera_icon{
    font-size: 3rem;
    position: relative;
    top: 23px;
  }
}

.image_area{
  position: relative;
  bottom: 100px;
  right: 20px;
}
</style>