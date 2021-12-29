<template>
  <div class="hello">
    <p>The data below is added/removed from the Hubspot Database using Django's CRM Contacts API.</p>
    <v-dialog
      v-model="dialog"
      width="500"
      hide-overlay
      transition="dialog-bottom-transition">
      <v-form ref="addContactForm">
      <v-card style="padding:40px">
        <v-card-title>Adicionar Contato</v-card-title>
        <v-card-text>
        <v-text-field outlined :rules="rules" required type="text" placeholder="Digite seu Nome" v-model="name"/>
        <v-text-field outlined :rules="emailRules" required type="email" placeholder="Digite seu Email" v-model="email"/>
        <v-text-field outlined :rules="rules" required type="phone" return-masked-value mask="(##) #####-####" placeholder="Digite seu Telefone" v-model="phone"/>
        <v-text-field outlined :rules="rules" required type="date" placeholder="Digite sua data de nascimento" v-model="birthdate"/>
        <v-text-field outlined :rules="rules" required type="number" placeholder="Digite seu Peso (Kg)" v-model="weight"/>
        </v-card-text>
      <div>
        <v-btn
          @click="dialog=false"
          style="margin-right: 20px"
        >
          Cancelar
        </v-btn>
       
        <v-btn
          color="blue lighten-2"
          type="submit" 
          value="Salvar" 
          @click="addContact()"
        >
          Salvar
        </v-btn>
      </div>

      </v-card>
      </v-form>
    </v-dialog>
        
      <div class="contactTable">
      <v-row>
      <v-text-field
        style="margin-left:10px"
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        outlined
      ></v-text-field>
      <v-btn
          color="blue lighten-2"
          dark
          style="margin-left:30px; margin-right:10px;"
          height="55px"
          @click="dialog=true"
        >
          Adicionar Contato
        </v-btn>
      </v-row>
      <v-data-table
        :headers="headers"
        :items="contacts"
        :items-per-page="10"
        :search="search"
        class="elevation-2"
      ></v-data-table>
      </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import ContactAPI from '../services/contactService.js'

export default {
  name: "Messages",
  data() {
    return {
      emailRules:[ 
        (v) => !!v || "Esse campo é obrigatório",
         v => !v || /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'O email deve ser valido'],
      rules:[(v) => !!v || "Esse campo é obrigatório"],
      dialog: false,
      search: "",
      subject: "",
      msgBody: "",
      contacts: [],
      name: null,
      phone: null,
      weight: null,
      birthdate: null,
      email: null,
      headers: [
      { text: "Id", value: "id" },
      { text: "Nome", value: "properties.firstname" },
      { text: "Data de Nascimento", value: "properties.date_of_birth" },
      { text: "Email", value: "properties.email" },
      { text: "Telefone", value: "properties.phone" },
      { text: "Peso (Kg)", value: "properties.peso__kg_" },
    ]
    };
  },
  mounted() {
    this.getContacts();
  },
  computed: mapState({
    messages: state => state.messages.messages
  }),
  methods: {
    getContacts: function(){
      ContactAPI.getContacts().then((response) => {
        this.contacts = response.data;
        console.log(this.contacts);
      });
    },
    addContact: function(){
    if (this.$refs.addContactForm.validate()){
       ContactAPI.addContact({
        name: this.name,
        email: this.email,
        birthdate: this.birthdate,
        phone: this.phone,
        weight: this.weight
      }).then((response) => {
        this.dialog=false;
        this.getContacts();
      });
    }
     
    }
    
  },
  created() {
    this.$store.dispatch('messages/getMessages')
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
hr {
  max-width: 65%;
}

.msg {
  margin: 0 auto;
  max-width: 30%;
  text-align: left;
  border-bottom: 1px solid #ccc;
  padding: 1rem;
}

.msg-index {
  color: #ccc;
  font-size: 0.8rem;
  /* margin-bottom: 0; */
}

img {
  width: 250px;
  padding-top: 50px;
  padding-bottom: 50px;
}

.contactTable{
  padding: 50px;
}
</style>
